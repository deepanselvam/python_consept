"""
class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoyment the beach")
ramesh = goa() # it is know as ramesh is able to acces party and beach in goa
suresh = goa() # it is know as suresh is able to acces party and beach in goa
ramesh.party()# rames can able to acces anyone but ramesh whant only party
suresh.beach()
_________________________________________________________________________



class goa:
    name="ghdrrf" #ramesh is stored
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoyment the beach")
ramesh = goa() 
suresh = goa()
ramesh.name="ramesh" #ramesh is stored in the name variable in goa class
suresh.name="suresh"
ramesh.drink="yes"   #yes is tored in drink variable in goa class
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
ramesh.party() #function call

print(suresh.name)
print("drink:",suresh.drink)
suresh.beach() #function call
_______________________________________________________________________________
create class called laptop
create following variable and functions
variable=> price,processor,ram
creat object hp,dell,lenova
___________________________________________________________________________-
class laptop:
    price=""
    proc=""
    ram=""
hp=laptop()
dell=laptop()

hp.price="1000"
hp.proc="i5"
hp.ram="4GB"

dell.price="10000"
dell.proc="i5"
dell.ram="6GB"
print(hp.price)
print(dell.price)

__________________________________________________________________________
                       BIKE SPECIFICATION

class bike:
    price=""
    color=""
    model=""
re350=bike()
re500=bike()
re800=bike()

re350.price="1.5L,2.5L,4.5L"
re350.color="black,borun,blue"
re350.model="2020,2022,2023"
    
re500.price="3.5L,4.5L,5.5L"
re500.color="black,borun,blue"
re500.model="2020,2022,2023"
    
re800.price="4.5L,5.5L,6.5L"
re800.color="black,borun,blue"
re800.model="2020,2022,2023"

print(re350.price)

class bike:
    name=""
    def re350(self):
        print("price = 1.5L,2.5L,4.5L")
       

    def re500(self):
        print("price = 2.5L,3.5L,4.5L")

    def re800(self):
       print("price = 3.5L,4.5L,5.5L")

ramesh=bike()
ramesh.name="350"
print(ramesh.name)
ramesh.re350()

___________________________________________________________
class laptop:            # __INIT__ IS KNOWN AS CONTRUCTOR
    def __init__(self): #__init__ is python inbuild function
        print("deepan")  # if not call the functio but it take automaticaly
    def display(self):
         print("display")
         
hp=laptop()#object created named as hp

____________________________________________________________

class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.proc=""
    def display(self):
         print("price:",self.price)
         print("proc:",self.proc)
         print("ram:",self.ram)

hp=laptop()
hp.pric=20000
hp.ram="8gb"
hp.proc="i5"
print(hp.ram)
hp.display()
______________________________________________________________
"""
import turtle
from turtle import*

wn = Screen()
wn.setup(width=1200,height=680)
t= Turtle()
wn.bgcolor('black')
t.speed(-1)
colors =['white','red']

for i in range(180):
    t.pencolor(colors[i%len(colors)])
    t.rt(i)
    t.circle(100,i)
    t.fd(i)
    t.rt(180)
    t.fd(i)

wn.mainloop()
"""________________________________________________


import math
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)
speed(100000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()


"""
