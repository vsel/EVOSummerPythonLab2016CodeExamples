try:
    # 1/0
    0/1
except ZeroDivisionError:
    print('Exception, but you can go on')
else:
    print('No Exceptions. Done.')
finally:
    print('OK then')
