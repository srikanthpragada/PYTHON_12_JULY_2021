from threading import Thread
import threading


def print_numbers():
    for n in range(1, 11):
        print('Child', n)


pt = Thread(target=print_numbers)
pt.start()

for n in range(1, 11):
    print('Main', n)
