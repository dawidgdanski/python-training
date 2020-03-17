import threading
from threading import activeCount, currentThread


def main():
    print(f"Active htreads count: {activeCount()}")

    print(f"Current thread: {currentThread()}")

    print("Enumerating active threads:")

    for thread in threading.enumerate():
        print(thread)


if __name__ == "__main__":
    main()
