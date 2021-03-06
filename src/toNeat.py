#!/usr/bin/env python3.6

import re
import sys

# Maps a string such as 'The Beatles' to 'the_beatles'.
def toNeat(s, args):
    # Put spaces between and remove blank characters.
    blankCharsPad = r"()\[\],.\\\?\#/\!\$\:\;"
    blankCharsNoPad = r"'\""
    s = re.sub(r"([" + blankCharsPad + r"])([^ ])", "\\1 \\2", s)
    s = re.sub("[" + blankCharsPad + blankCharsNoPad + "]", "", s)

    # Replace spaces with a single dash.
    s = re.sub(r"[ \*\_]+", "_", s)
    s = re.sub("-+", "-", s)
    s = re.sub("^-*", "", s)
    s = re.sub("-*$", "", s)

    # Replace fractions
    s = s.replace("½", "1of2")
    s = s.replace("⅓", "1of3")
    s = s.replace("⅔", "2of3")
    s = s.replace("¼", "1of4")
    s = s.replace("¾", "3of4")

    s = s.title().replace("&", "and")

    # Ensure the string is only alphanumeric with '-', '+', and '+'.
    if not args.capital:
        s = s.lower()
    search = re.search("[^0-9a-zA-Z\-\+\_]", s)
    if search:
        print("Warning : Unrecognized character in '" + s + "'")
        with open("error.log", 'w') as log:
            log.write(s + "\n");
    return s
