def solution(a, b):
    swapped=0
    swapped_idx=-1
    other_swap=-1
    swapped_vala=-1
    swapped_valb=-1
    sa=set(a)
    sb=set(b)
    for i in range(len(a)):
        if a[i]!=b[i]:
            if swapped==1:
                if other_swap!=-1 or b[i]!=swapped_vala or a[i]!=swapped_valb:
                    return False
                else:
                    other_swap=i
            elif a[i] in sb:
                swapped_vala=a[i]
                swapped_valb=b[i]
                swapped=1
            else:
                return False
    return True