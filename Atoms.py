C = input("Enter chemical compound : ")
elements = []
c = ""
D = {}
C = C + " "
for i in range(len(C)):
    if(C[i].islower()):
        elements.append(C[i-1]+C[i])
        elements.remove(C[i-1])
    else:
        elements.append(C[i])
        if(C[i].isdigit() and C[i-1].isdigit()):
            elements.append(C[i-1]+C[i])
            del elements[i-1]
            del elements[i-1]

for j in elements:
    if(j.isalpha()):
        D[j] = 0

for k in range(len(elements)-1, -1, -1):
    mul = None
    if(elements[k] == ")"):
        m = k-1
        P =""
        while(True):
            if(elements[m]=="("):
                break
            if(elements[m].isdigit()):
                mul = int(elements[m])*int(elements[k+1])
                D[elements[m-1]]+=mul
            elif(elements[m].isalpha() and (elements[m+1].isdigit()==False)):
                D[elements[m]]+=int(elements[k+1])
            m-=1
if("(" in elements):
    for k2 in range(len(elements)-1, -1, -1):
        if(elements[k2] == ")"):
            break
        if(elements[k2].isdigit() and (elements[k2-1].isdigit() or elements[k2-1].isalpha())):
            D[elements[k2-1]]+=int(elements[k2])
        elif(elements[k2].isalpha() and elements[k2+1].isalpha()):
            D[elements[k2]]+=1
for k3 in range(len(elements)):
    if(elements[k3] == "("):
        break
    if(elements[k3].isalpha() and elements[k3+1].isdigit()):
        D[elements[k3]]+=int(elements[k3+1])
    elif(elements[k3].isalpha() and (elements[k3+1].isdigit()==False)):
        D[elements[k3]]+= 1

newL = []
for f in D:
    newL.append(f+str(D[f]))
newL = sorted(newL)
print("".join(newL))
