import turtle as T
import random

colors = ["red", 
          "blue",
          "green",
          "purple",
          "yellow",
          "orange",
          "pink",
          "black"]

T.speed(5)

counter = 0

while counter < 36:
    color = random.randint(0, 7)
    T.color(colors[color])
    for _ in range(4):
        T.forward(100)
        T.right(90)
    T.right(10)
    counter += 1

T.exitonclick()