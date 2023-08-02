from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os
import time

# Get the desired video title
title = str("vid1")

# Open the video and audio
video_path = "C:\\code\\content\\videos\\" + str(time.strftime("%Y-%m-%d")) + ".mp4"
music_path = "C:\\code\\content\\musics\\music.mp3"
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(music_path)
audio_final = audio_clip.audio_loop( audio_clip, duration=video_clip.duration)

# Concatenate the video clip with the audio clip
final_clip = video_clip.set_audio(audio_final)

# Export the final video with audio
final_clip.write_videofile("C:\\code\\content\\videos\\" + str(time.strftime("%Y-%m-%d")) + ".mp4")