ask3=open("ask3.txt","r")

#diavazei tis grammes
grammes=ask3.readlines()

for grammi in grammes:
	if "#" in grammi:
		l=grammi.strip()
#elegxos an arxizei apo #
		if l[0]!="#":
#xwrizei tin grammi
			tmp=grammi.split("#")
#metraei to plithos twn (' " ) pou proigounte
			aftakia1=tmp[0].count("'")
			aftakia2=tmp[0].count('"')
#elegxos gia ta aftakia an einai monos arithmos sinepagete oti einai mesa se protasi
			if aftakia1%2==1 or aftakia2%2==1:
				print grammi
			else:
				print grammi.split("#")[0]
	else:
		print grammi
ask3.close()

