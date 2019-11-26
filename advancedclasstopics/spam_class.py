class Spam:
    numInstances = 0  # Trace class passed in

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances(cls):
        print("Spam: number of instances: %s %s" % (cls.numInstances, cls))

    printNumInstances = classmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances(cls):  # Override a class method
        print("SUB...", cls)  # But call back to original
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)


class Other(Spam): pass  # Inherit class method verbatim


if __name__ == "__main__":
    x = Sub()
    y = Spam()
    x.printNumInstances()
    Sub.printNumInstances()
