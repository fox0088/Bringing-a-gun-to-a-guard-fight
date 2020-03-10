from math import hypot,atan2

def solution(dimensions, your_position, guard_position, distance):
    ypx=your_position[0]
    ypy=your_position[1]
    yp_list=[]
    gp_list=[]
    targetCnt=0
    angle_n_dist=dict()
    yp_list=matrix(dimensions, your_position, distance)
    gp_list=matrix(dimensions, guard_position, distance)

    for i in range(len(yp_list)):
        x=yp_list[i][0]-ypx
        y=yp_list[i][1]-ypy
        hyp=hypot(x,y)
        if hyp<=distance:
            atan=atan2(x,y)
            if atan not in angle_n_dist: angle_n_dist[atan]=hyp
        x=gp_list[i][0]-ypx
        y=gp_list[i][1]-ypy
        hyp=hypot(x,y)
        if hyp<=distance:
            atan=atan2(x,y)
            if atan not in angle_n_dist or hyp<=angle_n_dist[atan]:
                targetCnt+=1
                angle_n_dist[atan]=hyp
    return targetCnt

def matrix(room_size, position, distance):
    X,Y=position[0],position[1]
    arr,arrx,arry=[],[X],[Y]
    matX=distance//room_size[0]+2
    matY=distance//room_size[1]+2
    for i in range(1,matX):
        x2wall=room_size[0]*i-X
        x=X+2*x2wall
        arrx.append(x)
        X=x
    for i in range(1,matY):
        y2wall=room_size[1]*i-Y
        y=Y+2*y2wall
        arry.append(y)
        Y=y
    for i in arrx:
        for j in arry:
            arr+=[(i,-j)]+[(-i,j)]+[(-i,-j)]+[(i,j)]
    return arr

#[room size],[my position],[guard position],[max distance]    
print(solution([3,3], [1,1], [2,2], 5))
print(solution([300,275], [150,150], [185,100], 500))
print(solution([2,5],[1,2],[1,4],11))
print(solution([10,10],[4,4],[3,3],500))
