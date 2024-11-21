
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as n
import matplotlib.pyplot as pl

x = n.random.normal(5.0, 1.0, 1000)
y = n.random.normal(10.0, 2.0, 1000)

pl.scatter(x, y)
pl.show()


pl.savefig(sys.stdout.buffer)
sys.stdout.flush()

#n.random.normal(x,y,z) does mean x is a mean , y is a deviation , z is numbers of datas
