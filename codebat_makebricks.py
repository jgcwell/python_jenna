def make_bricks(small, big, goal):
    print "big 1x5: ", big, " small 1x1: ", small, " goal: ", goal
    if goal == 0:
        works = True
    else: 
        works = False
        if big > 0 and goal > 0:
            works = make_bricks(small, big-1, goal-5)
            if works:
                return works
        if small > 0 and goal > 0:
            works = make_bricks(small-1, big, goal-1)
    print "works? ", works
    return works
    
make_bricks(1,1,5)