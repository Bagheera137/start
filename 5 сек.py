import time
a=time.time()
while True:
    b=time.time()-a
   # print(b)
    if b>=1:
        print("огонь")
        a=time.time()

