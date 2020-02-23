aa = input(" a = ")
a = int(aa)
bb = input(" b = ")
b = int(bb)
cc = input(" c = ")
c = int(cc)

ddd = input(" d = ")
dd = int(ddd)
eee = input(" e = ")
ee = int(eee)
fff = input(" f = ")
ff = float(fff)






def f(x):                           #Intitialize our function
	return a*x**3-b*x**2+c


#the algorithm 
def dichotomy(d,e,f):        #d & e : the extremities of the interval. f : the accuracy        

	while e-d>f:
		m=(d+e)/2
		if f(d)*f(m)<=0:
			e=m
		else:
			d=m
	return (d,e)

print(dichotomy(dd, ee, ff))
