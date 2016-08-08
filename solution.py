import sys
num_cities, tower_range = map(int,raw_input().strip().split())
tower_range -= 1
tower_presence_arr = map(int,raw_input().strip().split())

who_covers = []
coverage_arr = []
def setup():
    for idx in range(num_cities):
        coverage_arr.append(0)
        who_covers.append([])

def coverage():
    maxidx = len(coverage_arr)-1
    for idx in range(num_cities):
        if tower_presence_arr[idx] == 1:
            #ledge = max(0, idx-tower_range)
            ledge = idx-tower_range
            if ledge < 0: 
                ledge = 0
            #redge = min(len(coverage_arr)-1, idx+tower_range)
            redge = idx+tower_range
            if redge > maxidx:
                redge = maxidx
            iidx = ledge
            while iidx <= redge:
                coverage_arr[iidx] += 1
                who_covers[iidx].append(idx)
                iidx += 1

def early_exit():
    # first look for unsolvable and immediately bail
    if 0 in coverage_arr:
        print "-1"
        sys.exit(0)

def final_coverage():
    final_coverage = []
    current_tower = None
    for idx in range(num_cities):
        if current_tower in who_covers[idx]:
            continue
        else:
            current_tower = max(who_covers[idx])
            final_coverage.append(current_tower)
    print len(final_coverage)

def main():
    setup()
    coverage()
    early_exit()
    final_coverage()

#main()
import cProfile
cProfile.run('main()')
#import pstats
#p = pstats.Stats('stats.txt')
#p.sort_stats('time')
#p.print_stats()
