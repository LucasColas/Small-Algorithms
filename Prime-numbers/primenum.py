print "Hello World !"
print "Prime numbers up to : ",


interval = input()
x = 0
  
for number in range(2, interval): 
       
   if number > 1: 
       for n in range(2, number): 
           if (number % n) == 0: 
               break
       else: 
           x = x+1
           print(number), 
           print(x)


           


print "It's over !"
