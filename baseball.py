import math
import random

class Pitch:
    def __init__(self,a,b,c,d,e,f,g):
        self.name = a
        self.group = b
        self.mph_avg = c
        self.mph_dev = d
        self.whiff_avg = e
        self.whiff_dev = f
        self.movement = g

FSM = Pitch("4-Seam Fastball","Fastball",93.51,2.27,0.211,0.053,[-1,-1])
CUT = Pitch("Cut Fastball","Fastball",88.55,2.53,0.251,0.075,[1,1])
TSM = Pitch("2-Seam Fastball","Fastball",88.55,2.53,0.251,0.075,[1,-1])
SPT = Pitch("Split-Finger Fastball","Fastball",85.78,2.30,0.375,0.71,[3,0])
SNK = Pitch("Sinking Fastball","Fastball",92.56,2.55,0.148,0.040,[2,1])
CHN = Pitch("Change-Up","Offspeed",84.58,2.93,0.305,0.066,[2,0])
CIR = Pitch("Circle Change","Offspeed",80.58,2.93,0.305,0.66,[2,-1])
PLM = Pitch("Palmball","Offspeed",78.58,2.93,0.305,0.066,[3,1])
EPH = Pitch("Eephus","Offspeed",65.18,3.85,0.242,0.104,[1,1])
GYR = Pitch("Gyro Bullet","Offspeed",82.58,3.43,0.211,0.111,[0,0])
SLD = Pitch("Slider","Breaking",84.65,2.89,0.357,0.76,[2,5])
CRV = Pitch("Curveball","Breaking",78.72,3.28,0.320,0.075,[6,2])
TSC = Pitch("12-6 Curveball","Breaking",75.72,3.28,0.320,0.075,[7,0])
SLV = Pitch("Slurve","Breaking",70.60,4.16,0.261,0.069,[4,4])
SCR = Pitch("Screwball","Breaking",73.41,4.18,0.371,0.091,[6,-2])
FOR = Pitch("Forkball","Breaking",82.48,3.41,0.287,0.097,[4,0])
KCV = Pitch("Knuckle-Curve","Breaking",79.64,2.98,0.297,0.110,[4,1])
KNB = Pitch("Knuckleball","Breaking",71.92,4.22,0.223,0.028,[round(random.uniform(-4,6)),round(random.uniform(-4,6))])

def GetPitch(x,y,h):
    if y == "movement":
        if h == "1": ##LHP
            q = x.movement[1]
            z = x.movement[0]
            q *= -1
            result = [z,q]
            return result
        else:
            result = x.movement
            return result
    else:
        result = x.y
        return result
