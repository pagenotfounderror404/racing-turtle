from turtle import Turtle,Screen

t=Turtle()
s=Screen()
t.shape("turtle")

def forward():
    t.fd(20)
def backwards():
    t.bk(20)
def clockwise():
    t.right(20)
def anticlockwise():
    t.left(20)
def clear():
    s.reset()
s.listen()
s.onkey(key="w",fun=forward)
s.onkey(key="s",fun=backwards)
s.onkey(key="d",fun=clockwise)
s.onkey(key="a",fun=anticlockwise)
s.onkey(key="c", fun=clear)
s.exitonclick()
