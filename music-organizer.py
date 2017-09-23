#!/usr/bin/env python3.6

"""
This script (music-organizer.py) organizes my music collection for
iTunes and [mpv](http://mpv.io) using tag information.
The directory structure is `<artist>/<track>`, where `<artist>` and `<track>`
are lower case strings separated by dashes.
"""

import argparse
import glob
import os
import re
import shutil
import sys
import src.toNeat
import src.tracknumber
import audioFunction

parser = argparse.ArgumentParser(
        description="""Organizes a music collection using tag information.
        Some features described in the synopsis might not work as expect
        so be cautious and backup your collection first.""")

parser.add_argument("path",
                    help="The path to your music folder")

parser.add_argument("dest",
                    default=".",
                    help="Path to the destination of your library")

parser.add_argument('-d', '--delete-conflicts', action='store_true',
                    dest='delete_conflicts',
                    help="Delete conflicting filenames in the same directory")

parser.add_argument('-e', '--delete-unrecognized', action='store_true',
                    dest='delete_unrecognized',
                    help="Delete unrecognized extensions")

parser.add_argument('-a', '--album', action='store_true',
                    dest='album',
                    help="Adds album folder inside the artist folder")

parser.add_argument('-A', '--artist', action='store_true',
                    dest='artist',
                    help="Place the songs or albums in an artist folder")

parser.add_argument('-n', '--number', action='store_true',
                    dest='number',
                    help="Adds number in front of sorted songs")

parser.add_argument('-C', '--capital', action='store_true',
                    dest='capital',
                    help="Make the first letter of words capital")

args = parser.parse_args()


def artist(path):
    print("Organizing artist")
    delete_dirs = []
    for dirname, dirnames, filenames in os.walk(path + "/."):
        # Move all the files to the root directory.
        for filename in filenames:
            fullPath = os.path.join(dirname, filename)
            # formating song
            returned = song(fullPath)
            if returned is "succes":
                print("succesful formated")
            elif returned is "delete":
                print("deleted remaining files in folder")
            elif returned is "unrecognized":
                print("Unrecognized files left")
            elif returned is "error":
                print("error with file")
            else:
                returnedlist = returned.split('/')
                for extdir in returnedlist:
                    if extdir in delete_dirs:
                        delete_dirs.remove(extdir)

        # Add subdirectories to a list
        for subdirname in dirnames:
            delete_dirs.append(subdirname)

    # deletes subdirectories
    for d in delete_dirs:
        shutil.rmtree(os.path.join(".", d), ignore_errors=True)


def song(filename):
    # if filename[0] == '.':
    #    print("Ignoring dotfile: '{}'".format(filename))
    #    return
    ext = os.path.splitext(filename)[1]
    if ext in (".mp3", ".ogg", ".flac"):
        print("Organizing song '" + filename + "'.")
        try:
            audio = audioFunction.returnAudio(filename)
            artist = str(audio['artist'][0])
            title = str(audio['title'][0])
            if args.album:
                album = str(audio['album'][0])
            if args.number:
                try:
                    neatTracknumber = src.tracknumber.getTracknumber(filename)
                except:
                    neatTracknumber = "0"
            print("    artist: " + artist)
            print("    title: " + title)
            if args.album:
                print("    album: " + album)
        except:
            print("Error: file cannot be read.")
            errorpath = args.dest + "/unknown"
            if not os.path.isdir(errorpath):
                os.mkdir(errorpath)
            errorfile = errorpath + "/" + filename.split("/")[-1]
            print(errorfile)
            os.rename(filename, errorfile)
            return "error"

        neatArtist = src.toNeat.toNeat(artist, args)
        if args.number:
            neatTitle = neatTracknumber + "." + src.toNeat.toNeat(title, args)
        else:
            neatTitle = src.toNeat.toNeat(title, args)

        print("    neatArtist: " + neatArtist)
        print("    neatTitle: " + neatTitle)
        newpath = args.dest
        if args.artist:
            newpath = newpath + "/" + neatArtist
            if not os.path.isdir(newpath):
                os.mkdir(newpath)
        if args.album:
            neatAlbum = src.toNeat.toNeat(album, args)
            print("    neatAlbum: " + neatAlbum)
            newpath = newpath + "/" + neatAlbum
            if not os.path.isdir(newpath):
                os.mkdir(newpath)
            newFullPath = os.path.join(newpath, neatTitle + ext)
        else:
            newFullPath = os.path.join(newpath, neatTitle + ext)

        if newFullPath != filename:
            if os.path.isfile(newFullPath):
                if args.delete_conflicts:
                    os.remove(filename)
                    print("File exists: '" + newFullPath + "'")
                    print("Deleted: '" + filename + "'")
                else:
                    print("Error: File exists: '" + newFullPath + "'")
                    return os.path.split(newFullPath)[0]

            else:
                os.rename(filename, newFullPath)
                return "succes"

    else:
        print("Error: Unrecognized music file extension " + filename + ".")
        return "unrecognized"


def collection(path):
    path = path.replace('[', '[[]')
    for f in glob.glob(path + '/*'):
        if os.path.isdir(f):
            if args.artist:
                artist(f)
            else:
                collection(f)

        elif os.path.isfile(f):
            song(f)

if not os.path.isdir(args.dest):
    os.mkdir(args.dest)

collection(args.path)
print("\nComplete!")

