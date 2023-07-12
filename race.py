from turtle import Turtle,Screen
import random
a=Turtle(shape="turtle")
b=Turtle(shape="turtle")
c=Turtle(shape="turtle")
score=Turtle(shape="turtle")
e=Turtle(shape="turtle")
f=Turtle(shape="turtle")
color=["red","green","blue","cyan","magenta","yellow"]
def randomcolor():
    co=random.choice(color)
    color.remove(co)
    return co
p=randomcolor()
q=randomcolor()
s=randomcolor()
t=randomcolor()
u=randomcolor()
v=randomcolor()
a.color(p)
b.color(q)
c.color(s)
score.color(t)
e.color(u)
f.color(v)
s=Screen()
s.setup(width=500,height=400)
w=s.textinput(title="Make a bet",prompt='Which turtle will win the race?("red","green","blue","cyan","magenta","yellow"').lower()
a.penup()
b.penup()
c.penup()
score.penup()
e.penup()
f.penup()
a.goto(y=-150, x=-400)
b.goto(y=-100, x=-400)
c.goto(y=-50, x=-400)
score.goto(y=0, x=-400)
e.goto(y=50,x=-400)
f.goto(y=100,x=-400)
def race(a):
    if w:
        r=random.randint(0,10)
        a.fd(r)
turtlerace=True
while turtlerace:
    race(a)
    race(b)
    race(c)
    race(score)
    race(e)
    race(f)
    if a.pos()>(250,-150):
        turtlerace=False
        if p==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {p}")
    if b.pos()>(250,-100):
        turtlerace=False
        if q==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {q}")
    if c.pos()>(250,-50):
        turtlerace=False
        if s==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {s}")
    if score.pos()>(250, 0):
        turtlerace=False
        if t==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {t}")
    if e.pos()>(250,50):
        turtlerace=False
        if u==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {u}")
    if f.pos()==(250,100):
        turtlerace=False
        if v==w:
            print("Your guess was correct. You win the bet")
        else:
            print(f"You lose. The winner was {v}")
s.exitonclick()
