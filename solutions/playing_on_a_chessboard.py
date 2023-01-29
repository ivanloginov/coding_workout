def game(n):
    denum = 2*(n%2!=0) + (n%2==0)
    num = n/2*(n)*denum
    res = [num]
    if denum!=1:
        res.append(denum)
    return res