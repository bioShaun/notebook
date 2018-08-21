import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args, **kwargs):
            t0 = time.time()
            _result = func(*_args, **kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            arg_lst = []
            if _args:
                arg_lst.append(', '.join(repr(arg) for arg in _args))
            if kwargs:
                pairs = ['%s=%r' % (k, w)
                         for k, w in sorted(kwargs.items * ())]
                arg_lst.append(', '.join(pairs))
            args = ', '.join(arg_lst)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
