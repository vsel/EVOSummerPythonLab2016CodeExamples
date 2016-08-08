import ctypes

from contextlib import contextmanager


@contextmanager
def int_changer(statement_to_change):
    # __init__
    statement_address = id(statement_to_change)
    old_value = bytes([statement_to_change])
    # __enter__
    ctypes.cast(statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = b'\x2A'
    try:
        yield 'But we had a {}!!!'.format(int.from_bytes(old_value, byteorder='little'))
    # __exit__
    except:
        print("Do something...")
    finally:
        ctypes.cast(statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = \
            old_value
        print('Now 112 is {}'.format(112))

if __name__ == "__main__":
    with int_changer(112) as answer:
        print('The 112 is {}'.format(112))
        # print(answer)
        1/0
    print(answer)
