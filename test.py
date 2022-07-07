import baseball
import random
from copy import deepcopy

count = [0,0] ##balls,strikes
arsenal = [0,1,9,11]
y = 0
while y < 100:
    a = baseball.CatcherCall(15,0,arsenal,0,count)
    print(a)
    y += 1
