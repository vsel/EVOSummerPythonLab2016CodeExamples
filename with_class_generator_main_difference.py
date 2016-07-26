import ctypes

from contextlib import contextmanager


@contextmanager
def int_changer(statement_to_change):
    # __init__
    statement_address = id(statement_to_change)
    statement_to_change = bytes([statement_to_change])
    ctypes.cast(statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = b'\x2A'
    # __enter__
    yield 'But we had a {}!!!'.format(int.from_bytes(statement_to_change, byteorder='little'))
    # __exit__
    ctypes.cast(statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = statement_to_change
    print('Now 112 is {}'.format(112))


class IntChanger:
    def __init__(self, statement_to_change):
        self.statement_address = id(statement_to_change)
        self.statement_to_change = bytes([statement_to_change])
        ctypes.cast(self.statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = b'\x2A'

    def __enter__(self):
        return 'But we had a {}!!!'.format(int.from_bytes(self.statement_to_change, byteorder='little'))

    # Why does this exception_type, exception_value, traceback needed I will tell you later
    def __exit__(self, exception_type, exception_value, traceback):
        ctypes.cast(self.statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = self.statement_to_change
        print('Now 112 is {}'.format(112))


if __name__ == "__main__":
    try:
        with IntChanger(112) as answer:
            print('The 112 is {}'.format(112))
            1 / 0
    except:
        print('Except 112 is {}'.format(112))
    try:
        with int_changer(112) as answer:
            print('The 112 is {}'.format(112))
            1 / 0
    except:
        print('Except 112 is {}'.format(112))
