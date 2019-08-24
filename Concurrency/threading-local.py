import threading

mydata = threading.local()


class x:
    def __del__(self):
        print
        "x got deleted!"


def run():
    mydata.foo = x()


t = threading.Thread(target=run)
t.start()
print("t started")
del mydata
print("mydata deleted")
t.join()
print("t joined")
