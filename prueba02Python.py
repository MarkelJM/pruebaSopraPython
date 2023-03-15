#Lista con diccionario con los datos de las personas:

lista_personas = [
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20},
    {"sexo": "M", "edad": 22},
    {"sexo": "F", "edad": 17},
    {"sexo": "M", "edad": 30},
    {"sexo": "F", "edad": 12},
    {"sexo": "F", "edad": 20}]
    


def clasificar_personas(lista):


    #valores iniciales
    mayores_edad = 0
    mayores = 9
    menores_edad = 0
    masculinos_mayores_edad = 0
    femeninos_menores_edad = 0
    mujeres = 0
    #Entramos en la lista y comparamos uno a uno las personas
    for person in lista:
        #filtramos en el diccionario 1. por edad para saber si son mayores de edad o no
        if person["edad"] >= 18:
            mayores_edad += 1
            if person["sexo"] == "M":
                masculinos_mayores_edad += 1
        else:
            menores_edad += 1
            if person["sexo"] == "F":
                femeninos_menores_edad += 1
        if person["sexo"] == "F":
            mujeres += 1

    porcentaje_mayores_edad = (mayores_edad / len(lista)) * 100
    porcentaje_mujeres = (mujeres / len(lista)) * 100

    #Diccionario para indicar todos los valores solicitados
    resultados = {
        "mayores_edad": mayores_edad,
        "menores_edad": menores_edad,
        "hombres_mayores_edad": masculinos_mayores_edad,
        "mujeres_menores_edad": femeninos_menores_edad,
        "porcentaje_mayores_edad": porcentaje_mayores_edad,
        "porcentaje_mujeres": porcentaje_mujeres
    }
    #print(resultados)
    return resultados


print(clasificar_personas(lista_personas))


print("TESTS")
def test_clasificar_personas():
    personas = [
        {"sexo": "M", "edad": 22},
        {"sexo": "F", "edad": 17},
        {"sexo": "M", "edad": 30},
        {"sexo": "F", "edad": 12},
        {"sexo": "F", "edad": 20},
        
    ]
    resultados = clasificar_personas(personas)
    assert resultados["mayores_edad"] == 3
    assert resultados["menores_edad"] == 2
    assert resultados["hombres_mayores_edad"] == 2
    assert resultados["mujeres_menores_edad"] == 1
    assert resultados["porcentaje_mayores_edad"] == 60.0
    assert resultados["porcentaje_mujeres"] == 60.0
    
