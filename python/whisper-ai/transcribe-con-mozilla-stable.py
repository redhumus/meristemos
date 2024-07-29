#pip install deepspeech==0.9.3 -f https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-cp37-cp37m-linux_x86_64.whl
#Debe probarse
#Con ayuda de ChatGPT



import deepspeech
import wave
import numpy as np
import stable_whisper

# Load the DeepSpeech model
model_path = '/path/to/deepspeech-0.9.3-models.pbmm'
model = deepspeech.Model(model_path)

# Set the beam width and language model weight for the DeepSpeech model
model.setBeamWidth(500)
model.enableExternalScorer('/path/to/deepspeech-0.9.3-models.scorer')
lm_alpha = 0.75
lm_beta = 1.85
model.setScorerAlphaBeta(lm_alpha, lm_beta)

# Load the audio file using the wave module
audio_file = wave.open('28-Bienvenido-Inampues.wav', 'rb')
sample_rate = audio_file.getframerate()

# Read the audio data as a numpy array
audio_data = np.frombuffer(audio_file.readframes(-1), np.int16)

# Transcribe the audio using the DeepSpeech model
text = model.stt(audio_data)

# Generate the subtitle file using stable-ts
result = stable_whisper.Transcript([text], [0], [len(audio_data)/sample_rate])
result.to_srt_vtt('28-Bienvenido-Inampues2.srt')
print('Fin del proceso')

