import pygame
import random
import time
import math
from simpleai.search import SearchProblem, astar, depth_first, breadth_first
WIDTH = 480
HEIGHT = 480
COSTS = {
        "up" : 1, #Arriba
        "down"  : 1, #Abajo
        "left" : 1, #Izquierda
        "right" : 1 #Derecha
        }


class SnakeProblem(SearchProblem):

    def __init__(self, map, goal, tam):
        """
        El mapa estara representado de forma (cabeza, lista de cuerpos)
        """
        self.goal = goal
        self.initial = map
        self.tamanioMap = tam
        self.actualAction = None
        super(SnakeProblem, self).__init__(initial_state = self.initial)

    def actions(self, state):
        """
        Define las acciones posibles para cada estado
        """
        actions = []
        bodies = state[1]
        for action in COSTS:
            newState = self.pseudoResult(state, action)
            newHead = newState[0]
            if (newHead[0] >= 0 and newHead[0] < self.tamanioMap[0] and
                newHead[1] >= 0 and newHead[1] < self.tamanioMap[1] and
                newHead not in bodies):
                actions.append(action)
        return actions


    def pseudoResult(self, state, action):
        """
        1. Arriba, 2.Abajo, 3.Izquierda, 4.Derecha
        """

        """
        Parte donde toma en cuenta el estado anterior para hacer una poda de los
        estados invalidos
        """
        if self.actualAction == "up" and action == "down":
            return ((self.tamanioMap[0] + 1, self.tamanioMap[1] + 1), None)
        if self.actualAction == "down" and action == "up":
            return ((self.tamanioMap[0] + 1, self.tamanioMap[1] + 1), None)
        if self.actualAction == "right" and action == "left":
            return ((self.tamanioMap[0] + 1, self.tamanioMap[1] + 1), None)
        if self.actualAction == "left" and action == "right":
            return ((self.tamanioMap[0] + 1, self.tamanioMap[1] + 1), None)



        fil, col = state[0]
        body = ()
        if state[1]:
            body = list(state[1])
            body.insert(0, (fil, col))
            body.pop(-1)

        #print(fil, col)
        if action == "up":
            fil -= 1
        elif action == "down":
            fil += 1
        elif action == "left":
            col -= 1
        elif action == "right":
            col += 1

        newState = ((fil, col), tuple(body))
        return newState
    def result(self, state, action):
        """
        1. Arriba, 2.Abajo, 3.Izquierda, 4.Derecha
        """
        fil, col = state[0]
        body = ()
        if state[1]:
            body = list(state[1])
            body.insert(0, (fil, col))
            body.pop(-1)

        #print(fil, col)
        if action == "up":
            fil -= 1
        elif action == "down":
            fil += 1
        elif action == "left":
            col -= 1
        elif action == "right":
            col += 1
        self.actualAction = action
        newState = ((fil, col), tuple(body))
        return newState


    def is_goal(self, state):
        return state[0] == self.goal

    def costs(self, state, action, state2):
        return COSTS[action]

    def heuristic(self, state):
        x, y = state[0]
        gx, gy = self.goal
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


class Head(pygame.sprite.Sprite):
    def __init__(self, pIni, tam_x, tam_y):
        pygame.sprite.Sprite.__init__(self)
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.image = pygame.Surface([tam_x, tam_y])
        self.rect = self.image.get_rect()
        self.image.fill([255, 0, 0])
        self.pos_head = pIni
        self.rect.topleft = pIni

    def update(self):
        #Pos head es la posicion en la matriz
        #print (self.pos_head)
        self.rect.x = self.pos_head[1] * tam_x
        self.rect.y = self.pos_head[0] * tam_y

