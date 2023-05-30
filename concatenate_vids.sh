#!/bin/bash

# FIXME: Muted output. Investigate and fix the case when there is a video without sound
ffmpeg -hide_banner -f concat -i file_list.txt -c copy video_"$(date +%Y%m%d_%H%M%S)".mp4
rm -rf blured_vids
rm file_list.txt
