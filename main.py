import time
a = 1
b = 1
while True:
    a, b = b, a + b
    print(a)
    time.sleep(0.2)
