"""
i=0
while(i<=100):
    print(i)
    i=i+1

______________________________________________________________________________    

while(true):
    print("true")
   # op is infinete true

_________________________________________________________________________________
                                      question's
    print the number from 1 to 5 using while loop                                  
 
i=1
while(i<=5):
    print(i)
    i=i+1
______________________________________________________________________________
 print following series 10,20,30,40,50,60,....200
 
i=10
while(i<=200):
    print(i,end=",")
    i=i+10

 ___________________________________________________________________________
write a program to print first 10 natural numbers in reverse order
10,9,8,7,6,5,4,3,2,1

i=10
while(i>=1):
    print(i,end=",")
    i=i-1
____________________________________________________________________________
to find the factorial of a number
"""

i=int(input("num:"))
fact=1
while(i>0):
  fact=fact*i
  i=i-1
print(fact)
