#!/usr/bin/env python3

import sys
import os
import argparse
import mutagen

TAGGABLE_EXTENSIONS = {
    ".mp3",
    ".wma",
    ".flac"
}

def main():
    
    args = parse_args()
    path = args.path
    if not check_path(path):
        print(f"Path {args.path} not valid. It either does not exist or it is not a directory.")
        exit(1)
        
    [visitChild(c, path, "") for c in os.listdir(path)]


def parse_args():
    parser = argparse.ArgumentParser(description='Root directory')
    parser.add_argument("--path", required=True)
    return parser.parse_args()

def check_path(filePath):
    return os.path.exists(filePath) and os.path.isdir(filePath)


def visitChild(childName, parentPath, parentArtist):
    artist = parentArtist or childName
    albumName = os.path.basename(parentPath)
    childPath =  os.path.join(parentPath, childName)   

    if os.path.isdir(childPath):
        [visitChild(c, childPath, artist) for c in os.listdir(childPath)]
    elif is_taggable(childPath):
        add_tags(childPath, artist, albumName)

def is_taggable(file):
    extension = os.path.splitext(file)
    return extension[-1] in TAGGABLE_EXTENSIONS

def add_tags(filePath, artist, album):
    #print(f"{filePath}: au: {artist}, al:{album}")
    mediafile = mutagen.File(filePath, easy=True)
    mediafile['album'] = album
    mediafile['albumartist'] = artist
    mediafile['artist'] = artist
    print(f"{mediafile}")

if __name__ == "__main__":
    main()
