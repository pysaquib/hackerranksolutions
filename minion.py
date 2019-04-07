S = input("Enter string : ")
S = S.upper()
kevin, stuart = 0, 0
vowel = ['A', 'E', 'I', 'O', 'U']
i = 0
while(i<len(S)):
    if(S[i] in vowel):
        kevin+= (len(S)-i)
    else:
        stuart+= (len(S)-i)
    i+=1

if(kevin>stuart):
    print("Kevin "+str(kevin))
elif(stuart>kevin):
    print("Stuart "+str(stuart))
else:
    print("Draw")
