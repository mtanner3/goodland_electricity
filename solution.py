import sys
num_cities, tower_range = map(int,raw_input().strip().split())
tower_range -= 1
tower_presence_arr = map(int,raw_input().strip().split())

print "tower range = %d" % tower_range

towers_on = 0
solvable = True
prev_tpidx = 0
tpidx = tower_range
while True:
    print "prevcity = %d. looking at idx=%d" % (prev_tpidx, tpidx)
    if tower_presence_arr[tpidx] == 1:
        towers_on += 1
        print "  Tower. Switching on. %d" % towers_on
        tpidx += tower_range
        prev_tpidx = tpidx
        tpidx += tower_range
        if tpidx > num_cities:
            break
    else:
        print "  no tower. Backing up"
        tpidx -= 1
        if tpidx == prev_tpidx:
            solvable = False
            break

print towers_on
