# Teemo Attacking
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe,
# Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will meanAshe is poisoned
# during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends,
# the timer for it is reset, and the poison effect will end duration seconds after the new attack. You are given a
# non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[
# i], and an integer duration. Return the total number of seconds that Ashe is poisoned.


def findPoisonedDuration(timeSeries, duration):
    res = 0
    for i in range(0, len(timeSeries) - 1):
        s = timeSeries[i] + duration - 1
        if s < timeSeries[i + 1]:
            res += s - timeSeries[i] + 1
        else:
            res += timeSeries[i + 1] - timeSeries[i]

    res += duration
    return res


a = [1, 2]
a.reverse()
b = 2
print(findPoisonedDuration(a, b))
