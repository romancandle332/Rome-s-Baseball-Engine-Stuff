import math
import random

def SkillConvert(x,metric): ##Converts player attributes into different values
    skill_input = round((x - 12.5)/2.5,3)
    if metric == 0: ##Meter Value, like Pitch Control in baseball games
        output = round(random.gauss(50 + skill_input * 12.5,6.25))
    return output

class Pitch:
    def __init__(self,a,b,c,d,e,f,g,h):
        self.name = a
        self.group = b
        self.mph_avg = c
        self.mph_dev = d
        self.whiff_avg = e
        self.whiff_dev = f
        self.movement = g ##movement is listed as positive = down and right from a RHP as viewed by the batter/catcher
        self.break_direction = h ##0 glove side, 1 arm side

FSM = Pitch("4-Seam Fastball","Fastball",93.51,2.27,0.211,0.053,[-2,-2],1)
CUT = Pitch("Cut Fastball","Fastball",88.55,2.53,0.251,0.075,[-1,1],0)
TSM = Pitch("2-Seam Fastball","Fastball",88.55,2.53,0.251,0.075,[-1,-4],1)
SPT = Pitch("Split-Finger Fastball","Fastball",85.78,2.30,0.375,0.71,[3,0],0)
SNK = Pitch("Sinking Fastball","Fastball",92.56,2.55,0.148,0.040,[1,1],0)
CHN = Pitch("Change-Up","Offspeed",84.58,2.93,0.305,0.066,[0,-2],1)
CIR = Pitch("Circle Change","Offspeed",80.58,2.93,0.305,0.66,[1,-2],1)
PLM = Pitch("Palmball","Offspeed",78.58,2.93,0.305,0.066,[2,-1],1)
EPH = Pitch("Eephus","Offspeed",65.18,3.85,0.242,0.104,[-1,-1],1)
GYR = Pitch("Gyro Bullet","Offspeed",82.58,3.43,0.211,0.111,[0,0],0)
SLD = Pitch("Slider","Breaking",84.65,2.89,0.357,0.76,[1,5],0)
CRV = Pitch("Curveball","Breaking",78.72,3.28,0.320,0.075,[6,2],0)
TSC = Pitch("12-6 Curveball","Breaking",75.72,3.28,0.320,0.075,[7,0],0)
SLV = Pitch("Slurve","Breaking",70.60,4.16,0.261,0.069,[4,4],0)
SCR = Pitch("Screwball","Breaking",73.41,4.18,0.371,0.091,[6,-2],1)
FOR = Pitch("Forkball","Breaking",82.48,3.41,0.287,0.097,[4,0],0)
KCV = Pitch("Knuckle-Curve","Breaking",79.64,2.98,0.297,0.110,[4,1],0)
KNB = Pitch("Knuckleball","Breaking",71.92,4.22,0.223,0.028,[0,0],0)

pitch_dictionary = {}
pitch_dictionary[0] = FSM
pitch_dictionary[1] = CUT
pitch_dictionary[2] = TSM
pitch_dictionary[3] = SPT
pitch_dictionary[4] = SNK
pitch_dictionary[5] = CHN
pitch_dictionary[6] = CIR
pitch_dictionary[7] = PLM
pitch_dictionary[8] = EPH
pitch_dictionary[9] = GYR
pitch_dictionary[10] = SLD
pitch_dictionary[11] = CRV
pitch_dictionary[12] = TSC
pitch_dictionary[13] = SLV
pitch_dictionary[14] = SCR
pitch_dictionary[15] = FOR
pitch_dictionary[16] = KCV
pitch_dictionary[17] = KNB

pitch_zone = list(range(225))
strike_zone = []
ball_zone = pitch_zone[:]
tight_strike_zone = []
wide_strike_zone = []
strike_zone_edges = []
for x in pitch_zone:
    whole = x // 15
    remainder = x % 15
    if 3 <= whole <= 11 and 3 <= remainder <= 11:
        strike_zone.append(x)
        ball_zone.remove(x)
    if 2 <= whole <= 12 and 2 <= remainder <= 12:
        wide_strike_zone.append(x)
        strike_zone_edges.append(x)
    if 4 <= whole <= 10 and 4 <= remainder <= 10:
        tight_strike_zone.append(x)
        strike_zone_edges.remove(x)
        
def PitchZone(zone): ##Setting zone base values
    whole = zone // 15
    remainder = zone % 15
    x = whole - 7
    y = remainder - 7
    return [x,y]

