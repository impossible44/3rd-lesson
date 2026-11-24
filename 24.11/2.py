import threading
import time

def worker(name, sleep_time):
    print(f"Поток {name}: засыпаю на {sleep_time} c")
    time.sleep(sleep_time)
    print(f"Поток {name} завершен")
t1=threading.Thread(target=worker, args=("A",2))
t2=threading.Thread(target=worker, args=("B",5))
t1.start()
t2.start()
t1.join()
t2.join()
print("Все потоки завершены")