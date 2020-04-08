import asyncio
import time


def sequential_count_down(name, delay, start):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        time.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1


def run_sequential():
    start = time.perf_counter()

    sequential_count_down('A', 1, start)
    sequential_count_down('B', 0.8, start)
    sequential_count_down('C', 0.5, start)

    print('-' * 40)
    print('Done.')


async def count_down(name, delay, start):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)
        # time.sleep(delay) reverts the coroutine to sequential task

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1


def run_async():
    loop = asyncio.get_event_loop()
    start = time.perf_counter()
    tasks = [
        loop.create_task(count_down('A', 1, start)),
        loop.create_task(count_down('B', 0.8, start)),
        loop.create_task(count_down('C', 0.5, start))]

    loop.run_until_complete(asyncio.wait(tasks))

    print('-' * 40)
    print('Done.')


if __name__ == "__main__":
    run_async()
