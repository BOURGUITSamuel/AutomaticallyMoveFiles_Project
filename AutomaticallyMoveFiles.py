import os
import glob
import shutil
from os import path

'''Extensions'''
filename = glob.glob("D:/*")
documents = ['.pdf', '.docx', '.doc', '.txt']
media = ['.mp4', '.mp3', '.mkv', '.wav', '.avi']
pictures = ['.jpeg', '.jpg', '.svg', '.png', '.PNG', '.gif', '.psd', ]
setupFiles = ['.exe', '.msi']
compressedFiles = ['.zip']
files = ['.apk', '.ipa']
scripts = ['.sh', '.py', '.bash']

'''Folder Location'''
DocumentsLocation = 'D:/Documents'
PicturesLocation = 'D:/Pictures'
Medialocation = 'D:/Media'
SetupFilesLocation = 'D:/SetupFiles'
CompressedFilesLocation = 'D:/CompressedFiles'
FilesLocation = 'D:/Files'
ScriptsLocation = 'D:/Scripts'


def automovefile():
    for file in filename:
        if os.path.splitext(file)[1] not in documents:
            pass
        else:
            if path.exists(DocumentsLocation):
                shutil.move(file, DocumentsLocation)
            else:
                os.mkdir(DocumentsLocation)
                shutil.move(file, DocumentsLocation)
        if os.path.splitext(file)[1] not in media:
            pass
        else:
            if path.exists(Medialocation):
                shutil.move(file, Medialocation)
            else:
                os.mkdir(Medialocation)
                shutil.move(file, Medialocation)
        if os.path.splitext(file)[1] not in pictures:
            pass
        else:
            if path.exists(PicturesLocation):
                shutil.move(file, PicturesLocation)
            else:
                os.mkdir(PicturesLocation)
                shutil.move(file, PicturesLocation)
        if os.path.splitext(file)[1] not in setupFiles:
            pass
        else:
            if path.exists(SetupFilesLocation):
                shutil.move(file, SetupFilesLocation)
            else:
                os.mkdir(SetupFilesLocation)
                shutil.move(file, SetupFilesLocation)
        if os.path.splitext(file)[1] not in compressedFiles:
            pass
        else:
            if path.exists(CompressedFilesLocation):
                shutil.move(file, CompressedFilesLocation)
            else:
                os.mkdir(CompressedFilesLocation)
                shutil.move(file, CompressedFilesLocation)
        if os.path.splitext(file)[1] not in files:
            pass
        else:
            if path.exists(FilesLocation):
                shutil.move(file, FilesLocation)
            else:
                os.mkdir(FilesLocation)
                shutil.move(file, FilesLocation)
        if os.path.splitext(file)[1] not in scripts:
            pass
        else:
            if path.exists(ScriptsLocation):
                shutil.move(file, ScriptsLocation)
            else:
                os.mkdir(ScriptsLocation)
                shutil.move(file, ScriptsLocation)


automovefile()
