# Proyecto Python: Buscador de información de países usando la API REST Countries
import requests

def buscar_pais(nombre_pais):
    url= f"https://restcountries.com/v3.1/name/{nombre_pais}"
    try:
        respuesta= requests.get(url)
        respuesta.raise_for_status()
        datos= respuesta.json()
        
        if datos:
            pais= datos[0]
            nombre= pais.get("name", {}).get("common","Desconocido")
            capital= pais.get("capital", ["Desconocida"])[0]
            poblacion= pais.get("population","Desconocida")
            moneda = list(pais.get("currencies", {}).keys())[0] if pais.get("currencies") else "Desconocida"
            bandera= pais.get("flags",{}).get("png", "")
            
            print(f"El país es: {nombre}")      
            print(f"La capital es: {capital}")  
            print(f"La población es: {poblacion}")
            print(f"La moneda del país es: {moneda}")
            print(f"La bandera del país es: {bandera}")
        else:
            print("No se encontró información sobre el país mencionado")
            
            
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e} ")


if __name__=="__main__":
    print("Buscador de información de países")
    pais= input("Por favor ingresa el nombre del país: ")
    buscar_pais(pais)

