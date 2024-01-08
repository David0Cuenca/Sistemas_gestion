import requests

def obtener_personajes_por_especie(especie):
    base_url = "https://rickandmortyapi.com/api"
    endpoint = "/character"
    params = {"species": especie}

    try:
        response = requests.get("{base_url}{endpoint}", params=params)

        if response.status_code == 200:
            data = response.json()
            personajes = data["results"]
            if personajes:
                print(f"Personajes de la especie '{especie}':")
                for personaje in personajes:
                    print(f"- {personaje['name']}")
            else:
                print(f"No se encontraron personajes de la especie '{especie}'.")
        else:
            print("Error en la solicitud. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

especie_usuario = input("Ingrese la especie para buscar personajes: ")
obtener_personajes_por_especie(especie_usuario)
