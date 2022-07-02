import math
import random

def GetPitch(x,y,r): ##library of different pitch attributes. x is what pitch you want, y is what attribute you want outputted, r is pitch throwing hand
    if x == "4SM":
        pitch_name = "4-Seam Fastball"
        pitch_type = "Fastball"
        mph_avg = 93.51
        mph_dev = 2.27
        whiff_avg = 0.211
        whiff_dev = 0.053
        movement = [-1,-1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "CUT":
        pitch_name = "Cut Fastball"
        pitch_type = "Fastball"
        mph_avg = 88.55
        mph_dev = 2.53
        whiff_avg = 0.251
        whiff_dev = 0.075
        movement = [1,1] ##Measured against GYR; Positive = Down and Right from Batter      

    elif x == "2SM":
        pitch_name = "2-Seam Fastball"
        pitch_type = "Fastball"
        mph_avg = 88.55
        mph_dev = 2.53
        whiff_avg = 0.251
        whiff_dev = 0.075
        movement = [1,-1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "SPT":
        pitch_name = "Split-Finger Fasterball"
        pitch_type = "Fastball"
        mph_avg = 85.78
        mph_dev = 2.30
        whiff_avg = 0.375
        whiff_dev = 0.071
        movement = [3,0] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "SNK":
        pitch_name = "Sinking Fastball"
        pitch_type = "Fastball"
        mph_avg = 92.56
        mph_dev = 2.55
        whiff_avg = 0.148
        whiff_dev = 0.040
        movement = [2,1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "CHN":
        pitch_name = "Change-Up"
        pitch_type = "Offspeed"
        mph_avg = 84.58
        mph_dev = 2.93
        whiff_avg = 0.305
        whiff_dev = 0.066
        movement = [2,0] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "CIR":
        pitch_name = "Circle Change"
        pitch_type = "Offspeed"
        mph_avg = 80.58
        mph_dev = 2.93
        whiff_avg = 0.305
        whiff_dev = 0.066
        movement = [2,-1] ##Measured against GYR; Positive = Down and Right from Batter


    elif x == "PLM":
        pitch_name = "Palmball"
        pitch_type = "Offspeed"
        mph_avg = 78.58
        mph_dev = 2.93
        whiff_avg = 0.305
        whiff_dev = 0.066
        movement = [3,1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "SLD":
        pitch_name = "Slider" 
        pitch_type = "Breaking"
        mph_avg = 84.65
        mph_dev = 2.89
        whiff_avg = 0.357
        whiff_dev = 0.76
        movement = [2,5] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "CRV":
        pitch_name = "Curveball"
        pitch_type = "Breaking"
        mph_avg = 78.72
        mph_dev = 3.28
        whiff_avg = 0.320
        whiff_dev = 0.075
        movement = [6,2] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "126":
        pitch_name = "12-6 Curveball"
        pitch_type = "Breaking"
        mph_avg = 75.72
        mph_dev = 3.28
        whiff_avg = 0.320
        whiff_dev = 0.075
        movement = [7,0] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "SLV":
        pitch_name = "Slurve"
        pitch_type = "Breaking"
        mph_avg = 70.60
        mph_dev = 4.16
        whiff_avg = 0.261
        whiff_dev = 0.069
        movement = [4,4] ##Measured against GYR; Positive = Down and Right from Batter


    elif x == "SCR":
        pitch_name = "Screwball"
        pitch_type = "Breaking"
        mph_avg = 73.41
        mph_dev = 4.18
        whiff_avg = 0.371
        whiff_dev = 0.091
        movement = [6,-2] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "FOR":
        pitch_name = "Forkball"
        pitch_type = "Breaking"
        mph_avg = 82.48
        mph_dev = 3.41
        whiff_avg = 0.287
        whiff_dev = 0.097
        movement = [4,0] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "KCV":
        pitch_name = "Knuckle-Curve"
        pitch_type = "Breaking"
        mph_avg = 79.64
        mph_dev = 2.98
        whiff_avg = 0.297
        whiff_dev = 0.110
        movement = [4,1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "KNB":
        pitch_name = "Knuckleball"
        pitch_type = "Breaking"
        mph_avg = 71.92
        mph_dev = 4.22
        whiff_avg = .223
        whiff_dev = .028
        vert = round(random.uniform(-4,6))
        horz = round(random.uniform(-4,6))
        movement = [vert,horz] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "EPH":
        pitch_name = "Eephus"
        pitch_type = "Offspeed"
        mph_avg = 65.18
        mph_dev = 3.85
        whiff_avg = 0.242
        whiff_dev = 0.104
        horz = random.randint(0,1)
        roll = random.randint(0,1)
        if roll == 1:
            horz *= -1
        movement = [horz,1] ##Measured against GYR; Positive = Down and Right from Batter

    elif x == "GYR":
        pitch_name = "Gyro Bullet"
        pitch_type = "Offspeed"
        mph_avg = 82.58
        mph_dev = 3.43
        whiff_avg = 0.211
        whiff_dev = 0.111
        movement = [0,0] ##Measured against GYR; Positive = Down and Right from Batter

    if y == "movement":
        if r == 1: ##LHP
            movement[1] *= -1
    return y
