
import sys
import matplotlib
matplotlib.use('TkAgg')

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)


x=[]

for i in range(4):
    element = float(input("enter number-eleman gir ".format(i+1)))
    x.append(element)

print("list-liste", x)
y = numpy.random.normal(150, 40, 4) / x

train_x = x[:4]
train_y = y[:4]

test_x = x[4:]
test_y = y[4:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 100, 4)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
