# coding=utf-8
__author__ = 'ankeet'

import operator


def main():
    """

    :rtype
     ≤: None
    """
    a = {'a': 10001, 'b': 2, 'c': 555}
    print sorted(a.items(), key=operator.itemgetter(1))

    return None


def formatting_strings():
    k = "uid"
    v = "sa"

    print "%s=%s" % (k, v)
    print "{0}={1}".format(k, v)

    print "Today's stock price: %f" % 50.4625
    print "change since yesterday: %+.2f" % 1.5


if __name__ == '__main__':
    formatting_strings()