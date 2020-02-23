print "Hello World !"

print "n = ",
n=input()

F0 = 0
F1 = 1

print "n = 0"
print "F0 =",
print(F0)

print "n=1"
print "F1 =",
print (F1)


for i in range(2, n):
	Fn = F0 + F1
	print "n = ",
	print(i)
	print "F",
	print (i),
	print "=",
	print(Fn)
	F0=F1
	F1=Fn
	if Fn > 1:
		for x in range(2,Fn):
			if(Fn % x) == 0:
				break
		else:
			print(Fn),
			print "prime number"


	
