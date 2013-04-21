#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import codecs

sourceFormats = ['ascii', 'iso-8859-1']
targetFormat = 'utf-8'
outputDir = 'converted'

def convertFile(fileName):
    print("Converting '" + fileName + "'...")
    for format in sourceFormats:
        try:
            with codecs.open(fileName, 'rU', format) as sourceFile:
                writeConversion(sourceFile)
                print('Done formating with:.%s'% format)
                return
        except UnicodeDecodeError:
            pass

    print("Error: failed to convert '" + fileName + "'.")


def writeConversion(file):
    path = os.path.join(outputDir,file.name)
    path_dir = os.path.dirname(path)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)

    with codecs.open(outputDir + '/' + file.name, 'w', targetFormat) as targetFile:
        for line in file:
            targetFile.write(line)

def convert_all_files_in_dir(dirpath):
    for directory, subdirectories, files in os.walk(dirpath):
        for file in files:
            convertFile(os.path.join(directory, file))

if __name__ == '__main__':
    arg1 = sys.argv[1]
    convert_all_files_in_dir(arg1)
