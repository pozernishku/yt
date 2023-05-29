#!/bin/bash

ffmpeg -hide_banner -f concat -i file_list.txt video_"$(date +%Y%m%d_%H%M%S)".mp4
rm -rf blured_vids
rm file_list.txt
