#!/usr/bin/env python2

def zeros(number, padlength):
    """ Pad with zeros."""
    return str(number).zfill(padlength)


def setup_directories(*dirs):
    """ Creates directories if they don't already exist."""
    for directory in dirs:
        if os.path.exists(directory):
            pass    
        else:
            os.makedirs(directory)

def readfile(filename):
    filehandler = open(filename,'r')
    rawtext = filehandler.readlines()
    filehandler.close()
    return rawtext

