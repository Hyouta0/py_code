#LaneSimple = ["L0","L1","L2"]


#def laneTraverse(lane,size,lvl):
#    if(lvl == size):
#        return 
#    print(lane[lvl])
#    laneTraverse(lane,size,lvl+1);

#size = len(LaneSimple)
#laneTraverse(LaneSimple,size,0);


lanePlane = ["L0","L1",["L2L0","L2L1","L2L2","L2L3"],\
        "L3",[["L4L0","L4L1","L4L2"],\
        ["L4R0"]],"L5","L6","L7","L8"];

def laneTraversel(lane):
    for ad in lane: 
        #print(type(ad));
        if(type(ad) == list):
            laneTraversel(ad);
        else:
            print(ad);


laneTraversel(lanePlane);
