#!/bin/bash

# TODO: Move this functionality into Python
url="https://www.reddit.com/r/TikTokCringe/hot.json?limit=2"
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
json_response=$(curl -s -H "User-Agent: $user_agent" "$url")
video_urls=$(python -m find_videos --json "$json_response")
youtube-dl $(echo "$video_urls")

mkdir blured_vids
for f in *.mp4;
do
  # TODO: Try to do it using multiprocessing
  ffmpeg -hide_banner -i "$f" -lavfi '[0:v]scale=ih*16/9:-1,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,crop=h=iw*9/16' -vb 800K blured_vids/"$f";
done

rm *.mp4
for f in blured_vids/*.mp4;
do
  echo "file $f" >> file_list.txt;
done
