import multiprocessing
import time
import random
from datetime import datetime

def worker():
    
    time.sleep(random.random())
    
    
    print(f"Process {multiprocessing.current_process().name}: {datetime.now()}")

if __name__ == "__main__":
    processes = []

    
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    
    for p in processes:
        p.join()