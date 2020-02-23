def f(x):
	return x**3-6*x**2+6

def dichotomie(a,b,e):

	while b-a>e:
		m=(a+b)/2

		if f(a)*f(m)<=0:
			b=m
		else: 
			a=m

	return(a,b)

print(dichotomie(1,2,1E-3))
