# Alartag - Album Artist Tagger

This is a very small utility aimed on a simple task.
If you have a lot of imported music structured into directories
```
  -rootDirectory
    |- Author 1 -
    |  |- Song 1.mp3
    |  |- Song 2.mp3
    |  |- Album 1
    |  |  |- OtherSong 1.mp3
    |  |  |- OtherSong 2.mp3
    |  |  |- ...
    |  |- Subdirectory
    |  |  |- Album 2
    |  |  |  |- Some SuperSong.wma
    |  |  |- Album 3
    |  |  |  |- Yet another song.ogg
    |- Some Anonymous Song.mp3
    |- Author 2
        | ...
```

The script scans the children of the rootDirectory recursively for taggable music files (mp3/wma/FLAC/...). 
* Directories at the first level are used for Artist and Album Artist tag (Author 1, Author 2)
* Directories on the last level are used as Album Name, for example Yet another song.ogg will be tagged with { Artist: Author 1, Album: Album 3}
* Files of unsupported media type are ignored regardless of their file extension.

This script uses [Mutagen](https://github.com/quodlibet/mutagen) to do the tagging magic. Kudos to all the contributors that made such awesome library.
  
## Prerequisites
* Python 3.5 and higher
* Internet connection for downloading the Mutagen from PyPi. Or - if you would like to tinker around with offline installation, feel free to do so.

## Installation
Clone this repository. In terminal, cd to the root directory of the project and run
```
pip3 install .
```

## Usage
After installation, simply run the following command in the terminal and let the magic happen.
```
alartag -path <path-to-root-directory>
```

To display help about the application usage, run
```
alartag -h
```
## License
GNU-GPLv2