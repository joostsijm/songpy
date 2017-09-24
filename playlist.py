#!/usr/bin/env python3.6

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2015.04.09'

"""
This script (music-autoplaylists.py) automatically creates
M3U playlists from the genre ID3 tags of songs in a directory.
"""

import argparse
import os
import re
import shutil
import sys
from collections import defaultdict

import audioFunction
import src.toNeat


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
            help="The path to your music directory")
    parser.add_argument("dest",
            default="./playlists",
            help="Path to destination")
    parser.add_argument("-a","--album",
            action="store_true",
            help="Album mode")
    parser.add_argument("-g","--genre",
            action="store_true",
            help="Genre mode")
    parser.add_argument("-C","--capital",
            action="store_true",
            help="Changes names to capital")
    args = parser.parse_args()

    titleList = defaultdict(list)

    for dpath, dnames, fnames in os.walk(args.path):
        if '.git' in dpath:
            continue
        for fname in fnames:
            if os.path.splitext(fname)[1] != '.mp3':
                continue
            filePath = os.path.abspath(os.path.join(dpath, fname))
            audio = audioFunction.returnAudio(filePath)
            if args.genre:
                if 'genre' in audio:
                    assert(len(audio['genre']) == 1)
                    title = src.toNeat.toNeat(str(audio['genre'][0]), args)
                else:
                    title = 'Unknown'

                titleList[title].append(filePath)
            elif args.album:
                if 'artist' in audio or 'album' in audio:
                    if 'artist' in audio :
                        assert(len(audio['artist']) == 1)
                        title = src.toNeat.toNeat(audio["artist"][0], args)
                    if 'album' in audio:
                        assert(len(audio['album']) == 1)
                        title += "-" + src.toNeat.toNeat(audio["album"][0], args)
                else:
                    title = 'Unknown'

                titleList[title].append(filePath)

    if os.path.exists(args.dest):
        shutil.rmtree(args.dest)
    os.makedirs(args.dest)

    for item, songs in titleList.items():
        filePath = os.path.join(args.dest, item + '.m3u')
        print("Creating playlist: " + filePath)
        with open(filePath, 'w') as f:
            f.write("#EXTM3U\n")
            f.write("\n".join(sorted(songs)) + "\n")

if __name__ == '__main__':
    main()
