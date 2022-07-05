from multiprocessing import Lock as multiprocessing_Lock


class Dummy():
    def dummy(self, *args, **kw):
        pass

    def __getattr__(self, name):
        return self.dummy

class Lock:
    def __init__(self, *args, **kwargs):
        self._lock = multiprocessing_Lock()

    def dummy(self, *args, **kw):
        pass

    def __getattr__(self, name):
        return self.dummy

    def __enter__(self):
        self._lock.__enter__()
        return Dummy()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.__exit__(exc_type, exc_val, exc_tb)
        return Dummy()


__version__ = '2.3.2'

LOCK_EX = False
LOCK_NB = True
