import pickle, crowbar

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