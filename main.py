n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    cmd,j=input().split()
    a2=set(map(int,input().split()))
    if cmd=="intersection_update":
        a.intersection_update(a2)
    elif cmd=="symmetric_difference_update":
        a.symmetric_difference_update(a2)
    elif cmd=="update":
        a.update(a2)
    elif cmd=="difference_update":
        a.difference_update(a2)
print(sum(a))
