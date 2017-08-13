import os
import pickle
from gi.repository.GdkPixbuf import Pixbuf

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

def getIcon(name, mime = None, size = None):
    d = os.path.join(r, 'icons')
    
    if mime == None:
        mime = 'png'
        
    n = ".".join([name, mime])
    p = os.path.join(d, n)
    
    if size == None:
        i = Pixbuf.new_from_file(p)
    else:
        i = Pixbuf.new_from_file_at_scale(p, size, size, False)
        
    return i
    

def loadPydFile(file):
    loaded = pickle.load(open(file, 'rb'))
    return loaded

def savePydFile(file, data):
    pickle.dump(data, open(file, 'wb'))


def make_short(title, lenght = 26):
    short = ""
    if len(title) > lenght:
        for i in range(lenght):
            try:
                short += title[i]
            except:
                pass
    else:
        short = title

    return short