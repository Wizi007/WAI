import os

def start(app):
    try:
        os.startfile(app)
        return('')
    except:
        return('The path is either wrong or the file does not exist')