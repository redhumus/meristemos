#Con ayuda de ChatGPT
# Debe probarse

import openai
from pydub import AudioSegment
from pydub.silence import split_on_silence
#Para revisar
# Autenticación con la API de OpenAI
openai.api_key = "<tu_clave_de_API_de_OpenAI>"

# Carga del archivo de audio
audio_file = AudioSegment.from_file("<nombre_de_archivo>.<extensión>")

# Detección de pausas en el audio
pausas = split_on_silence(audio_file, min_silence_len=1000, silence_thresh=-40)

# Transcripción de cada fragmento de audio
transcriptions = []
for fragmento in pausas:
    # Convertir el fragmento de audio en formato PCM
    fragmento_data = fragmento.raw_data

    # Transcripción del fragmento de audio
    transcription_result = openai.Transcription.create(
        audio=fragmento_data,
        model="whisper-2021.09.09"
    )

    # Agregar el resultado de la transcripción a la lista de transcripciones
    transcriptions.append(transcription_result)

# Agrupar las palabras en frases
frases = []
frase_actual = ""
for transcription_result in transcriptions:
    for word in transcription_result.words:
        # Si la palabra actual es un signo de puntuación, se agrega a la frase actual
        if word.text in [".", ",", ";", ":", "?", "!"]:
            frase_actual += word.text + " "
        # Si la duración de la pausa anterior es mayor a 1 segundo, se agrega una nueva frase
        elif word.start > 0 and word.start - frases[-1][-1]["end"] > 1:
            frases.append({"text": frase_actual.strip(), "start": frases[-1][-1]["end"], "end": word.start})
            frase_actual = word.text + " "
        # En caso contrario, se agrega la palabra actual a la frase actual
        else:
            frase_actual += word.text + " "
    # Agregar la última frase al final de la lista
    frases.append({"text": frase_actual.strip(), "start": transcription_result.words[0].start, "end": transcription_result.words[-1].end})

# Guardar las frases en un archivo de texto
with open("<ruta_de_archivo_local>.txt", "w") as f:
    for i, frase in enumerate(frases):
        f.write(f"Frase {i+1} ({frase['start']} - {frase['end']}): {frase['text']}\n")

