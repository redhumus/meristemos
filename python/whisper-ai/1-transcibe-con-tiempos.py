import os
from pydub import AudioSegment
from whisper import DecodingOptions, DecodingResult
import whisper

# ruta del archivo de audio
archivo_audio = "audio.wav"

# duración en segundos de cada segmento
duracion_segmento = 10

# ruta del archivo de salida de la transcripción
ruta_salida = "transcripcion.txt"

# carga el modelo pre-entrenado
#whispereando tomado de https://github.com/openai/whisper

model = whisper.load_model("base")


#elegir idioma

import ipywidgets as widgets

languages = {"af_za": "Afrikaans", "am_et": "Amharic", "ar_eg": "Arabic", "as_in": "Assamese", "az_az": "Azerbaijani", "be_by": "Belarusian", "bg_bg": "Bulgarian", "bn_in": "Bengali", "bs_ba": "Bosnian", "ca_es": "Catalan", "cmn_hans_cn": "Chinese", "cs_cz": "Czech", "cy_gb": "Welsh", "da_dk": "Danish", "de_de": "German", "el_gr": "Greek", "en_us": "English", "es_419": "Spanish", "et_ee": "Estonian", "fa_ir": "Persian", "fi_fi": "Finnish", "fil_ph": "Tagalog", "fr_fr": "French", "gl_es": "Galician", "gu_in": "Gujarati", "ha_ng": "Hausa", "he_il": "Hebrew", "hi_in": "Hindi", "hr_hr": "Croatian", "hu_hu": "Hungarian", "hy_am": "Armenian", "id_id": "Indonesian", "is_is": "Icelandic", "it_it": "Italian", "ja_jp": "Japanese", "jv_id": "Javanese", "ka_ge": "Georgian", "kk_kz": "Kazakh", "km_kh": "Khmer", "kn_in": "Kannada", "ko_kr": "Korean", "lb_lu": "Luxembourgish", "ln_cd": "Lingala", "lo_la": "Lao", "lt_lt": "Lithuanian", "lv_lv": "Latvian", "mi_nz": "Maori", "mk_mk": "Macedonian", "ml_in": "Malayalam", "mn_mn": "Mongolian", "mr_in": "Marathi", "ms_my": "Malay", "mt_mt": "Maltese", "my_mm": "Myanmar", "nb_no": "Norwegian", "ne_np": "Nepali", "nl_nl": "Dutch", "oc_fr": "Occitan", "pa_in": "Punjabi", "pl_pl": "Polish", "ps_af": "Pashto", "pt_br": "Portuguese", "ro_ro": "Romanian", "ru_ru": "Russian", "sd_in": "Sindhi", "sk_sk": "Slovak", "sl_si": "Slovenian", "sn_zw": "Shona", "so_so": "Somali", "sr_rs": "Serbian", "sv_se": "Swedish", "sw_ke": "Swahili", "ta_in": "Tamil", "te_in": "Telugu", "tg_tj": "Tajik", "th_th": "Thai", "tr_tr": "Turkish", "uk_ua": "Ukrainian", "ur_pk": "Urdu", "uz_uz": "Uzbek", "vi_vn": "Vietnamese", "yo_ng": "Yoruba"}
selection = widgets.Dropdown(
    options=[("Select language", None), ("----------", None)] + sorted([(f"{v} ({k})", k) for k, v in languages.items()]),
    value="es_419",
    description='Language:',
    disabled=False,
)

selection


# segunda parte idioma

lang = selection.value
language = languages[lang]

assert lang is not None, "Please select a language"
print(f"Selected language: {language} ({lang})")

# abre el archivo de audio y lo divide en segmentos
audio_file = AudioSegment.from_file(archivo_audio)
duration = len(audio_file)
segments = range(0, duration, duracion_segmento)

# abre el archivo de salida para escritura
with open(ruta_salida, "w") as archivo_salida:
    for i, start in enumerate(segments):
        # establece el segmento actual
        end = start + duracion_segmento
        segment = audio_file[start:end]

        # transcribe el segmento actual
        opciones_decodificacion = DecodingOptions(
            beam_width=1024, max_alternatives=1, word_score=2.0, valid_word_count_weight=1.85
        )
        resultado_transcripcion: DecodingResult = model.transcribe(segment, opciones_decodificacion)

        # escribe el texto de la transcripción en el archivo de salida
        texto_transcripcion = resultado_transcripcion.text
        marca_tiempo = f"{start/1000:.3f}-{end/1000:.3f}"
        archivo_salida.write(f"{marca_tiempo}:\n")
        archivo_salida.write(f"{texto_transcripcion}\n\n")
