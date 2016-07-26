import dis
from time import sleep

original = [1, 2, 3]
print('Address in memory {memory_address}'.format(memory_address=hex(id(original))))
copy = original
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))


def copy_staright_way(copy_from_outer_scope):
    copy_from_outer_scope = copy_from_outer_scope + [4, 5, 6]
dis.dis(copy_staright_way)
copy_staright_way(copy)
print(copy)
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))


def copy_by_plus_equal(copy_from_outer_scope):
    copy_from_outer_scope += [4, 5, 6]
dis.dis(copy_by_plus_equal)
copy_by_plus_equal(copy)
print(copy)
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))

print(hex(id(123)))

# sudo gdb -p 31959
# x/5 0x114ed40

# sleep(1000000)