def WhatZone(x,y):
    zone_x = (round(x) + 7)*15
    zone_y = (round(y) + 7)*15
    zone = zone_x + zone_y
    return zone

def CatcherCall(Catcher_Call_Skill,Batter_Hand,Pitcher_Arsenal,Pitcher_Hand,count):
    call_rating = SkillConvert(Catcher_Call_Skill,0)
    print(call_rating)

    if call_rating >= 40: ##Catchers separate pitches into types
        fastballs = []
        breaking_balls = []
        offspeed = []
        for x in Pitcher_Arsenal:
            pitch_type = pitch_dictionary[x].group
            if pitch_type == "Fastball":
                fastballs.append(x)
            elif pitch_type == "Breaking":
                breaking_balls.append(x)
            elif pitch_type == "Offspeed":
                offspeed.append(x)
            else:
                print("Pitch type error during Catcher Call")
        if not offspeed:
            offspeed = breaking_balls[:]
        if not breaking_balls:
            breaking_balls = offspeed[:]

    if call_rating < 0: ##Very worst
        pitch_pick = random.choice(Pitcher_Arsenal) ##Picks random pitch
        location_roll = random.choice(pitch_zone) ##Throw it anywhere
    elif 0 <= call_rating < 10: ##Very Bad
        pitch_pick = random.choice(Pitcher_Arsenal) ##Picks random pitch
        random_roll = random.randint(0,4) ##Knows there's a strikezone
        if random_roll == 4: ##Doesn't know exactly where it is.
            location_roll = random.choice(strike_zone)
        elif random_roll == 3 or random_roll == 1:
            location_roll = random.choice(tight_strike_zone)
        else:
            location_roll = random.choice(wide_strike_zone)
    elif 10 <= call_rating < 25: ##Bad
        pitch_pick = random.choice(Pitcher_Arsenal) ##Picks random pitch
        if count[0] >= 3: ##Tries to avoid a walk
            location_roll = random.choice(tight_strike_zone)
        else:
            location_roll = random.choice(strike_zone)

    elif 25 <= call_rating < 40: ##Below Average
        if count[0] >= 3: ##Tries to avoid a walk
            location_roll = random.choice(tight_strike_zone)
            pitch_pick = random.choice(fastballs)
        else:
            pitch_pick = random.choice(Pitcher_Arsenal)
            location_roll = random.choice(strike_zone)
    elif 40 <= call_rating < 60: ##Average
        if count[0] >= count[1]: ##Uses fastballs when behind in count
            pitch_pick = random.choice(fastballs)
        else:
            pitch_pick = random.choice(Pitcher_Arsenal)
        if count[0] >= 3:
            location_roll = random.choice(tight_strike_zone)
        else:
            location_roll = random.choice(strike_zone)

    elif 60 <= call_rating < 75: ##Above Average
        random_roll = random.randint(0,4)
        if count[1] > count[0]: ##Ahead in count
            if random_roll == 0: ##Prefers breaking/offspeed
                pitch_pick = random.choice(fastballs)
            elif 1 <= random_roll < 3:
                pitch_pick = random.choice(breaking_balls)
            elif 3 <= random_roll <= 4:
                pitch_pick = random.choice(offspeed)
        elif count[0] == 3: ##Avoids Walk
            pitch_pick = random.choice(fastballs)
        elif count[0] >= count[1]: ##Behind in the count
            if random_roll <= 2: ##Prefers Fastballs
                pitch_pick = random.choice(fastballs)
            elif random_roll == 3:
                pitch_pick = random.choice(breaking_balls)
            elif random_roll == 4:
                pitch_pick = random.choice(offspeed)
        else: ##Picks at random to avoid errors
            pitch_pick = random.choice(Pitcher_Arsenal)
        if count[0] >= 3: ##Avoids walk
            location_roll = random.choice(tight_strike_zone)
        elif count[1] > count[0]: ##May fish for a swinging strike when ahead
            location_roll = random.choice(wide_strike_zone)
        else:
            location_roll = random.choice(strike_zone)
    elif 75 <= call_rating < 90: ##Good
        random_roll = random.randint(0,4)
        if count[1] > count[0]: ##Ahead in count
            if random_roll == 0: ##Prefers breaking/offspeed
                pitch_pick = random.choice(fastballs)
            elif 1 <= random_roll < 3:
                pitch_pick = random.choice(breaking_balls)
            elif 3 <= random_roll <= 4:
                pitch_pick = random.choice(offspeed)
        elif count[0] == 3: ##Avoids Walk
            pitch_pick = random.choice(fastballs)
        elif count[0] >= count[1]: ##Behind in the count
            if random_roll <= 2: ##Prefers Fastballs
                pitch_pick = random.choice(fastballs)
            elif random_roll == 3:
                pitch_pick = random.choice(breaking_balls)
            elif random_roll == 4:
                pitch_pick = random.choice(offspeed)
        else: ##Picks at random to avoid errors
            pitch_pick = random.choice(Pitcher_Arsenal)
        if count[0] >= 3: ##Avoids walk
            call_zone = strike_zone[:]
        elif count[1] > count[0]: ##Ahead in count
            call_zone = strike_zone_edges[:]
        else:
            call_zone = strike_zone[:]
        pitch_type = pitch_dictionary[pitch_pick].group
        if pitch_type == "Breaking" or pitch_type == "Offspeed":
            for x in call_zone: ##Non-FB target bottom half of zone
                coords = PitchZone(x)
                if coords[0] <= 0:
                    call_zone.remove(x)
        location_roll = random.choice(call_zone)
    elif 90 <= call_rating < 100: ##Very Good
        random_roll = random.randint(0,4)
        if count[1] > count[0]: ##Ahead in count
            if random_roll == 0: ##Prefers breaking/offspeed
                pitch_pick = random.choice(fastballs)
            elif 1 <= random_roll < 3:
                pitch_pick = random.choice(breaking_balls)
            elif 3 <= random_roll <= 4:
                pitch_pick = random.choice(offspeed)
        elif count[0] == 3: ##Avoids Walk
            pitch_pick = random.choice(fastballs)
        elif count[0] >= count[1]: ##Behind in the count
            if random_roll <= 2: ##Prefers Fastballs
                pitch_pick = random.choice(fastballs)
            elif random_roll == 3:
                pitch_pick = random.choice(breaking_balls)
            elif random_roll == 4:
                pitch_pick = random.choice(offspeed)
        else: ##Picks at random to avoid errors
            pitch_pick = random.choice(Pitcher_Arsenal)
        if count[0] >= 3: ##Avoids walk
            call_zone = strike_zone[:]
        elif count[1] > count[0]: ##Ahead in count
            call_zone = strike_zone_edges[:]
        else:
            call_zone = strike_zone[:]
        pitch_type = pitch_dictionary[pitch_pick].group
        if pitch_type == "Breaking" or pitch_type == "Offspeed":
            for x in call_zone: ##Non-FB target bottom third of zone
                coords = PitchZone(x)
                if coords[0] <= 1:
                    call_zone.remove(x)
        location_roll = random.choice(call_zone)
    elif 100 <= call_rating: ##Elite
        random_roll = random.randint(0,4)
        if count[1] > count[0]: ##Ahead in count
            if random_roll == 0: ##Prefers breaking/offspeed
                pitch_pick = random.choice(fastballs)
            elif 1 <= random_roll < 3:
                pitch_pick = random.choice(breaking_balls)
            elif 3 <= random_roll <= 4:
                pitch_pick = random.choice(offspeed)
        elif count[0] == 3: ##Avoids Walk
            pitch_pick = random.choice(fastballs)
        elif count[0] >= count[1]: ##Behind in the count
            if random_roll <= 2: ##Prefers Fastballs
                pitch_pick = random.choice(fastballs)
            elif random_roll == 3:
                pitch_pick = random.choice(breaking_balls)
            elif random_roll == 4:
                pitch_pick = random.choice(offspeed)
        else: ##Picks at random to avoid errors
            pitch_pick = random.choice(Pitcher_Arsenal)
        if count[0] >= 3: ##Avoids walk
            call_zone = strike_zone[:]
        else:
            call_zone = strike_zone_edges[:]
        pitch_type = pitch_dictionary[pitch_pick].group
        for x in call_zone: ##Makes several adjustments
            coords = PitchZone(x)
            if pitch_type == "Breaking" or pitch_type == "Offspeed":  ##Non-FB target bottom range of zone
                if coords[0] <= 2:
                    call_zone.remove(x)
            if -2 < coords[0] < 2 and -2 < coords[1] < 2: ##Nevers calls it over the middle
                call_zone.remove(x)
        location_roll = random.choice(call_zone)
    else:
        print("Call Rating Error")
    location = PitchZone(location_roll)
    pitch_call_name = pitch_dictionary[pitch_pick].name
    return [pitch_pick,pitch_call_name,location]
    
