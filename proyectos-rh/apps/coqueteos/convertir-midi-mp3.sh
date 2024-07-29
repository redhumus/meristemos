for file in *.mid
do
  ffmpeg -i "$file" -acodec libmp3lame -q:a 2 "${file%.mid}.mp3"
done
