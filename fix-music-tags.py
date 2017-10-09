#!/usr/bin/env python3.6

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2015.12.30'

"""
This script (fix-music-tags.py) mass-removes unwanted music tags.
"""

import os
import argparse
import glob
import audioFunction
import src.tracknumber


def fixTags(fname, keep):
    audio = audioFunction.returnAudio(fname)
    delKeys = []
    for k, v in audio.items():
        if k not in keep:
            delKeys.append(k)

    for k in delKeys:
        del audio[k]
    audio.save()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('directory',
            help='Directory with music files to fix.')

    parser.add_argument('-k',
            '--keep',
            default=['title', 'artist', 'album', 'genre'],
            type=str,
            nargs='+',
            metavar='TAG',
            help="Tags to keep. Default: title, artist, album, genre"
            )

    parser.add_argument('-n',
            '--fixnumber',
            action='store_true',
            help="Try to fix song number."
            )

    args = parser.parse_args()

    types = ('*.mp3', '*.ogg,', '*.flac')
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob("{}/*{}".format(args.directory, files)))
        for fname in files_grabbed:
            print("Fixing tags for " + fname)
            fixTags(fname, args.keep)
            if args.fixnumber:
                src.tracknumber.formatNumber(fname)
