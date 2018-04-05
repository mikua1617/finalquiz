def uniqueValues(aDict):
    L1=[]
    dict_cpy=aDict.copy()
    for keys in aDict:
        counter=0
        for vals in aDict.values():
            if aDict[keys]==vals:
                counter+=1
        if counter==1:
            L1.append(keys)

    return L1
