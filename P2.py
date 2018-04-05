def longestRun(L):
    counter=1
    flag=0
    for looper in range(len(L)-1):
        if L[looper] > L[looper+1]:
            max_len=counter
            counter=1
            flag=1
        else:
            counter+=1

    if flag!=1:
        max_len=counter

    return max_len
        
