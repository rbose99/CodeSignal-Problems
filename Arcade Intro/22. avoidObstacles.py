def solution(inputArray):
    if len(inputArray)==0:
        return 1
    ob=sorted(inputArray)
    jump=2
    collide=True
    while(collide):  
        collide=False
        for i in range(len(ob)):
            if ob[i] % jump == 0:
                collide=True
                break
        jump+=1
    return jump-1

