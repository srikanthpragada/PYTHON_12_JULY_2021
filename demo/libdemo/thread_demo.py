from threading import Thread
import threading

print(threading.current_thread().name)

class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print('Child', n)


pt = PrintThread()
pt.start()

for n in range(1, 11):
    print('Main', n)
