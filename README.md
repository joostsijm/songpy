# SongPy
Music organizer written in Python 3.

## About
Intended as command line program to be able to organize your music library.
Still minimal suport for file types but might improve in the future.

Currentl supported file types: 
* .MP3
* .OGG

## Quick Start
To transfer your music libary to a new location and organize the songs you use the following:
```
python music-organizer.py <path> <destination>
```
Make sure your library only exits of folders and files of the supported file types.
Would you like more options of organizing your library read the synopsis for a more details

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

## Contributing
Feel free to contribute to this repository by means of a pull-request.

## License
This program _SongPy_ is published under the term of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
