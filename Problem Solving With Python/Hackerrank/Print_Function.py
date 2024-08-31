def fun(n):
    ans = ""
    for i in range(1,n+1):
        if i == n:
            ans += str(i)
        else:
            ans += str(i) 
    print(ans)

n = int(input())
fun(n)       