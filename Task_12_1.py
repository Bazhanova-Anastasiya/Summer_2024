X = [1,2,3,4,1,2,3,4,1,4]
lmin = []
lmax = []
def min_ind_and_max_ind(X):
    for k,v in enumerate(X):
        #print(f'k = {k} v = {v}')
        if v == min(X):
            lmin.append(k)
        elif v == max(X):
            lmax.append(k)
    return lmin, lmax

print(*min_ind_and_max_ind(X))

