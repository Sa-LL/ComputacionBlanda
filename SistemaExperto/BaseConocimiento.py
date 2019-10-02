from pyDatalog import pyDatalog

pyDatalog.create_terms('sintoma_de, tiene_sintoma, tiene_tp, tiene_aerofagia, tiene_apendicitis, tiene_pancreatitis')
pyDatalog.create_terms('tiene_bronquitis, tiene_dengue, tiene_derramepleural, tiene_encefalitis,  regla_enfermedad')
pyDatalog.create_terms('dolor_en_el_pecho, dificultad_respiratoria, tos, expectoracion_con_sangre, sudoracion_excesiva')
pyDatalog.create_terms('fatiga, fiebre, perdida_de_peso, sibilancias,  distension_abdominal, dolor_abdominal')
pyDatalog.create_terms('ruidos_intestinales, eructos, meteorismo, escalofrios, vomitos, temblores, estreñimiento') 
pyDatalog.create_terms('diarrea, nauseas, falta_de_apetito, sudoracion, abdomen_con_gases, hipo, indigestion')
pyDatalog.create_terms('mucosidad_oral, dificultad_respiratoria, erupcion_en_la_piel, sangre_encias, debilidad_general') 
pyDatalog.create_terms('dolor_muscular, dolor_de_garganta, dolor_toracico, convulciones, dolor_de_cabeza, apatia,confusion') 
pyDatalog.create_terms('Somnolencia, enf_1, enf_2, enf_3, enf_4, enf_5, enf_6, enf_7, enf_8, enf_9, Caso, regla_enfermedad')
#*Casos base*/
#/*Caso 1*/
#/*Tuberculosis pulmonar*/
+tiene_sintoma(enf_1, dificultad_respiratoria) 
+tiene_sintoma(enf_1, dolor_en_el_pecho) 
+tiene_sintoma(enf_1, tos) 
+tiene_sintoma(enf_1, expectoracion_con_sangre)
+tiene_sintoma(enf_1, sudoracion_excesiva)
+tiene_sintoma(enf_1, fatiga)
+tiene_sintoma(enf_1, fiebre)
+tiene_sintoma(enf_1, perdida_de_peso)
+tiene_sintoma(enf_1, sibilancias)
#/*Caso 2*/
#/*Aerofagia*/
+tiene_sintoma(enf_2, distension_abdominal) 
+tiene_sintoma(enf_2, dolor_abdominal)
+tiene_sintoma(enf_2, ruidos_intestinales)
+tiene_sintoma(enf_2, eructos)
+tiene_sintoma(enf_2, meteorismo)
#/*Caso 3*/
#/*Apendicitis*/
+tiene_sintoma(enf_3, dolor_abdominal)
+tiene_sintoma(enf_3, escalofrios)
+tiene_sintoma(enf_3, vomitos)
+tiene_sintoma(enf_3, temblores)
+tiene_sintoma(enf_3, estreñimiento)
+tiene_sintoma(enf_3, nauseas)
+tiene_sintoma(enf_3, falta_de_apetito)
+tiene_sintoma(enf_3, fiebre)
#/*Caso 4*/
#/*Pancreatitis*/
+tiene_sintoma(enf_4, fiebre)
+tiene_sintoma(enf_4, nauseas)
+tiene_sintoma(enf_4, vomitos)
+tiene_sintoma(enf_4, sudoracion)
+tiene_sintoma(enf_4, abdomen_con_gases)
+tiene_sintoma(enf_4, hipo)
+tiene_sintoma(enf_4, indigestion)
+tiene_sintoma(enf_4, distension_abdominal)
#/*Caso 5*/
#/*Bronquitis*/
+tiene_sintoma(enf_5, tos)
+tiene_sintoma(enf_5, mucosidad_oral)
+tiene_sintoma(enf_5, dificultad_respiratoria)
+tiene_sintoma(enf_5, fiebre)
#/*Caso 6*/
#/*Dengue*/
+tiene_sintoma(enf_6, fiebre)
+tiene_sintoma(enf_6, nauseas)
+tiene_sintoma(enf_6, vomitos)
+tiene_sintoma(enf_6, erupcion_en_la_piel)
+tiene_sintoma(enf_6, sangre_encias)
+tiene_sintoma(enf_6, debilidad_general)
+tiene_sintoma(enf_6, dolor_muscular)
+tiene_sintoma(enf_6, tos)
+tiene_sintoma(enf_6, dolor_de_garganta)
#/*Caso 7*/
#/*Derrame pleural*/
+tiene_sintoma(enf_7, dolor_toracico)
+tiene_sintoma(enf_7, tos)
+tiene_sintoma(enf_7, dificultad_respiratoria)
+tiene_sintoma(enf_7, fiebre)             
+tiene_sintoma(enf_7, hipo)
#/*Caso 8*/
#/*Encefalitis*/
+tiene_sintoma(enf_8, fiebre)
+tiene_sintoma(enf_8, convulciones)
+tiene_sintoma(enf_8, dolor_de_cabeza)
+tiene_sintoma(enf_8, apatia)
+tiene_sintoma(enf_8, confusion)
+tiene_sintoma(enf_8, vomitos)

