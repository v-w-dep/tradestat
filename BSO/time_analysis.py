import time

def time_decorator(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if (te - ts)>=0: print(f'{method.__name__}  {(te - ts):2.2f} seconds')
        else: print(f'{method.__name__}  {(te - ts)/1000 :2.2f} ms')
        return result
    return timed
