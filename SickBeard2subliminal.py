#!/usr/bin/env python
"""
https://github.com/Tyrix/SickBeard2subliminal

SB2subliminal processes the downloaded TV Episode and automatically gets a
matching subtitle for it 

"""
import sys
import os
import logging
import shutil
import subliminal

#===========
#  CONFIG
#===========
LOGFILE = 'SickBeard2subliminal.log'
LANGUAGES = ['en', 'de']
SERVICES = ['addic7ed', 'bierdopje', 'opensubtitles']
CACHE_DIR = "C:\\change\\your\\path_pls\\"
#===========


logging.basicConfig(filename=LOGFILE, format="%(asctime)s -\
                    %(levelname)s:%(message)s", level=logging.DEBUG)

fileName = os.path.basename(sys.argv[2])
filePath = os.path.split(sys.argv[1])[0] + "\\" + fileName

#processed Filepath
proc_filePath = sys.argv[1]
#processed Filepath replaced extension with srt
proc_filePath_srt = proc_filePath[:len(proc_filePath)-3] + "srt"

logging.info("got filename: " + filePath)
logging.info("Processed srt filepath: " + proc_filePath_srt)
logging.info("initiating subliminal")
logging.info(subliminal.download_subtitles(filePath, LANGUAGES, SERVICES, cache_dir=CACHE_DIR))

#replace video filename extension with srt, srt file is in SickBeard root folder, move it to the processed TV folder with processed filename
fileName_srt = fileName[:-3] + "srt"
logging.info("Moving srt file: " + fileName_srt + " to folder: " + proc_filePath_srt)
shutil.move(fileName_srt, proc_filePath_srt)

