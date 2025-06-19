# Proyecto Python: Buscador de información de países usando la API REST Countries
import requests

def buscar_pais(nombre_pais):
    url= f"https://restcountries.com/v3.1/name/{nombre_pais}"
    try:
        respuesta= requests.get(url)
        respuesta.raise_for_status()
        datos= respuesta.json
        
        if datos:
            pais= datos[0]
            nombre= pais.get("name")
                
        
        else:
            print("No se encontró información sobre el país mencionado")
            
            
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e} ")




if __name__=="__main__:":
    pais= input("Por favor ingresa el nombre del país: ")
    buscar_pais(pais)