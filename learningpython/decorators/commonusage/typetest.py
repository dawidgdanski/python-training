def typetest(**argchecks):
    def onDecorator(func):
        code = func.__code__  # Code object of function object
        allargs = code.co_varnames[:code.co_argcount]  # <== First N locals are expected args

        def onCall(*pargs, **kargs):
            positionals = list(allargs)[:len(pargs)]
            for (argname, type) in argchecks.items():
                if argname in kargs:
                    if not isinstance(kargs[argname], type):
                        raise TypeError(
                            f'Forbidden type for argument {argname}. '
                            f'Expected: {type.__name__}, actual: {kargs[argname].__class__.__name__}')
                elif argname in positionals:
                    position = positionals.index(argname)
                    if not isinstance(pargs[position], type):
                        raise TypeError(
                            f'Forbidden type for argument {argname}. '
                            f'Expected: {type.__name__}, actual: {pargs[position].__class__.__name__}')
                else:
                    # Assume not passed: default
                    return func(*pargs, **kargs)

        return onCall

    return onDecorator


@typetest(a=int, c=float)
def func(a, b, c, d):  # func = typetest(...)(func)
    print(a, b, c, d)


func(1, 2, 3.0, 4)  # OK
func('spam', 2, 99, 4)  # Triggers exception correctly
