a = "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?1234567890!@#$%^&*()-=_+`~ " + '"' 
mass = []
chore = 0
def brute(a,st,pl,numb):
	global chore
	st += pl
	if len(st) != numb:
		for i in a:
			brute(a,st,i,numb)
	else:
		#print(st)
		chore +=1

for i in range(len(a)):
	mass.append(a[i])

for i in range(2):
	brute(a,'','',i)
print("Altogether:",chore)

