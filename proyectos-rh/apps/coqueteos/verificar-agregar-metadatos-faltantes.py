# creado para agregar los datos que el script inicial no

import os
import sqlite3
import datetime
import pretty_midi

# Conexión a la base de datos
conn = sqlite3.connect('mididb.sqlite')
c = conn.cursor()

# Agregar columnas de metadatos faltantes
try:
    c.execute('''ALTER TABLE features ADD COLUMN duration REAL''')
    print("Se ha agregado la columna 'duration'")
except sqlite3.OperationalError:
    print("La columna 'duration' ya existe")

try:
    c.execute('''ALTER TABLE features ADD COLUMN modified TIMESTAMP''')
    print("Se ha agregado la columna 'modified'")
except sqlite3.OperationalError:
    print("La columna 'modified' ya existe")

# Obtener la lista de archivos de la carpeta midi
midi_folder = '/home/omnibus/Documents/musica-midi'
midi_files = [f for f in os.listdir(midi_folder) if f.endswith('.mid')]

# Iterar sobre los archivos de midi
for midi_file in midi_files:
    file_path = os.path.join(midi_folder, midi_file)

    # Obtener los metadatos usando pretty_midi
    try:
        pm = pretty_midi.PrettyMIDI(file_path)
    except Exception as e:
        print(f"No se pudo leer el archivo {midi_file}: {e}")
        continue

    # Verificar si el archivo ya existe en la base de datos
    c.execute("SELECT * FROM features WHERE file_name=?", (midi_file,))
    result = c.fetchone()

    # Si el archivo existe, actualizar los metadatos
    if result:
        row_id = result[0]
        duration = pm.get_end_time()
        modified = os.path.getmtime(file_path)
        modified_str = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''UPDATE features SET duration=?, modified=? WHERE id=?''', (duration, modified_str, row_id))
    # Si el archivo no existe, agregarlo a la base de datos
    else:
        duration = pm.get_end_time()
        modified = os.path.getmtime(file_path)
        modified_str = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''INSERT INTO features (file_name, title, artist, genre, duration, modified, has_piano, has_drums, has_bass, has_guitar, has_strings, has_brass, has_woodwinds, processed)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (midi_file, midi_file, '', '', duration, modified_str, 0, 0, 0, 0, 0, 0, 0, 0))

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

