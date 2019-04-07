import collections
s = input().strip()
d = collections.Counter(s)
new = []
for j in d:
    new.append(d[j])

flag = ""
new.sort()
m = max(new)
mini = min(new)
set = set(new)

maxCount = new.count(m)
for c in new:
    if(c!=m):
        otherCount = new.count(c)
        break

if(len(set)==1):
    print("YES")
elif(len(set)==2 and (otherCount==1 or maxCount==1)):
    for k in new:
        if(k!=m):
            if(m-k==1 or k-m==1):
                flag = 'Green'
        break
    else:
        flag = 'Red'
    if(mini == 1 and new.count(mini)==1):
        print("YES")
    else:
        if(flag == 'Green'):
            print("YES")
        else:
            print("NO")
else:
    print("NO")
