# In Python 3.X (and 2.6+ for compatibility)

if __name__ == "__main__":
    def func(a, b, c, e=True, f=None):  # Args: three required, two defaults
        x = 1  # Plus two more local variables
        y = 2


    code = func.__code__  # Code object of function object
    print(code.co_nlocals)
    print(code.co_varnames)  # All local variable names
    print(code.co_varnames[:code.co_argcount])  # <== First N locals are expected args
