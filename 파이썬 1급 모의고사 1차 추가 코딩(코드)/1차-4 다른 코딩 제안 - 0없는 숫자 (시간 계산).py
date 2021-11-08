import time

start= time.time()

num = 9949999;

for i in range(100):
      answer=int(str(num+1).replace('0','1'))
 

end= time.time()

print(end-start)

############################

start= time.time()

num = 9949999;

num = num+1
digit = 1

for i in range(100):
    while num // digit % 10 == 0:
         num+= digit
         digit *= 10

end= time.time()

print(end-start)
