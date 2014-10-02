
def make_short(self, title, lenght = 26):
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