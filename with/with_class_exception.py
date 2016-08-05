import ctypes


class IntChanger:
    def __init__(self, statement_to_change):
        self.statement_address = id(statement_to_change)
        self.statement_to_change = bytes([statement_to_change])
        ctypes.cast(self.statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = b'\x2A'

    def __enter__(self):
        return 'But we had a {}?'.format(int.from_bytes(self.statement_to_change, byteorder='little'))

    def __exit__(self, exception_type, exception_value, traceback):
        # print(exception_type)
        # print(exception_value)
        # print(traceback)
        # print('The 112 is {}'.format(112))
        ctypes.cast(self.statement_address, ctypes.POINTER(ctypes.c_char))[3 * 8] = self.statement_to_change
        print('Now 112 is {}'.format(112))
        if exception_type == ZeroDivisionError:
            print('Doing something...')
            # sending signal to interpreter that everything is OK.
            # return True

if __name__ == "__main__":
    with IntChanger(112) as answer:
        print('In this context The 112 is {}'.format(112))
        1/0
    print(answer)


