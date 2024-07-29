import stable_whisper

model = stable_whisper.load_model('medium')
# modified model should run just like the regular model but accepts additional parameters
result = model.transcribe('./leydy/28-Bienvenido-Inampues.m4a', regroup=False)  # regroup es variable clave en el ultimo ejercicio se usó false

# srt/vtt
result.to_srt_vtt('./leydy/28-Bienvenido-Inampues2.srt', word_level=False) # word_leve=False también es clave. hay otra variable segment_level=False que al usarla dejó todo dividido en palabras
print('Fin del proceso')
