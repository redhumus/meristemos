import pandas as pd

# Leer el archivo CSV
archivo_csv = 'tu_archivo.csv'
df = pd.read_csv(archivo_csv)

# Iterar sobre todas las columnas y eliminar espacios en blanco al inicio y al final
for col in df.columns:
    if df[col].dtype == 'object':  # Solo si la columna contiene texto
        df[col] = df[col].str.strip()

# Guardar el DataFrame modificado en un nuevo archivo CSV
nuevo_archivo_csv = 'nuevo_archivo.csv'
df.to_csv(nuevo_archivo_csv, index=False)

print(f'Archivo CSV limpiado guardado en {nuevo_archivo_csv}')

