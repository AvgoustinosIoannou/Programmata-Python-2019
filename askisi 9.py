def maxsequence(list):
#arxikopioisi
    max=0
    z=0
    sublist = []
    while(1):
        for i in range(len(list)):
            sum = 0
#vriskei ola ta sinexomena pithana athroismata
            for j in range(i+1-z):
                sum = list[j-1+z] + sum
#max pairnei tin timi tou megaliterou sum
                if(sum>max):
                    max=sum
                    sublist.append(list[j - 1 + z])
        z+=1
        if(z==len(list)):
            break
#epistrefei to max kai ti lista pou ta stoixeia to apoteloun
    return max,sublist
list=[]
while (1):
    a= raw_input("dwse num:")
    if(a=="exit"):
        break
    else:
        list.append(int(a))
b= maxsequence(list)
print b