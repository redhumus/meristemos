# Ultima versión con pretty-midi, argparse e incorporación en la bd de archivos  procesados con algun error marcados como no procesados


# En este script, los datos del MIDI folder se agregan como argumento al momento de ejecutar el script en la línea de comandos. Para hacerlo, se debe escribir el nombre de la carpeta donde se encuentran los archivos MIDI después del nombre del script:
# python3 script.py MIDI_FOLDER
# Donde MIDI_FOLDER es el nombre de la carpeta donde se encuentran los archivos MIDI que se desean procesar.


import os
import sqlite3
import argparse
import datetime
import pretty_midi

# Argumentos de la línea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('midi_folder', type=str, help='Carpeta con los archivos MIDI')
parser.add_argument('database_name', type=str, help='Nombre de la base de datos SQLite')
args = parser.parse_args()

# Conexión a la base de datos
conn = sqlite3.connect(args.database_name)
c = conn.cursor()

# Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS mididata
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             artist TEXT,
             genre TEXT,
             album TEXT,
             year TEXT,
             duration REAL,
             modified TEXT,
             processed TEXT)''')

# Obtener lista de archivos MIDI
midi_files = [os.path.join(args.midi_folder, f) for f in os.listdir(args.midi_folder) if f.endswith('.mid')]

# Recorrer archivos MIDI
for midi_file in midi_files:
    try:
        # Cargar archivo MIDI con pretty_midi
        midi_data = pretty_midi.PrettyMIDI(midi_file)

        # Verificar existencia de metadatos
        title = midi_data.get_title() or os.path.splitext(os.path.basename(midi_file))[0]
        artist = midi_data.get_artist() or ''
        genre = midi_data.get_genre() or ''
        album = midi_data.get_album() or ''
        year = midi_data.get_date() or ''
        duration = midi_data.get_end_time() or ''
        modified = datetime.datetime.fromtimestamp(os.path.getmtime(midi_file)).strftime('%Y-%m-%d %H:%M:%S')
        processed = 'yes'

        # Insertar metadatos en la base de datos
        c.execute("INSERT INTO mididata (title, artist, genre, album, year, duration, modified, processed) \
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (title, artist, genre, album, year, duration, modified, processed))
        conn.commit()

    except Exception as e:
        # En caso de error, registrar archivo no procesado en la base de datos
        processed = 'no'
        c.execute("INSERT INTO mididata (title, processed) VALUES (?, ?)", (os.path.splitext(os.path.basename(midi_file))[0], processed))
        conn.commit()
        print(f"Error procesando {midi_file}: {e}")

# Cerrar conexión a la base de datos
conn.close()

