n=raw_input("Enter 1st string\n")
m=raw_input("Enter 2nd string\n")
s=0
if len(n)<=len(m):
    s=len(n)
else:
    s=len(m)
ans=""
for i in range(s):
    ans+=n[i]
    ans+=m[i]
if len(n)<len(m):
    ans+=m[i+1:]
else:
    ans+=n[i+1:]
print(ans)
