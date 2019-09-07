This is a very small Linux utility aimed on a simple task.
If you have a lot of imported music structured into directories
...
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
...

The script scans the children of the rootDirectory recursively for taggable music files (mp3/wma/FLAC/...). 
* Directories at tje first level are used for Artist tag (Author 1, Author 2)
* Directories on the last level are used as Album Name, for example Yet another song.ogg will be tagged with { Artist: Author 1, Album: Album 3}



## Usage
Simply run the following command in the terminal and let the magic happen.
```shell
./id3-auto-album-author --path <path-to-root-directory>
```