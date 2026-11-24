import threading
counter=0
lock=threading.Lock()
def increment():
    global counter
    for _ in range(1_000_000):
        c=counter
        time.sleep(0)
        counter=c+1
threads=[threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)
