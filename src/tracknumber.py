#!/usr/bin/env python3.6

import audioFunction
import os
import re


def fixTracknumber(fname):
    audio = audioFunction.returnAudio(fname)
    try:
        tracknumber = re.findall(r'\d+', os.path.basename(fname).split(' ')[0])[0]
    except:
        tracknumber = "0"
    audio['tracknumber'] = tracknumber.zfill(2)
    return formatNumber(audio)

def formatNumber(audio):
    print(audio)
    if 'tracknumber' in audio:
        if "/" in audio['tracknumber'][0]:
            audio['tracknumber'] = audio['tracknumber'][0].split('/')[0]
        audio.save()
    else:
        fixTracknumber(audio)
    print(audio)
    return audio

def getTracknumber(audio):
    return str(audio['tracknumber'][0])
