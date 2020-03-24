from threading import Lock

my_lock = Lock()


def get_data_from_file_v2(filename):
    with my_lock, open(filename, 'r') as f:
        data.append(f.read())
        # equivalent to with ...
        #                   with ...


data = []

try:
    get_data_from_file_v2('output2/sample0.txt')
except:
    print('Encountered an exception...')
my_lock.acquire()
print('Lock acquired.')
