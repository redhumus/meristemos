#!/bin/bash

# Variables
ACOUSTID_API_KEY="your_acoustid_api_key_here"
MUSICBRAINZ_API_ENDPOINT="https://musicbrainz.org/ws/2"
MUSICBRAINZ_LOOKUP_SCRIPT="./musicbrainzngslookup.py"
MUSICBRAINZ_USER_AGENT="my_application/1.0"
OUTPUT_FILE="metadata.csv"

# Función para procesar un archivo
process_file() {
  filename=$1
  echo "Processing file: $filename"

  # Obtener la huella digital del archivo
  fingerprint=$(fpcalc "$filename" | grep FINGERPRINT= | cut -d "=" -f 2)

  # Si el archivo es un archivo MIDI, mostrar un mensaje y continuar con el siguiente archivo
  file_type=$(file "$filename")
  if [[ "$file_type" == *"MIDI"* ]]; then
    echo "File is a MIDI file, skipping..."
    return
  fi

  # Obtener información de AcoustID
  echo "Querying AcoustID..."
  acoustid_result=$(curl -s "https://api.acoustid.org/v2/lookup?client=myapp&meta=recordings+releasegroups+compress&duration=$(soxi -D "$filename")&fingerprint=$fingerprint&api_key=$ACOUSTID_API_KEY")
  recording_id=$(echo "$acoustid_result" | jq -r '.results[0].recordings[0].id')
  if [[ "$recording_id" == "null" ]]; then
    echo "No AcoustID match found."
    recording_title=""
    recording_artist=""
    recording_release=""
    recording_year=""
  else
    recording_title=$(echo "$acoustid_result" | jq -r '.results[0].recordings[0].title')
    recording_artist=$(echo "$acoustid_result" | jq -r '.results[0].recordings[0]["artist-credit"][0].artist.name')
    recording_release=$(echo "$acoustid_result" | jq -r '.results[0].releasegroups[0].title')
    recording_year=$(echo "$acoustid_result" | jq -r '.results[0].releasegroups[0].first-release-date')
    echo "AcoustID match found: $recording_artist - $recording_title ($recording_release, $recording_year)"
  fi

  # Obtener información de MusicBrainz
  echo "Querying MusicBrainz..."
  musicbrainz_result=$(python3 "$MUSICBRAINZ_LOOKUP_SCRIPT" --user-agent="$MUSICBRAINZ_USER_AGENT" --endpoint="$MUSICBRAINZ_API_ENDPOINT" recording "$recording_id")
  recording_mb_id=$(echo "$musicbrainz_result" | jq -r '.id')
  recording_mb_url=$(echo "$musicbrainz_result" | jq -r '.url.resource')
  echo "MusicBrainz match found: $recording_mb_id ($recording_mb_url)"

  # Escribir metadatos en archivo CSV
  echo "Writing metadata to CSV file: $OUTPUT_FILE"
  echo "$filename,$recording_artist,$recording_title,$recording_release,$recording_year,$recording_mb_id,$recording_mb_url" >> "$OUTPUT_FILE"
}

# Procesar todos los archivos en la carpeta actual
for filename in *; do
  if [[ -f "$filename" ]]; then
    process_file "$filename"
  fi
done

echo "Done."
