import eyed3
import os
import sys
import re

main_artist = None
main_album = None
rename_directory = True

try :
    for file in os.listdir(sys.argv[1]):
        if file.endswith(".mp3"):
            path = os.path.join(sys.argv[1], file)
            audio = eyed3.load(path)
            artist = audio.tag.artist
            album = audio.tag.album

            title = re.sub(r"[:*?<>|]", "", audio.tag.title)
            title = re.sub(r"[/\\]", "_", title)

            os.rename(path, os.path.join(sys.argv[1], f"{artist} - {title} - {album}.mp3"))

            if main_album is None:
                main_artist = artist
                main_album = album
            elif main_album != album:
                rename_directory = False
            
            if main_artist != artist:
                main_artist = None


except FileNotFoundError:
    print(f"Error: directory {sys.argv[1]} not found", file=sys.stderr)
except NotADirectoryError:
    print(f"Error: filename {sys.argv[1]} given is not a directory", file=sys.stderr)

if rename_directory:
    parent = os.path.abspath(os.path.join(sys.argv[1], os.pardir))
    if main_artist is not None:
        os.rename(sys.argv[1], os.path.join(parent, f"{main_artist} - {main_album}"))
    else:
        os.rename(sys.argv[1], os.path.join(parent, f"Various Artists - {main_album}"))