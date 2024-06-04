# Collection Manager
A short Python script I wrote to help manage my growing `.mp3` music collection by renaming files according to a consistent format. As my collection grows, I may choose to add other Python scripts to this repository that help manage the collection.

### Usage
Install the required packages by running the following code:
```
python -m pip install -r requirements.txt
```

At the moment, there's a single Python script titled `rename.py` that renames `.mp3` files using their ID3 tags. Files are renamed to an `artist - song title - album.mp3` format. If the entire directory contains songs from the same album, then the selected directory is also renamed according to the following rules:  
* If the directory contains `.mp3` files with the same artist tag, then the directory is renamed to an `artist - album` format
* If the directory contains `.mp3` files with different artist tags, then the directory is renamed to an `Various Artists - album` format
  
### License
The BSD 3-Clause License (BSD-3) 2024 - [Kedar Panchal](https://github.com/KedarPanchal). Please look at the
[LICENSE](LICENSE) for further information.