def PitchLocation(strikes,balls,pitch_con,pitch_movement,pitch_break): ##Determining where the Pitcher throws the ball
    secondary_list = list(range(9))
    if balls == 3: ##Needs a Strike
        zone_a = random.choice(strike_zone)
        if zone_a // 5 == 1: ##Top of the Zone
            secondary_list.remove(0)
            secondary_list.remove(1)
            secondary_list.remove(2)
            if zone_a % 5 == 1: ##Inside
                secondary_list.remove(3)
                secondary_list.remove(6)
            elif zone_a % 5 == 3: ##Outside
                secondary_list.remove(5)
                secondary_list.remove(8)
        elif zone_a // 5 == 3: ##Bottom of the Zone
            secondary_list.remove(6)
            secondary_list.remove(7)
            secondary_list.remove(8)
            if zone_a % 5 == 1: ##Inside
                secondary_list.remove(0)
                secondary_list.remove(3)
            elif zone_a % 5 == 3: ##Outside
                secondary_list.remove(2)
                secondary_list.remove(5)
        else:
            if zone_a % 5 == 1: ##Inside
                secondary_list.remove(0)
                secondary_list.remove(3)
                secondary_list.remove(6)
            elif zone_a % 5 == 3: ##Outside
                secondary_list.remove(2)
                secondary_list.remove(5)
                secondary_list.remove(8)
        zone_b = random.choice(secondary_list)
    else:
        zone_a = random.choice(pitch_zone)
        if zone_a // 5 == 0: ##Top of the Zone
            secondary_list.remove(0)
            secondary_list.remove(1)
            secondary_list.remove(2)
            if zone_a % 5 == 0: ##Inside
                secondary_list.remove(3)
                secondary_list.remove(6)
            elif zone_a % 5 == 5: ##Outside
                secondary_list.remove(5)
                secondary_list.remove(8)
        elif zone_a // 5 == 5: ##Bottom of the Zone
            secondary_list.remove(6)
            secondary_list.remove(7)
            secondary_list.remove(8)
            if zone_a % 5 == 0: ##Inside
                secondary_list.remove(0)
                secondary_list.remove(3)
            elif zone_a % 5 == 5: ##Outside
                secondary_list.remove(2)
                secondary_list.remove(5)
        else:
            if zone_a % 5 == 0: ##Inside
                secondary_list.remove(0)
                secondary_list.remove(3)
                secondary_list.remove(6)
            elif zone_a % 5 == 4: ##Outside
                secondary_list.remove(2)
                secondary_list.remove(5)
                secondary_list.remove(8)
        zone_b = random.choice(secondary_list)
    target = PitchZone(zone_a,zone_b)
    target_zone = [zone_a,zone_b]

    ##using pitcher break to adjust actual trajectory
    break_x_adjust = pitch_break / 17.5 * pitch_movement[0] * random.uniform(0.8,1.05)
    break_y_adjust = pitch_break / 17.5 * pitch_movement[1] * random.uniform(0.8,1.05)
    release_x = target[0] - break_x_adjust
    release_y = target[1] - break_y_adjust
    release_intended = [release_x,release_y]

    ##using pitcher control to adjust release accuracy
    control_roll = round(random.uniform(-5,20),2)
    if control_roll > pitch_con:
        x_roll = random.randint(30,70)
        y_roll = 100 - x_roll
        error_roll = random.gauss((control_roll-pitch_con)/2.5,1)
        control_adjust_x = error_roll * x_roll/100 * random.choice([-1,1])
        control_adjust_y = error_roll * y_roll/100 * random.choice([-1,1])
    else:
        control_adjust_x = 0
        control_adjust_y = 0
    release_x_actual = round(release_x + control_adjust_x,2)
    release_y_actual = round(release_y + control_adjust_y,2)
    release_actual = [release_x_actual,release_y_actual]
    actual_x = round(release_x_actual + break_x_adjust,2)
    actual_y = round(release_y_actual + break_y_adjust,2)
    location_actual = [actual_x,actual_y]
    actual_zone = IntoPitchZone(actual_x,actual_y)
    secondary_list = list(range(9))
    return [target,target_zone,release_intended,release_actual,location_actual,actual_zone]