class Body(pygame.sprite.Sprite):
    def __init__(self, pIni, tam_x, tam_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([tam_x, tam_y])
        self.rect = self.image.get_rect()
        self.image.fill([0, 255, 0])
        self.pos = pIni
        self.rect.x = self.pos[1] * tam_x
        self.rect.y = self.pos[0] * tam_y

    def update(self):
        #Pos es la posicion en la matriz
        self.rect.x = self.pos[1] * tam_x
        self.rect.y = self.pos[0] * tam_y

class Food(pygame.sprite.Sprite):
    def __init__(self, pIni, tam_x, tam_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([tam_x, tam_y])
        self.rect = self.image.get_rect()
        self.image.fill([0, 0, 255])
        self.pos = pIni
        self.rect.x = self.pos[1] * tam_x
        self.rect.y = self.pos[0] * tam_y


class Snake:
    """
    Tiene muchas similitudes con el snake que no es grafico, la diferencia es
    que la cabeza y el cuerpo seran sprites, estos tendran dos posiciones, la
    posicion de la matriz y la conversion al plano cartesiano de esta posicion.
    Ademas tendra una direccion base por si no cambia de direccion
    """
    def __init__(self, lim_filas, lim_columnas, tam_x, tam_y, game):
        self.head = Head([0, 0], tam_x, tam_y)
        self.body = []
        self.game = game
        self.game.allSprites.add(self.head)
        self.lim_filas = lim_filas - 1
        self.lim_col = lim_columnas - 1
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.dir = 4

    def grow(self):
        """
        Funcion que le agregara un cuadro a la serpiente cuando coma
        """
        newBody = None
        if self.body: #Si tiene elementos el cuerpo, le agregamos uno nuevo que sea igual al ultimo
            newBody = Body(self.body[-1].pos, self.tam_x, self.tam_y)
        else:
            newBody = Body(self.head.pos_head, self.tam_x, self.tam_y)

        self.game.allSprites.add(newBody)
        self.game.body.add(newBody)
        self.body.append(newBody)
        #print (len(self.body))


    def movement_head2(self, dir):
        """
        1. Arriba, 2.Abajo, 3.Izquierda, 4.Derecha, se debe tener en cuenta que
        si se le da arriba pero arriba hay cuerpo no puede hacer este desplazamiento
        Se debe recordar que el mapa es una matriz, fila columna, no posicion x, y
        """
        if self.body:
            self.movement_body()
        self.dir = dir
        if dir == 1:
            self.head.pos_head = [self.head.pos_head[0] - 1, self.head.pos_head[1]]
        elif dir == 2:
            self.head.pos_head = [self.head.pos_head[0] + 1, self.head.pos_head[1]]

        elif dir == 3:
            self.head.pos_head = [self.head.pos_head[0], self.head.pos_head[1] - 1]

        else:
            self.head.pos_head = [self.head.pos_head[0], self.head.pos_head[1]  + 1]


        return self.keepPlaying()


    def keepPlaying(self):
        #Condicional de fin del juego por salirse de los limites
        if (self.head.pos_head[0] < 0 or self.head.pos_head[1] < 0 or
            self.head.pos_head[0] > self.lim_filas or self.head.pos_head[1] > self.lim_col):
            return False
        elif self.head.pos_head in [i.pos for i in self.body]: #Fin del juego por colision
            return False
        else:
            return True

    def movement_body(self):
        newBody = Body(self.head.pos_head, self.tam_x, self.tam_y)
        self.game.allSprites.add(newBody)
        self.body.insert(0, newBody)
        self.game.allSprites.remove(self.body[-1])
        self.body.pop(-1)

class Game:

    def __init__(self, lim_filas, lim_columnas, tam_x, tam_y):
        #Inicializacion
        pygame.init()
        self.lim_filas = lim_filas
        self.lim_columnas = lim_columnas
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.gameDisplay = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        #Empieza un nuevo juego
        self.dir = 4
        self.allSprites = pygame.sprite.Group()
        self.body = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()

        self.snake = Snake(self.lim_filas, self.lim_columnas, self.tam_x, self.tam_y, self) #Enviamos la informacion de la clase game
        self.controlSearchProblem()

    def createMap(self):
        map = []
        #print(self.food.pos)
        for i in range(self.lim_filas):
            row = []
            for j in range(self.lim_columnas):
                if [i, j] == self.snake.head.pos_head:
                    row.append('h')
                elif [i, j] in [i.pos for i in self.snake.body]:
                    row.append('b')
                elif [i, j] == self.food.pos:
                    #print(i, j)
                    row.append('f')
                else:
                    row.append('*')
            map.append(tuple(row))
        map = tuple(map)
        return map


    def controlSearchProblem(self):
        self.createFood()
        result = self.searchOne()
        try:
            self.actions = [i[0] for i in result.path()[1:]]
            print(self.actions)
        except:
            print("No puede llegar a la comida")
            #map = self.createMap()
            #for i in map:
                #print(i)
        #print("hola")
        #print(self.actions)
        else:
            self.playWithSearchProblem()


    def playWithSearchProblem(self):
        self.playing = True
        """
        print("Goal: ", self.food.pos)
        #print("Head:", self.snake.head.pos_head)
        print("Actions: ", self.actions)
        map = self.createMap()
        for i in map:
            print(i)
        """
        while self.playing and self.actions: #and i < 10:
            self.clock.tick(20)
            self.events()
            self.update()
            self.draw()

        if self.playing:
            self.controlSearchProblem()


    def searchOne(self):

        food = (self.food.pos[0], self.food.pos[1])
        head = (self.snake.head.pos_head[0], self.snake.head.pos_head[1])

        body = [i.pos for i in self.snake.body]
        if body:
            body = [tuple(i) for i in body]
        else:
            body = ()
        state = (head, tuple(body))
        problem = SnakeProblem(state, food, [self.lim_filas, self.lim_columnas])
        #result = depth_first(problem, graph_search = True)
        result = astar(problem, graph_search = False)
        return result

    def update(self):
        #Movimiento de la serpiente
        self.transformAction()
        self.actions.pop(0)
        self.playing  = self.snake.movement_head2(self.dir) and self.playing

        ls_col = pygame.sprite.spritecollide(self.snake.head, self.foods, True)
        if ls_col:
            self.snake.grow()
        self.allSprites.update()

    def transformAction(self):
        if self.actions[0] == "up":
            self.dir = 1
        elif self.actions[0] == "down":
            self.dir = 2
        elif self.actions[0] == "left":
            self.dir = 3
        elif self.actions[0] == "right":
            self.dir = 4


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Se termina de jugar y de correr
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #ciclo de dibujo
        self.gameDisplay.fill([0, 0, 0])
        self.allSprites.draw(self.gameDisplay)
        pygame.display.flip()

    def createFood(self):
        posNewFood = [random.randrange(0, self.lim_filas),
                      random.randrange(0, self.lim_columnas)]
        while (posNewFood == self.snake.head.pos_head or
               posNewFood in [i.pos for i in self.snake.body]):
               #Para que la comida no aparexca donde este la serpiente
               posNewFood = [random.randrange(0, self.lim_filas),
                             random.randrange(0, self.lim_columnas)]
        food = Food(posNewFood, self.tam_x, self.tam_y)
        self.food = food
        #print("new food", self.food.pos)
        self.foods.add(food)
        self.allSprites.add(food)

    def showGoScreen(self):
        #Para terminar o seguir el juego
        map = self.createMap()
        print(self.dir)
        for i in map:
            print(i)
        time.sleep(2)

if __name__ == '__main__':
    lim_filas = 10
    lim_columnas = 10
    tam_x = int(WIDTH/lim_columnas)
    tam_y = int(HEIGHT/lim_filas)
    g = Game(lim_filas, lim_columnas, tam_x, tam_y)
    while g.running:
        """
        Este ciclo maneja cada vez que se acaba el juego, ya que dentro hay otro
        ciclo que maneja el juego como tal
        """
        g.new()
        g.showGoScreen()
