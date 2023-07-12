import multiprocessing
import time
from multiprocessing.pool import Pool

def f(i):
    time.sleep(2)
    print(i)


start = time.time()
        #1
# p_list = []
# for i in range(10):
#     p = multiprocessing.Process(target=f, args=(i,))
#     p.start()
#     p_list.append(p)
#
# for i in p_list:
#     i.join()

        #2
with Pool() as pool:
    pool.map(f,list(range(10)))

print(time.time() - start)
