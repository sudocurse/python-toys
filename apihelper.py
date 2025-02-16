def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string-- that is, anything with a method list?
    """

    methodList = [method for method in dir(object) if callable(getattr(object, method))]

    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

    # print callable(processFunc)


if __name__ == '__main__':
    # print info.__doc__
    # print info(info)
    # print info("flicker")
    muh = []
    print info(muh)
