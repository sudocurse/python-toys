import apihelper


def trpe():
    print type(1)
    li = []
    print type(li)
    print type(type(li))
    print apihelper.info(type(li), spacing=15)


def strgg():
    print str(1)
    horsemen = ['war', 'pests', 'famine']
    print horsemen

    horsemen.append('jason newsted')

    print "searchin %%%" + str(horsemen) + "%%%% seek and destroy"

def no_underscores(s):

    if s.startswith("__"):
        return False
    return True


def dur():
    li = []
    return dir(li)

if __name__ == '__main__':
    # trpe()
    # strgg()
    print filter(no_underscores, dur())

    print callable(strgg)