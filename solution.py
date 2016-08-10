import sys
num_cities, tower_range = map(int,raw_input().strip().split())
tower_range -= 1
tower_presence_arr = map(int,raw_input().strip().split())

DEBUG = False

towers_on = 0
solvable = True
dark_idx = 0
tpidx = dark_idx + tower_range
while True:
    if DEBUG: print "dark city = %d. looking for tower at idx=%d" % (dark_idx, tpidx),
    if tpidx >= num_cities: 
        break
    if tower_presence_arr[tpidx] == 1:
        towers_on += 1
        if DEBUG: print "\n  Switching on tower %d. Total on = %d" % (tpidx, towers_on)
        tpidx += tower_range
        if tpidx >= (num_cities-1):
            break
        dark_idx = tpidx + 1
        tpidx = min(dark_idx + tower_range, (num_cities-1))
    else:
        if DEBUG: print "no tower. Backing up"
        tpidx -= 1
        if tpidx < (dark_idx - tower_range):
            solvable = False
            break

if solvable is False:
    print "-1"
else:
    print towers_on
