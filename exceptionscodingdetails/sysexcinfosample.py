import sys

if __name__ == "__main__":
    try:
        raise ValueError("MESSAGE")
    except(ValueError, SyntaxError) as error:
        print(f'caught: {error}, args: {error.args}')
        exc_info = sys.exc_info()
        print(exc_info)
