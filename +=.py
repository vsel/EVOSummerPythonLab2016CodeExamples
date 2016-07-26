original = [1, 2, 3]
print('Address in memory {memory_address}'.format(memory_address=hex(id(original))))
copy = original
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))
copy = copy + [1, 2, 3]
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))
copy += [1, 2, 3]
print('Address in memory {memory_address}'.format(memory_address=hex(id(copy))))
