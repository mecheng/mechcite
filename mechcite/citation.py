from mechcite import Bibliography
from functools import wraps


class cite(object):
    def __init__(self, key):
        self.key = key
        self.used = False
        self.bib = Bibliography()

    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            if not self.used:
                self.bib.cite(self.key)
                self.used = True
            return f(*args, **kwargs)

        return wrapped_f
