def genbin(n, bs=''):  
    if len(bs) == n:
        print(bs)
    else:
        genbin(n, bs + '0')
        genbin(n, bs + '1')
genbin(3)