counter = 0
result = 'Not done'
while counter < 50:
    counter += 1
    print(counter)
else:
    result = 'Done'

print(result)

counter = 0
result = 'Not done'
while counter < 50:
    counter += 1
    break
else:
    # to check that something stoped while
    result = 'Not done'

print(result)
