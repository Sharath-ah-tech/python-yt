import random
from datetime import datetime, timedelta

print(random.uniform(1, 100))
print(random.random())
 
print(random.randint(1, 100))
print(random.randrange(1, 100, 2))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample([1, 2, 3, 4, 5], 3))

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst) 

print(random.getrandbits(8))
print(random.triangular(1, 10))
print(random.gauss(0, 1))
print(random.lognormvariate(0, 1))

now = datetime.now()

print(now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.date(), now.time())

print(now + timedelta(days=7))
