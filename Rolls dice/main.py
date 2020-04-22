import random 

nbR = 150
Nb_Min = 1
Nb_Max = 6

stats = [0,0,0,0,0,0]
#or stats = [0]*6

for k in range(nbR): 

	dice = random.randint(Nb_Min,Nb_Max #choose a real number ∈ [Nb_Min;Nb_Max]

	stats[dice-1] = stats[dice-1]+1 


print(stats)

for k in range(6):
	print(stats[k], "% of",k+1) 
