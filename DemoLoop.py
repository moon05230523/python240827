# DemoLoop.py

lst = [10, 20, 30]
for i in lst:
    print("Item:{0}".format(i))

iterL = filter(None, lst)
for item in iterL:
    print(item)

def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)   