#/*Reglas*/
tiene_tp(Caso)<= tiene_sintoma(Caso, dificultad_respiratoria) & tiene_sintoma(Caso, dolor_en_el_pecho) & tiene_sintoma(Caso, tos) & tiene_sintoma(Caso, expectoracion_con_sangre) & tiene_sintoma(Caso, sudoracion_excesiva) & tiene_sintoma(Caso, fatiga) & tiene_sintoma(Caso, fiebre) & tiene_sintoma(Caso, perdida_de_peso) & tiene_sintoma(Caso, sibilancias)
	
tiene_aerofagia(Caso)<= tiene_sintoma(Caso,distension_abdominal) & tiene_sintoma(Caso, dolor_abdominal) & tiene_sintoma(Caso, ruidos_intestinales) & tiene_sintoma(Caso, eructos) & tiene_sintoma(Caso, meteorismo)
	
tiene_apendicitis(Caso)<= tiene_sintoma(Caso, dolor_abdominal) & tiene_sintoma(Caso, escalofrios) & tiene_sintoma(Caso, vomitos) & tiene_sintoma(Caso, temblores) & tiene_sintoma(Caso, estreñimiento) & tiene_sintoma(Caso, nauseas) & tiene_sintoma(Caso, falta_de_apetito) & tiene_sintoma(Caso, fiebre)

tiene_pancreatitis(Caso)<= tiene_sintoma(Caso, fiebre) & tiene_sintoma(Caso, nauseas) & tiene_sintoma(Caso, vomitos) & tiene_sintoma(Caso, sudoracion) & tiene_sintoma(Caso, abdomen_con_gases) & tiene_sintoma(Caso, hipo) & tiene_sintoma(Caso, indigestion) & tiene_sintoma(Caso, distension_abdominal)
	
tiene_bronquitis(Caso)<= tiene_sintoma(Caso, tos) & tiene_sintoma(Caso, mucosidad_oral) & tiene_sintoma(Caso, dificultad_respiratoria) & tiene_sintoma(Caso, fiebre)
	
tiene_dengue(Caso)<= tiene_sintoma(Caso, fiebre) & tiene_sintoma(Caso, nauseas) & tiene_sintoma(Caso, vomitos) & tiene_sintoma(Caso, erupcion_en_la_piel) & tiene_sintoma(Caso, sangre_encias) & tiene_sintoma(Caso, debilidad_general) & tiene_sintoma(Caso, dolor_muscular) & tiene_sintoma(Caso, tos) & tiene_sintoma(Caso, dolor_de_garganta)
	
tiene_derramepleural(Caso)<= tiene_sintoma(Caso,dolor_toracico) & tiene_sintoma(Caso, tos) & tiene_sintoma(Caso, dificultad_respiratoria) & tiene_sintoma(Caso, fiebre)  & tiene_sintoma(Caso, hipo)
	
tiene_encefalitis(Caso)<= tiene_sintoma(Caso, fiebre) & tiene_sintoma(Caso, convulciones) & tiene_sintoma(Caso, dolor_de_cabeza) & tiene_sintoma(Caso, apatia) & tiene_sintoma(Caso, confusion) & tiene_sintoma(Caso, vomitos)
	
	
def regla_enfermedad(nombre_enf):
	if tiene_tp(nombre_enf):
		return 1
	elif tiene_aerofagia(nombre_enf):
		return 2
	elif tiene_apendicitis(nombre_enf):
		return 3
	elif tiene_pancreatitis(nombre_enf):
		return 4
	elif tiene_bronquitis(nombre_enf):
		return 5
	elif tiene_dengue(nombre_enf):
		return 6
	elif tiene_derramepleural(nombre_enf):
		return 7
	elif tiene_encefalitis(nombre_enf):
		return 8
		
		
		
