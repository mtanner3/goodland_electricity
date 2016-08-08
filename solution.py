import sys
#import array
num_cities, tower_range = map(int,raw_input().strip().split())
tower_range -= 1
tower_presence_arr = map(int,raw_input().strip().split())

# using these 2 lines (and .keys() below) yields 49.392 seconds
#furthest_cover = {}
#coverage_arr   = {}
# using these 2 lines yields 53.577 seconds
#furthest_cover = array.array('I', [0]*num_cities)
#coverage_arr   = array.array('I', [0]*num_cities)

# using these 2 lines yields 37.034 seconds
furthest_cover = [None] * num_cities
coverage_arr = [0] * num_cities

def get_ledge(idx):
    ledge = idx-tower_range
    if ledge < 0: 
        ledge = 0
    return ledge

maxidx = num_cities - 1
def get_redge(idx):
    redge = idx+tower_range
    if redge > maxidx:
        redge = maxidx
    return redge

def assign_coverage(iidx, idx):
    coverage_arr[iidx] = 1
    furthest_cover[iidx] = idx

def coverage():
    for idx in xrange(num_cities):
        if tower_presence_arr[idx] == 1:
            ledge = get_ledge(idx)
            redge = get_redge(idx)
            iidx = ledge
            while iidx <= redge:
                #assign_coverage(iidx, idx)
                coverage_arr[iidx] = 1
                furthest_cover[iidx] = idx
                iidx += 1

def early_exit():
    # first look for unsolvable and immediately bail
    #if 0 in coverage_arr.keys():
    if 0 in coverage_arr:
        print "-1"
        sys.exit(0)

def final_coverage():
    final_coverage = []
    current_tower = None
    for idx in xrange(num_cities):
        if current_tower is None:
            current_tower = furthest_cover[idx]
        if (idx - current_tower) <= tower_range:
            continue
        else:
            current_tower = furthest_cover[idx]
            final_coverage.append(current_tower)
    print len(final_coverage) + 1

def main():
    coverage()
    early_exit()
    final_coverage()

main()
#import cProfile
#cProfile.run('main()')
