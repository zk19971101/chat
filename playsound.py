import pygame
import os
import ffmpeg
from ffpyplayer.player import MediaPlayer
# from playsound import playsound


def play(audio_path):
    player = MediaPlayer(audio_path)
    while True:
        audio_frame, val = player.get_frame()
        print("frame:", type(audio_frame))
        print("val", type(val))


if __name__ == '__main__':
    from pydub import AudioSegment

    from pydub.playback import play

    audio_path = "./tempt.wav"
    os.system(f"ffmpeg -i {audio_path} t.wav")
    song = AudioSegment.from_wav("t.wav")
    play(song)


