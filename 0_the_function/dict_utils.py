def dict2list(dct, keylist) -> list[any]: return list(map(lambda i: dct[keylist[i]], range(len(keylist))))



def list2dict(L, keylist): return {x[0]: x[1] for x in zip(keylist, L)}

def  listrange2dict(L): return {k: v for k,v in zip(range(len(L)), L)}
