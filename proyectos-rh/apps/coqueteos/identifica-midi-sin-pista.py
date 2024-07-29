# se encontraron errores al intentar leer la duración de midis. algunos no tenían pista. fue necesario crear un script para hacer un listado de los midis sin pistas y verificarlos

import os
import pretty_midi

# Ruta de la carpeta de archivos MIDI
MIDI_FOLDER = "/home/omnibus/Documents/musica-midi"

# Lista para almacenar los nombres de los archivos sin pista
no_track_files = []

# Recorremos todos los archivos de la carpeta especificada
for file_name in os.listdir(MIDI_FOLDER):
    # Verificamos si el archivo es un archivo MIDI
    if file_name.endswith(".mid") or file_name.endswith(".midi"):
        # Cargamos el archivo MIDI con pretty_midi
        try:
            midi_data = pretty_midi.PrettyMIDI(os.path.join(MIDI_FOLDER, file_name))
        except:
            print(f"Error al cargar el archivo MIDI: {file_name}")
            continue
        
        # Verificamos si hay una pista en el archivo
        if len(midi_data.instruments) == 0:
            no_track_files.append(file_name)

# Creamos un archivo de texto con los nombres de los archivos sin pista
with open("archivos_sin_pista.txt", "w") as f:
    for file_name in no_track_files:
        f.write(file_name + "\n")

