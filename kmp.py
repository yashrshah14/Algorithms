def computeLPS(p,p_len,lps):
    length=0
    i=1
    while(i<p_len):
        if p[i]==p[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1


s=raw_input("Enter the string")
p=raw_input("Enter the pattern")
s_len=len(s)
p_len=len(p)
lps=[0]*p_len
j=0
computeLPS(p,p_len,lps)
i=0
while i<s_len:
    if p[j]==s[i]:
        i+=1
        j+=1
    if j==p_len:
        print("Found pattern at index:",str(i-j))
        j=lps[j-1]
    elif(i<s_len and p[j]!=s[i]):
         if (j!=0):
             j=lps[j-1]
         else:
             i+=1
         
        
            
            
    
