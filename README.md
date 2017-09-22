# SongPy
Music organizer written in Python 3.

## About
Intended as command line program to be able to organize your music library.
Still, minimal support for file types but might improve in the future.

Currently supported file types:
* .MP3
* .OGG

## Quick Start
To transfer your music library to a new location and organize the songs you use the following:
```
./music-organizer.py <path> <destination>
```
Make sure your library only exits of folders and files of the supported file types.
Would you like more options of organizing your library read the synopsis for a more details

## Synopsis
```
usage: music-organizer.py [-h] [-d] [-e] [-a] [-A] [-n] [-C] path dest

Organizes a music collection using tag information. Some features described in
the synopsis might not work as expect so be cautious and backup your
collection first.

positional arguments:
  path                  The path to your music folder
  dest                  Path to the destination of your library

optional arguments:
  -h, --help            show this help message and exit
  -d, --delete-conflicts
                        Delete conflicting filenames in the same directory
  -e, --delete-unrecognized
                        Delete unrecognized extensions
  -a, --album           Adds album folder inside the artist folder
  -A, --artist          Place the songs or albums in an artist folder
  -n, --number          Adds number in front of sorted songs
  -C, --capital         Make the first letter of words capital
```

## Contributing
Feel free to contribute to this repository by means of a pull-request.

## License
This program _SongPy_ is published under the term of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
