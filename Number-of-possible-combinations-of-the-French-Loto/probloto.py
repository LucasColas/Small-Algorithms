#dresse toutes les combinaisons possibles

from itertools import combinations
 
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]


n = 1
 
for y in combinations(x, 5):
    print(y),
    print(n)

    n = n+1
    if (n == 1000001):
     print "Keanu Reeves forever"

    if (n == 500001):
    	print "YODA !"

    




#donne le nombre total de combinaisons

def fact(n):

    if n<2:
        return 1
    else:
        return n*fact(n-1)
 

g = fact(49)//(fact(49-5)*fact(5))
print(g)