#!/usr/bin/env python2.7

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.oggvorbis import OggVorbis 
import os

def returnAudio(path):
    ext = os.path.splitext(path)[1]
    if ext == ".mp3":
        audio = MP3(path, ID3=EasyID3)
    elif ext == ".ogg":
        audio = OggVorbis(path)
    return audio
