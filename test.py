lis=[]
def n_digit(num,n):
    return (num//10**(n-1))%10
def test(l,r,n,num = 0):
    if n==1:
        for i in range(n_digit(l,1),n_digit(r,1)+1):
            lis.append(num*10+i)
        return 0
    for i in range(n_digit(l,n),n_digit(r,n)+1):
        test(l,r,n-1,num*10+i)


