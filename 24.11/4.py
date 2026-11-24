import threading
import queue
import time

q=queue.Queue()
def producer():
    for i in range(5):
        q.put(f"item -{i}")
        time.sleep(0.1)
    q.put(None)
def consumer():
    while True:
        item=q.get()
        if item is None:
            break
        print(f"Получил {item}")
t_prod=threading.Thread(target=producer)
t_cons=threading.Thread(target=consumer)
t_prod.start()
t_cons.start()
t_prod.join()
t_cons.join()