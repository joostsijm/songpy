#!/usr/bin/env python3.6

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.easymp4 import EasyMP4
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import FLAC
import os


def returnAudio(path):
    ext = os.path.splitext(path)[1]
    if ext == ".mp3":
        audio = MP3(path, ID3=EasyID3)
    elif ext == ".ogg":
        audio = OggVorbis(path)
    elif ext == ".flac":
        audio = FLAC(path)
    elif ext == ".m4a":
        audio = EasyMP4(path)
    return audio

def validExt():
    return [
        ".mp3",
        ".ogg",
        ".flac",
        ".m4a",
    ]
