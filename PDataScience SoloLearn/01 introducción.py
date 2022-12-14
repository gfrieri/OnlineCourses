players = [14,18,19,24,26,33,42,55,67]
#your code goes here
sum = 0
for a in players:
    sum = sum + a

sum = sum/int(len(players))
print('Mean:', sum)

var = 0
for a in players:
    var = (sum - a)**2 + var

var = var/int(len(players))
print('Variance:', var)
sd = var**0.5
print('Standard Deviation:', sd)

osdcount = 0
for a in players:
    y = float(a)
    if (y >= sum-sd) & (y <= sum+sd):
        osdcount = osdcount + 1

print('Count of values within one standard deviation:', osdcount)
