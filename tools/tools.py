from functools import wraps
import threading
from time import sleep


def async(func):
    @wraps
    def func_wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return func_wrapper

@async
def destroy_graph(g, time):
    sleep(time)
    g.destroy()