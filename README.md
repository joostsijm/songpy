# SongPy
Music organizer written in Python.

## About
**SongPy** is intended as command line program to be able to organize your music library. It still has minimal suport for filetypes.

Currently supported filetypes: .MP3, .OGG

## Quick Start
To transver your music libary to a new location and organize the songs you use the following:
```
python2 music-organizer.py <path> <destination>
```
Make sure your libary only exits of folders and files of the supported filetypes. If you want to delete enrecognized file extensions run the `-e` flag.   
For a rundown of the availble flags read the synopsis. 

## Synopsis
	usage: music-organizer.py [-h] [-d] [-e] [-a] [-A] [-n] [-C] path dest

	Organizes a music collection using tag information. The directory format is
	that the music collection consists of artist subdirectories, and there are 2
	modes to operate on the entire collection or a single artist.

	positional arguments:
	  path                  The path to your music folder.
	  dest                  Path to the destination of your libary.

	optional arguments:
	  -h, --help            show this help message and exit
	  -d, --delete-conflicts
	                        If an artist has duplicate tracks with the same name,
	                        delete them. Note this might always be best in case an
	                        artist has multiple versions. To keep multiple
	                        versions, fix the tag information.
	  -e, --delete-unrecognized
	                        Delete unregcognized extensions
	  -a, --album           Adds album folder inside the artist folder to sort out
	                        albums.
	  -A, --artist          Place the songs or albums in a artist folder.
	  -n, --number          Adds number in front of sorted songs
	  -C, --capital         Makes the first letter of a song capital.

## License
This program _SongPy_ is published under the term of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
