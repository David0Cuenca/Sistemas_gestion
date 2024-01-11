import requests

def obtener_personajes_por_especie(especie):
    base_url = "https://rickandmortyapi.com/api/character"
    pagina = 1

    try:
        while True:
            response = requests.get(f"{base_url}?page={pagina}&species={especie}")
            if response.status_code == 200:
                data = response.json()
                personajes = data["results"]
                if personajes:
                    print(f"Personajes de la especie '{especie}' - Página {pagina}")
                    for personaje in personajes:
                        print(f"- {personaje['name']}")
                    pagina += 1
                else:
                    print(f"No se encontraron más personajes de la especie '{especie}'.")
                    break
            else:
                print(f"Error en la solicitud. Código de estado: {response.status_code}")
                break
    except Exception as e:
        print(f"Error: {e}")

especie_usuario = input("Ingrese la especie para buscar personajes: ")

obtener_personajes_por_especie(especie_usuario)
