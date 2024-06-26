# Collection Manager
A short Python script I wrote to help manage my growing digital music collection by renaming files according to a consistent format. As my collection grows, I may choose to add other Python scripts to this repository that help manage the collection.

### Usage
Install the required packages by running the following code:
```
python -m pip install -r requirements.txt
```

At the moment, there's a single Python script titled `rename.py` that renames any audio file in the [supported files](#supported-files) section of this README using their ID3 tags. Files are renamed to an `artist - song title - album` format. If the entire directory contains songs from the same album, then the selected directory is also renamed according to the following rules:  
* If the directory contains audio files with the same artist tag, then the directory is renamed to an `artist - album` format
* If the directory contains audio files with different artist tags, then the directory is renamed to an `Various Artists - album` format
  
### Supported Files
Below is a list of the filetypes supported by the scripts at the moment:
* `.mp1`
* `.mp2`
* `.mp3`
* `.oga`
* `.ogg`
* `.opus`
* `.spx`
* `.wav`
* `.flac`
* `.wma`
* `.m4b`
* `.m4a`
* `.m4r`
* `.m4v`
* `.mp4`
* `.aax`
* `.aaxc`
* `.aiff`
* `.aifc`
* `.aif`
* `.afc`
### License
The BSD 3-Clause License (BSD-3) 2024 - [Kedar Panchal](https://github.com/KedarPanchal). Please look at the
[LICENSE](LICENSE) for further information.