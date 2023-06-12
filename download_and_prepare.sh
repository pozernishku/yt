#!/bin/bash

# TODO: Move this functionality into pure Python
url="https://www.reddit.com/r/TikTokCringe/hot.json?limit=2"
python -m download --url "$url"

mkdir blured_vids
for f in *.mp4;
do
  # TODO: Try to do it using multiprocessing (looks like it's already multiprocessing)
  # TODO: Update the command below. It should work on video without audio stream as well
  scale="ih*16/9:-1"
  boxblur="luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg]"
  overlay="(W-w)/2:(H-h)/2"
  crop="h='if(gte(iw*9/16,ih),ih-1,iw*9/16)'"
  filter="[0:v]scale=$scale,boxblur=$boxblur;[bg][0:v]overlay=$overlay,crop=$crop"
  ffmpeg -hide_banner -i "$f" -filter_complex "$filter" -b:v 1M blured_vids/"$f";
done

rm *.mp4
for f in blured_vids/*.mp4;
do
  echo "file $f" >> file_list.txt;
done
