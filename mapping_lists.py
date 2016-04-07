
'''
def main(params):
    li = [1, 9, 8, 4]
    print [elem * 2 for elem in li]

    print li
    li = ["%s=%s" % (k, v) for k, v in params.items()]
    print sorted(li, reverse=True)

if __name__ == '__main__':
    tmpdict = {'a': 'woof', 'b': 'meow'}

    main(tmpdict)
'''

params = {"server":"facebook.com", "database":"master", "uid":"sa", "pwd":"secret"}
print params.keys()

print params.values()

print params.items()


def jump(x, y):
    if x % 4 == 0:
        return x + 100000
    else:
        return x

seq = range(12)

print map(jump, seq, seq)


def how_many(a, b):
    return a + b

print reduce(how_many, range(1, 5))


def even(x):
    return x % 2 == 0

print filter(even, range(2, 25))