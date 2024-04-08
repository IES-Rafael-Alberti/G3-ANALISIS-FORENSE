import json
import re

# Abre el archivo y lee los datos
with open('datosbrutos.txt', 'r') as f:
    data = f.read()

# Busca los patrones que corresponden a los campos que quieres extraer
pattern = r'"username": "(.*?)",.*?"timestamp": "(.*?)",.*?"content": "(.*?)"'

# Usa regex para encontrar todas las coincidencias
matches = re.findall(pattern, data)

# Crea una lista para almacenar los mensajes
messages = []

# Itera sobre las coincidencias y crea un diccionario para cada mensaje
for match in matches:
    message = {
        "username": match[0],
        "timestamp": match[1],
        "content": match[2]
    }
    messages.append(message)

# Ordena los mensajes de más recientes a menos recientes
messages = sorted(messages, key=lambda x: x['timestamp'], reverse=True)

# Convierte la lista de mensajes en JSON
chat = json.dumps(messages, indent=4)

# Escribe el chat en un archivo
with open('chat.json', 'w') as f:
    f.write(chat)