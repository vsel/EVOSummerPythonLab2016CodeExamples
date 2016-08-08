counter = 0
result = 'Not done'
while counter < 10:
    counter += 1
    print(counter, end=', ')
else:
    result = 'Done'

print(result)

counter = 0
result = 'Not done'
while counter < 10:
    counter += 1
    print(counter, end=', ')
    if counter > 2:
        break
else:
    # to check that something stoped while
    result = 'Done'

print(result)
