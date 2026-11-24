import multiprocessing
import time

def heavy_cale(n):
    print(f"Процесс считает для n={n}")
    total=sum(i*i for i in range(n))
    return total

if __name__=="__main__":
    p1=multiprocessing.Process(target=heavy_cale, args=(10_000_000,))
    p2=multiprocessing.Process(target=heavy_cale, args=(10_000_000,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Оба процесса завершились")
    
    #print(f"Значение __name__:{__name__}")
    #if __name__==
    
    
    
    """DZ: multiprocessing.Queue
                       .Pipe 
                       .Manager"""