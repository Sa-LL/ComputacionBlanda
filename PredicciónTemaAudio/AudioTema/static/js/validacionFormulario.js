
function validarFecha(){
    alert(fecha)
}

function inicial(){
    var fecha = document.querySelector("#fechaNacimiento");
    fecha.addEventListener("input", validarFecha, false)
}

validarFecha()