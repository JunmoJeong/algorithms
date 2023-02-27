import numpy
lotto = numpy.random.choice(range(1,46),6,replace=False)
lotto.sort()
print(lotto)