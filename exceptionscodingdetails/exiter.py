import sys


def bye():
    sys.exit(40)  # Crucial error: abort now!


if __name__ == "__main__":
    try:
        bye()
    except SystemExit as e:
        print('got it')  # Oops--we ignored the exit
        print('continuing...')
