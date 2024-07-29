import whisper
import datetime
import os
import time


#Aplicación que pide el nombre de carpeta y devuelve una tarea de whisper sobre los archivos dentro de ella avistando via correo la finalización de cada tarea

print('|>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<|\n'
'|------------------------------------------|\n'
'|*********Este es un desarrollo de*********|\n'
'|**********La Mica Prieta Software*********|\n'
'|     COPYLEFT 2022 - Licencia GPL V.3     |\n'
'|------------------------------------------|\n'
'|>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<|\n')


#Inicia Loop Digitar nombre de carpeta, listar o salir

while True:
    dir = input('Ingresa nombre de directorio o escribe "Salir"')
    dir_existe = os.path.exists(dir)
    dir_existe is False

    if dir == 'Salir': quit()

    elif dir_existe is True:
        break
#Este try parece no funcionar
    try:
        os.listdir(dir)

    except:
        print('Directorio no existe')
        continue

# Fin Loop


print('Hecho!!!')

dir_base = os.path.dirname(__file__)
print('Estás en el directorio:'+ str(dir_base))
dir_trabajo = os.path.join(dir_base,dir)
print('El dir ingresado está en:'+ str(dir_trabajo))
dir_analizar = os.listdir(dir_trabajo)
print(dir_analizar)



# crea punto inicio para medir tiempo de ejecución
inicio = time.time()


# crea variable fecha
fecha = datetime.datetime.now()


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


# ///////////////////////////////
#Inicia proceso por archivo
#////////////////////////////

for archivo in dir_analizar:

    #crear archivo de texto
    f = open('./' + str(dir) + '/' + archivo + '.txt','a')
    print(f)
    f.write('Inicio de proceso')
    print('Inicio de proceso')
    f.write(str(fecha))


#escribir archivo

    result = model.transcribe('./' + str(dir) + "/" + str(archivo))
    f.write('\n' + '<<<<<<<<<<<<<<<<<<<Inicio transcripción><<<<<>>>>>>>>>>>>'+'\n')
    f.write(result["text"])
    f.write('\n' + '<<<<<<<<<<<<<<<<<<<fin transcripcion>>>>>>>>>>>>>>>>>>>>>')
    f.write('Fin de proceso')

    # fin de  medición tiempo ejecución
    fin = time.time()
    f.write(str(fin-inicio))

    f.close()
