
import turtle as a
import winsound
import random
import time
import pygame
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
sound_path_1 = os.path.join(current_dir, 'sound_c4', 'fall_sound_1.mp3')
sound_path_2 = os.path.join(current_dir, 'sound_c4', 'fall_sound_2.mp3')

pygame.mixer.init()
fall_sound_1 = pygame.mixer.Sound(sound_path_1)
fall_sound_2 = pygame.mixer.Sound(sound_path_2)


a.speed(10000000000000000000000000000000000000000000000000000000000000000000001)
a.ht()
a.tracer(0)
a.title('4 in a ROW')
#red / dark red
#yellow / gold
#dark gray / gray
#pink / hotpink
# lawngreen / limegreen
#skyblue1 / royalblue1
#darkorchid1 / purple
#white / white
#darkorange / orangered
#green / darkgreen
color_1 = "red"
color_1_dark = "dark red"
color_2 = "yellow"
color_2_dark = "gold"

color_c_1 = "red"
color_c_2 = "yellow"
red_won = 0
yellow_won = 0

def blank():
    a.color("blue")
    a.begin_fill()
    for k in range(4):
        a.forward(130)
        a.left(90)
    a.end_fill()
    a.forward(64)
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color("white")
    a.begin_fill()
    a.circle(55)
    a.end_fill()

def red():
    a.penup()
    a.forward(64)
    a.left(90)
    a.forward(10)
    a.right(90)
    a.pendown()
    a.color(color_1)
    a.begin_fill()
    a.circle(55)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_1_dark)
    a.begin_fill()
    a.circle(45)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_1)
    a.begin_fill()
    a.circle(35)
    a.end_fill()
    a.left(90)
    a.forward(25)
    a.right(90)
    a.color(color_1_dark)
    a.begin_fill()
    a.circle(10)
    a.end_fill()

def yellow():
    a.penup()
    a.forward(64)
    a.left(90)
    a.forward(10)
    a.right(90)
    a.pendown()
    a.color(color_2)
    a.begin_fill()
    a.circle(55)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_2_dark)
    a.begin_fill()
    a.circle(45)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_2)
    a.begin_fill()
    a.circle(35)
    a.end_fill()
    a.left(90)
    a.forward(25)
    a.right(90)
    a.color(color_2_dark)
    a.begin_fill()
    a.circle(10)
    a.end_fill()

def re(color_, color_1_dar):
    a.penup()
    a.forward(64)
    a.left(90)
    a.forward(10)
    a.right(90)
    a.pendown()
    a.color(color_)
    a.begin_fill()
    a.circle(55)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_1_dar)
    a.begin_fill()
    a.circle(45)
    a.end_fill()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.color(color_)
    a.begin_fill()
    a.circle(35)
    a.end_fill()
    a.left(90)
    a.forward(25)
    a.right(90)
    a.color(color_1_dar)
    a.begin_fill()
    a.circle(10)
    a.end_fill()
    
def start_screen():
    blank_spaces = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76]
    red_spaces = []
    yellow_spaces = []

    for item in red_spaces:
        red_spaces.remove(item)
    for item in yellow_spaces:
        yellow_spaces.remove(item)
        
    a.penup()
    a.goto(-445, 150)
    a.color("dark blue")
    a.write("4 IN A ROW", font =("Arial", 120, "bold"))
    a.color("blue")
    a.write("4 IN A ROW", font =("Arial", 120, "normal"))

    a.goto(-610, 90)
    a.pendown()
    a.color(color_1)
    a.begin_fill()
    a.circle(150)
    a.end_fill()
    a.color(color_1_dark)
    a.penup()
    a.goto(-610, 110)
    a.pendown()
    a.begin_fill()
    a.circle(130)
    a.end_fill()
    a.color(color_1)
    a.penup()
    a.goto(-610, 140)
    a.pendown()
    a.begin_fill()
    a.circle(100)
    a.end_fill()
    a.color(color_1_dark)
    a.penup()
    a.goto(-610, 220)
    a.pendown()
    a.begin_fill()
    a.circle(20)
    a.end_fill()
    a.penup()

    a.goto(600, 90)
    a.pendown()
    a.color(color_2)
    a.begin_fill()
    a.circle(150)
    a.end_fill()
    a.color(color_2_dark)
    a.penup()
    a.goto(600, 110)
    a.pendown()
    a.begin_fill()
    a.circle(130)
    a.end_fill()
    a.color(color_2)
    a.penup()
    a.goto(600, 140)
    a.pendown()
    a.begin_fill()
    a.circle(100)
    a.end_fill()
    a.color(color_2_dark)
    a.penup()
    a.goto(600, 220)
    a.pendown()
    a.begin_fill()
    a.circle(20)
    a.end_fill()
    a.penup()

    a.goto(-250, 0)
    a.pendown()
    a.color("dark blue")
    a.begin_fill()
    for k in range(2):
        a.forward(510)
        a.right(90)
        a.forward(150)
        a.right(90)
    a.end_fill()
    
    a.penup()    
    a.goto(-250, 0)
    a.pendown()
    a.color("blue")
    a.begin_fill()
    for k in range(2):
        a.forward(500)
        a.right(90)
        a.forward(150)
        a.right(90)
    a.end_fill()

    a.penup()
    a.goto(-220, -150)
    a.pendown()
    a.color("light gray")
    a.write("START", font =("Arial", 100, "bold"))
    a.color("white")
    a.write("START", font =("Arial", 100, "normal"))

    a.penup()
    a.goto(-150, -200)
    a.pendown()
    a.color("dark red")
    a.begin_fill()
    for k in range(2):
        a.forward(310)
        a.right(90)
        a.forward(100)
        a.right(90)
    a.end_fill()

    a.penup()
    a.goto(-150, -200)
    a.pendown()
    a.color("red")
    a.begin_fill()
    for k in range(2):
        a.forward(300)
        a.right(90)
        a.forward(100)
        a.right(90)
    a.end_fill()

    a.penup()
    a.goto(-120, -290)
    a.pendown()
    a.color("light gray")
    a.write("CLOSE", font =("Arial", 50, "bold"))
    a.color("white")
    a.write("CLOSE", font =("Arial", 50, "normal"))

    #
    a.penup()
    a.goto(510, -200)
    a.pendown()
    a.color("gray")
    a.begin_fill()
    for k in range(2):
        a.forward(100)
        a.right(90)
        a.forward(100)
        a.right(90)
    a.end_fill()
    
    a.penup()
    a.goto(500, -200)
    a.pendown()
    a.color("dark gray")
    a.begin_fill()
    for k in range(2):
        a.forward(100)
        a.right(90)
        a.forward(100)
        a.right(90)
    a.end_fill()
    
    a.penup()
    a.goto(516, -250)
    a.pendown()
    a.color("black")
    a.left(45)
    a.forward(45)
    a.left(90)
    a.pensize(10)
    a.circle(20, 180)
    a.circle(20, -180)
    a.right(90)
    a.pensize(5)
    a.backward(45)
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(60)
    a.end_fill()
    a.begin_fill()
    a.backward(10)
    a.right(90)
    a.forward(50)                                                                                                        
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()
    a.penup()
    a.goto(615, -220)
    a.pendown()
    a.color("red")
    a.begin_fill()
    for k in range(5):
        a.left(40)
        a.forward(15)
    a.circle(10)
    a.end_fill()
    a.penup()
    a.goto(625, -230)
    a.pendown()
    a.color("red")
    a.begin_fill()
    for k in range(5):
        a.left(40)
        a.forward(10)
    a.circle(10)
    a.end_fill()

        
box_min_x, box_max_x = -255, 255
box_min_y, box_max_y = -145, 0

def is_click_within_box(x, y):
    return box_min_x <= x <= box_max_x and box_min_y <= y <= box_max_y

end_min_x, end_max_x = -150, 170
end_min_y, end_max_y = -300, -130

def is_click_within_end(x, y):
    return end_min_x <= x <= end_max_x and end_min_y <= y <= end_max_y

paint_min_x, paint_max_x = 500, 600
paint_min_y, paint_max_y = -300, -180

def is_click_within_paint(x, y):
    return paint_min_x <= x <= paint_max_x and paint_min_y <= y <= paint_max_y

def on_click(x, y):
    if is_click_within_box(x, y):
       start_game()
    elif is_click_within_end(x, y):
       pygame.mixer.quit()
       exit()
    elif is_click_within_paint(x, y): 
       painting()
    else:
        ""
def red_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "red"
    color_1_dark = "dark red"

    color_c_1 = "red"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    
    return color_1, color_1_dark

def blue_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "skyblue1"
    color_1_dark = "royalblue1"

    color_c_1 = "skyblue1"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def purp_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "darkorchid1"
    color_1_dark = "purple"

    color_c_1 = "darkorchid1"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def pink_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "pink"
    color_1_dark = "hotpink"

    color_c_1 = "pink"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def dgrn_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "green"
    color_1_dark = "darkgreen"

    color_c_1 = "green"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def yellow_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "yellow"
    color_1_dark = "gold"

    color_c_1 = "yellow"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def grn_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "lawngreen"
    color_1_dark = "limegreen"

    color_c_1 = "lawngreen"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def orng_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "darkorange"
    color_1_dark = "orangered"

    color_c_1 = "darkorange"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def gray_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "darkgray"
    color_1_dark = "gray"

    color_c_1 = "darkgray"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

def whit_1():
    global color_1
    global color_1_dark
    global color_c_1
    
    color_1 = "white"
    color_1_dark = "white"

    color_c_1 = "white"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_1, color_1_dark

#

def red_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "red"
    color_2_dark = "dark red"

    color_c_2 = "red"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    
    return color_2, color_2_dark

def blue_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "skyblue1"
    color_2_dark = "royalblue1"

    color_c_2 = "skyblue1"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def purp_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "darkorchid1"
    color_2_dark = "purple"

    color_c_2 = "darkorchid1"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def pink_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "pink"
    color_2_dark = "hotpink"

    color_c_2 = "pink"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def dgrn_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "green"
    color_2_dark = "darkgreen"

    color_c_2 = "green"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def yellow_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "yellow"
    color_2_dark = "gold"

    color_c_2 = "yellow"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def grn_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "lawngreen"
    color_2_dark = "limegreen"

    color_c_2 = "lawngreen"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def orng_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "darkorange"
    color_2_dark = "orangered"

    color_c_2 = "darkorange"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def gray_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "darkgray"
    color_2_dark = "gray"
    color_c_2 = "darkgray" 

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def whit_2():
    global color_2
    global color_2_dark
    global color_c_2
    
    color_2 = "white"
    color_2_dark = "white"

    color_c_2 = "white"

    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    a.penup()
    a.pensize(170)
    a.color("blue")
    a.goto(-70, -1500)
    a.pendown()
    a.goto(-70, 1500)
    a.pensize(5)
    a.penup()
    a.pensize(130)
    a.color("blue")
    a.goto(65, -1500)
    a.pendown()
    a.goto(65, 1500)
    a.pensize(5)
    a.penup()
    a.goto(-475, 250)
    a.pendown()
    a.color(color_c_1) 
    a.write("P1", font =("Arial", 50, "bold"))
    a.penup()
    a.goto(375, 250)
    a.pendown()
    a.color(color_c_2)
    a.write("P2", font =("Arial", 50, "bold"))
    return color_2, color_2_dark

def painting():
    global color_1
    global color_1_dark
    global color_2
    global color_2_dark
    global color_c_1
    global color_c_2
    if color_1 == "red":
        red_1()
    elif color_1 =="skyblue1":
        blue_1()
    elif color_1 == "darkorchid1":
        purp_1()
    elif color_1 =="pink":
        pink_1()
    elif color_1 =="green":
        dgrn_1()
    elif color_1 =="yellow":
        yellow_1()
    elif color_1 =="lawngreen":
        grn_1()
    elif color_1 =="darkorange":
        orng_1()
    elif color_1 =="darkgray":
        gray_1()
    elif color_1 =="white":
        whit_1()
           
    #same just for p2

    if color_2 == "red":
        red_2()
    elif color_2 =="skyblue1":
        blue_2()
    elif color_2 == "darkorchid1":
        purp_2()
    elif color_2 =="pink":
        pink_2()
    elif color_2 =="green":
        dgrn_2()
    elif color_2 =="yellow":
        yellow_2()
    elif color_2 =="lawngreen":
        grn_2()
    elif color_2 =="darkorange":
        orng_2()
    elif color_2 =="darkgray":
        gray_2()
    elif color_2 =="white":
        whit_2()
        
    a.color("blue")
    a.penup()
    a.goto(-1000, 75)
    a.pendown()
    a.goto(1000, 75)
    a.penup()
    a.goto(-1000, -50)
    a.pendown()
    a.goto(1000, -50)
    a.penup()
    a.goto(-1000, -175)
    a.pendown()
    a.goto(1000, -175)
    a.penup()
    a.color("blue")
    a.goto(-655, -175)
    a.pendown()
    a.color("blue")
    a.goto(-655, 75)
    a.penup()
    a.color("blue")
    a.goto(-535, -175)
    a.pendown()
    a.color("blue")
    a.goto(-535, 75)
    a.penup()
    a.color("blue")
    a.goto(-405, -175)
    a.pendown()
    a.color("blue")
    a.goto(-405, 75)
    a.penup()
    a.color("blue")
    a.goto(-275, -175)
    a.pendown()
    a.color("blue")
    a.goto(-275, 75)
    a.penup()
    a.color("blue")
    a.goto(-145, -175)
    a.pendown()
    a.color("blue")
    a.goto(-145, 75)
    #
    a.penup()
    a.goto(250, -175)
    a.pendown()
    a.goto(250, 75)
    a.penup()
    a.goto(380, -175)
    a.pendown()
    a.goto(380, 75)
    a.penup()
    a.goto(510, -175)
    a.pendown()
    a.goto(510, 75)
    a.penup()
    a.goto(640, -175)
    a.pendown()
    a.goto(640, 75)
    a.penup()
    a.goto(770, -175)
    a.pendown()
    a.goto(770, 75)
    #

    a.penup()
    a.goto(-785, -50)
    a.pendown()
    re("red", "dark red")
    a.penup()
    a.goto(-785, -175)
    a.pendown()
    re("yellow", "gold")
    a.penup()
    a.goto(-659, -50)
    a.pendown()
    re("skyblue1", "royalblue1")
    a.penup()
    a.goto(-659, -175)
    a.pendown()
    re("lawngreen", "limegreen")
    a.penup()
    a.goto(-531, -50)
    a.pendown()
    re("darkorchid1", "purple")
    a.penup()
    a.goto(-531, -175)
    a.pendown()
    re("darkorange", "orangered")
    a.penup()
    a.goto(-402, -50)
    a.pendown()
    re("pink", "hotpink")
    a.penup()
    a.goto(-402, -175)
    a.pendown()
    re("dark gray", "gray")
    a.penup()
    a.goto(-278, -50)
    a.pendown()
    re("green", "darkgreen")
    #
    a.penup()
    a.goto(125, -50)
    a.pendown()
    re("red", "dark red")
    a.penup()
    a.goto(125, -175)
    a.pendown()
    re("yellow", "gold")
    a.penup()
    a.goto(249, -50)
    a.pendown()
    re("skyblue1", "royalblue1")
    a.penup()
    a.goto(249, -175)
    a.pendown()
    re("lawngreen", "limegreen")
    a.penup()
    a.goto(378, -50)
    a.pendown()
    re("darkorchid1", "purple")
    a.penup()
    a.goto(378, -175)
    a.pendown()
    re("darkorange", "orangered")
    a.penup()
    a.goto(510, -50)
    a.pendown()
    re("pink", "hotpink")
    a.penup()
    a.goto(510, -175)
    a.pendown()
    re("dark gray", "gray")
    a.penup()
    a.goto(637, -50)
    a.pendown()
    re("green", "darkgreen")
    a.color("green")
    a.color("white")
    a.penup()
    a.goto(-125, -15)
    a.pendown()
    a.write("FINISH", font =("Arial", 50, "bold"))
    #red / dark red
    #yellow / gold
    #dark gray / gray
    #pink / hotpink
    # lawngreen / limegreen
    #skyblue1 / royalblue1
    #darkorchid1 / purple
    #white / white
    #darkorange / orangered
    #green / darkgreen-785, -50
    finish_min_x, finish_max_x = -160, 125
    finish_min_y, finish_max_y = -100000000, 1000000000000

    def is_click_within_finish(x, y):
        return finish_min_x <= x <= finish_max_x and finish_min_y <= y <= finish_max_y
    
    red1_min_x, red1_max_x = -785, -655
    red1_min_y, red1_max_y = -50, 80

    def is_click_within_red1(x, y):
        return red1_min_x <= x <= red1_max_x and red1_min_y <= y <= red1_max_y

    blue1_min_x, blue1_max_x = -654, -524
    blue1_min_y, blue1_max_y = -50, 80

    def is_click_within_blue1(x, y):
        return blue1_min_x <= x <= blue1_max_x and blue1_min_y <= y <= blue1_max_y

    purp1_min_x, purp1_max_x = -524, -394
    purp1_min_y, purp1_max_y = -50, 80

    def is_click_within_purp1(x, y):
        return purp1_min_x <= x <= purp1_max_x and purp1_min_y <= y <= purp1_max_y
    
    pink1_min_x, pink1_max_x = -394, -264
    pink1_min_y, pink1_max_y = -50, 80

    def is_click_within_pink1(x, y):
        return pink1_min_x <= x <= pink1_max_x and pink1_min_y <= y <= pink1_max_y

    dgrn1_min_x, dgrn1_max_x = -264, -134
    dgrn1_min_y, dgrn1_max_y = -50, 80

    def is_click_within_dgrn1(x, y):
        return dgrn1_min_x <= x <= dgrn1_max_x and dgrn1_min_y <= y <= dgrn1_max_y

    yellow1_min_x, yellow1_max_x = -785, -655
    yellow1_min_y, yellow1_max_y = -180, -50

    def is_click_within_yellow1(x, y):
        return yellow1_min_x <= x <= yellow1_max_x and yellow1_min_y <= y <= yellow1_max_y

    grn1_min_x, grn1_max_x = -655, -525
    grn1_min_y, grn1_max_y = -180, -50

    def is_click_within_grn1(x, y):
        return grn1_min_x <= x <= grn1_max_x and grn1_min_y <= y <= grn1_max_y

    orng1_min_x, orng1_max_x = -525, -395
    orng1_min_y, orng1_max_y = -180, -50

    def is_click_within_orng1(x, y):
        return orng1_min_x <= x <= orng1_max_x and orng1_min_y <= y <= orng1_max_y

    gray1_min_x, gray1_max_x = -395, -265
    gray1_min_y, gray1_max_y = -180, -50

    def is_click_within_gray1(x, y):
        return gray1_min_x <= x <= gray1_max_x and gray1_min_y <= y <= gray1_max_y

    whit1_min_x, whit1_max_x = -265, -135
    whit1_min_y, whit1_max_y = -180, -50

    def is_click_within_whit1(x, y):
        return whit1_min_x <= x <= whit1_max_x and whit1_min_y <= y <= whit1_max_y

    #

    red2_min_x, red2_max_x = 125, 235
    red2_min_y, red2_max_y = -50, 80

    def is_click_within_red2(x, y):
        return red2_min_x <= x <= red2_max_x and red2_min_y <= y <= red2_max_y

    blue2_min_x, blue2_max_x = 235, 365
    blue2_min_y, blue2_max_y = -50, 80

    def is_click_within_blue2(x, y):
        return blue2_min_x <= x <= blue2_max_x and blue2_min_y <= y <= blue2_max_y

    purp2_min_x, purp2_max_x = 365, 495
    purp2_min_y, purp2_max_y = -50, 80

    def is_click_within_purp2(x, y):
        return purp2_min_x <= x <= purp2_max_x and purp2_min_y <= y <= purp2_max_y
    
    pink2_min_x, pink2_max_x = 495, 625
    pink2_min_y, pink2_max_y = -50, 80

    def is_click_within_pink2(x, y):
        return pink2_min_x <= x <= pink2_max_x and pink2_min_y <= y <= pink2_max_y

    dgrn2_min_x, dgrn2_max_x = 625, 755
    dgrn2_min_y, dgrn2_max_y = -50, 80

    def is_click_within_dgrn2(x, y):
        return dgrn2_min_x <= x <= dgrn2_max_x and dgrn2_min_y <= y <= dgrn2_max_y

    yellow2_min_x, yellow2_max_x = 125, 235
    yellow2_min_y, yellow2_max_y = -180, -50

    def is_click_within_yellow2(x, y):
        return yellow2_min_x <= x <= yellow2_max_x and yellow2_min_y <= y <= yellow2_max_y

    grn2_min_x, grn2_max_x = 235, 365
    grn2_min_y, grn2_max_y = -180, -50

    def is_click_within_grn2(x, y):
        return grn2_min_x <= x <= grn2_max_x and grn2_min_y <= y <= grn2_max_y

    orng2_min_x, orng2_max_x = 365, 495
    orng2_min_y, orng2_max_y = -180, -50

    def is_click_within_orng2(x, y):
        return orng2_min_x <= x <= orng2_max_x and orng2_min_y <= y <= orng2_max_y

    gray2_min_x, gray2_max_x = 495, 625
    gray2_min_y, gray2_max_y = -180, -50

    def is_click_within_gray2(x, y):
        return gray2_min_x <= x <= gray2_max_x and gray2_min_y <= y <= gray2_max_y

    whit2_min_x, whit2_max_x = 625, 755
    whit2_min_y, whit2_max_y = -180, -50

    def is_click_within_whit2(x, y):
        return whit2_min_x <= x <= whit2_max_x and whit2_min_y <= y <= whit2_max_y
        
    def on_click_paint(x, y):
      if is_click_within_finish(x, y):
            a.reset()
            a.speed(100000000000000000000000000000000000000000000000000000000000001)
            a.ht()
            a.tracer(0)
            start_screen()
            a.onscreenclick(on_click)
            a.done()
      elif is_click_within_red1(x, y):
             color_1 = "red"
             color_1_dark = "dark red"
             red_1()
             painting()
      elif is_click_within_blue1(x, y):
             color_1 = "skyblue1"
             color_1_dark = "royalblue1"
             blue_1()
             painting()
      elif is_click_within_purp1(x, y):
             color_1 = "darkorchid1"
             color_1_dark = "purple"
             purp_1()
             painting()
      elif is_click_within_pink1(x, y):
             color_1 = "pink"
             color_1_dark = "hotpink"
             pink_1()
             painting()
      elif is_click_within_dgrn1(x, y):
             color_1 = "green"
             color_1_dark = "darkgreen"
             dgrn_1()
             painting()
      elif is_click_within_yellow1(x, y):
             color_1 = "yellow"
             color_1_dark = "gold"
             yellow_1()
             painting()
      elif is_click_within_grn1(x, y):
             color_1 = "lawngreen"
             color_1_dark = "limegreen"
             grn_1()
             painting()
      elif is_click_within_orng1(x, y):
             color_1 = "darkorange"
             color_1_dark = "orangered"
             orng_1()
             painting()
      elif is_click_within_gray1(x, y):
             color_1 = "darkgray"
             color_1_dark = "gray"
             gray_1()
             painting()
      elif is_click_within_whit1(x, y):
             color_1 = "white"
             color_1_dark = "white"
             whit_1()
             painting()
    #
      elif is_click_within_red2(x, y):
             color_2 = "red"
             color_2_dark = "dark red"
             red_2()
             painting()
      elif is_click_within_blue2(x, y):
             color_2 = "skyblue1"
             color_2_dark = "royalblue1"
             blue_2()
             painting()
      elif is_click_within_purp2(x, y):
             color_2 = "darkorchid1"
             color_2_dark = "purple"
             purp_2()
             painting()
      elif is_click_within_pink2(x, y):
             color_2 = "pink"
             color_2_dark = "hotpink"
             pink_2()
             painting()
      elif is_click_within_dgrn2(x, y):
             color_2 = "green"
             color_2_dark = "darkgreen"
             dgrn_2()
             painting()
      elif is_click_within_yellow2(x, y):
             color_2 = "yellow"
             color_2_dark = "gold"
             yellow_2()
             painting()
      elif is_click_within_grn2(x, y):
             color_2 = "lawngreen"
             color_2_dark = "limegreen"
             grn_2()
             painting()
      elif is_click_within_orng2(x, y):
             color_2 = "darkorange"
             color_2_dark = "orangered"
             orng_2()
             painting()
      elif is_click_within_gray2(x, y):
             color_2 = "darkgray"
             color_2_dark = "gray"
             gray_2()
             painting()
      elif is_click_within_whit2(x, y):
             color_2 = "white"
             color_2_dark = "white"
             whit_2()
             painting()
      else:
            painting()
            
    a.onscreenclick(on_click_paint)

    a.done()
    
def start_game():
    a.reset()
    a.speed(100000000000000000000000000000000000000000000000000000000000001)
    a.ht()
    a.tracer(0)
    blank_spaces = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76]
    red_spaces = []
    yellow_spaces = []

    the_x = -585
    number = 7

    for k in range(7):
        number += 5
        the_y = -385
        the_x += 130
        number -= 1
        for k in range(6):
            
                a.penup()
                a.goto(the_x, the_y)
                a.pendown()

                blank()

                number += 1
                the_y += 130

    a.penup()
    a.goto(-700, -200)
    a.color(color_1)
    a.pendown()
    for k in range(2):
        a.forward(80)
        a.left(90)
        a.forward(80)
        a.left(90)
    a.forward(17)
    a.write(f"{red_won}", font =("Arial", 60, "bold"))

    a.penup()
    a.goto(-615, -200)
    a.color(color_2)
    a.pendown()
    for k in range(2):
        a.forward(80)
        a.left(90)
        a.forward(80)
        a.left(90)
    a.forward(17)
    a.write(f"{yellow_won}", font =("Arial", 60, "bold"))

    a.penup()
    a.goto(-690, -110)
    a.pendown()
    a.color("black")
    a.write(f"WINS", font =("Arial", 40, "normal"))

    
    a.penup()
    a.goto(550, -395)
    a.left(60)
    a.pensize(30)
    a.color("gray")
    a.pendown()
    a.forward(250)
    a.right(60)
    a.pensize(1)

    blank_spaces = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76]
    for item in red_spaces:
        red_spaces.remove(item)
    for item in yellow_spaces:
        yellow_spaces.remove(item)
        
    choosing_line()
    



def choosing_line():
        global the_line

            
        a.onscreenclick(None)
        the_line = 0
        if turn_red == 1:
            a.penup()
            a.goto(550, -395)
            a.left(60)
            a.pensize(30)
            a.forward(250)
            a.pensize(1)
            a.right(240)
            a.pendown()
            a.color(color_1)
            a.begin_fill()
            a.right(30)
            a.forward(150)
            a.left(90)
            a.forward(100)
            a.left(90)
            a.forward(130)
            a.left(30)
            a.forward(80)
            a.end_fill()
            a.setheading(0)
        elif turn_yellow == 1:
            a.penup()
            a.goto(550, -395)
            a.left(60)
            a.pensize(30)
            a.forward(250)
            a.pensize(1)
            a.right(240)
            a.pendown()
            a.color(color_2)
            a.begin_fill()
            a.right(30)
            a.forward(150)
            a.left(90)
            a.forward(100)
            a.left(90)
            a.forward(130)
            a.left(30)
            a.forward(80)
            a.end_fill()
            a.setheading(0)

        one_min_x, one_max_x = -455, -325
        def is_click_within_1(x, y): 
                        return one_min_x <= x <= one_max_x and y == y

        two_min_x, two_max_x = -325, -195
        def is_click_within_2(x, y):
                        return two_min_x <= x <= two_max_x and y == y
                    
        three_min_x, three_max_x = -195, -65
        def is_click_within_3(x, y):
                        return three_min_x <= x <= three_max_x and y == y
                                
        four_min_x, four_max_x = -65, 75
        def is_click_within_4(x, y):
                        return four_min_x <= x <= four_max_x and y == y

        five_min_x, five_max_x = 75, 205
        def is_click_within_5(x, y):
                        return five_min_x <= x <= five_max_x and y == y

        six_min_x, six_max_x = 205, 335
        def is_click_within_6(x, y):
                        return six_min_x <= x <= six_max_x and y == y
                    
        seven_min_x, seven_max_x = 335, 465
        def is_click_within_7(x, y):
                        return seven_min_x <= x <= seven_max_x and y == y
                    
        def on_click_line(x, y):
                global the_line
                if is_click_within_1(x, y):
                           the_line = 1
                           drawing()
                elif is_click_within_2(x, y):
                           the_line = 2
                           drawing()
                elif is_click_within_3(x, y):
                           the_line = 3
                           drawing()
                elif is_click_within_4(x, y):
                           the_line = 4
                           drawing()
                elif is_click_within_5(x, y):
                           the_line = 5
                           drawing()
                elif is_click_within_6(x, y):
                           the_line = 6
                           drawing()
                elif is_click_within_7(x, y):
                           the_line = 7
                           drawing()
                        
                else:
                    ""
        a.onscreenclick(on_click_line)

        a.done()

def placing():
        global yellow_spaces  
        global red_spaces   
        global blank_spaces
        
        global line
        global high
        global still_felling
        global num 
        global stay

        global turn_red
        global turn_yellow

        high = 6
        still_felling = 0
        num = 0
        stay = 0
        
        for k in range(6):
            if still_felling != 1:
                num = (int(line) * 10) + int(high)
                if num in blank_spaces:
                    high -= 1
                if num in red_spaces or num in yellow_spaces:
                    still_felling = 1
                    num += 1
                    stay = 1
                    if turn_yellow == 1:
                        yellow_spaces.append(num)
                        blank_spaces.remove(num)
                    elif turn_red == 1:
                        red_spaces.append(num)
                        blank_spaces.remove(num)
            else:
                ""
        if stay != 1:
             num = (int(line) * 10) + 1
             if turn_yellow == 1:
                        yellow_spaces.append(num)
                        blank_spaces.remove(num)
             elif turn_red == 1:
                        red_spaces.append(num)
                        blank_spaces.remove(num)
                
        yy = str(num)[-1]
        yy = int(yy)
        the_x = -585 + (line * 130)
        the_y = -515 + (yy * 130)
        
        a.penup()
        a.goto(the_x, the_y)
        a.pendown()   

        if turn_red == 1:
            red()
            turn_red = 0
            turn_yellow = 1
        elif turn_yellow == 1:
            yellow()
            turn_yellow = 0
            turn_red = 1
            
        one_or_two = random.randint(1, 2)
        if one_or_two == 1:
            fall_sound_1.play()
        elif one_or_two == 2:
            fall_sound_2.play()



        #check who won

        #play again and reset thingi
        '''
        blank_spaces = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76]
        for item in red_spaces:
            red_spaces.remove(item)
        for item in yellow_spaces:
            yellow_spaces.remove(item)
            
        a.clear()    
        start_screen()

        a.onscreenclick(on_click)

        a.done()
        '''
        choosing_line()
def drawing():
    global blank_spaces
    global line
    global high
    global still_felling
    global num 
    global stay
    
    line = 0
    high = 6
    still_felling = 0
    num = 0
    stay = 0
    if the_line == 1 and 16 in blank_spaces:
        line = 1
        placing() 
    elif the_line == 2 and 26 in blank_spaces:
        line = 2
        placing()
    elif the_line == 3 and 36 in blank_spaces:
        line = 3
        placing()
    elif the_line == 4 and 46 in blank_spaces:
        line = 4
        placing()
    elif the_line == 5 and 56 in blank_spaces:
        line = 5
        placing()
    elif the_line == 6 and 66 in blank_spaces:
        line = 6
        placing()
    elif the_line == 7 and 76 in blank_spaces:
        line = 7
        placing()
        
       
while True:

    blank_spaces = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76]
    red_spaces = []
    yellow_spaces = []

    line = 0
    high = 6
    still_felling = 0
    num = 0
    stay = 0

    who_start = random.randint(1, 2)
    if who_start == 1:
                turn_red = 1
                turn_yellow = 0
    elif who_start == 2:
                turn_yellow = 1
                turn_red = 0
                    
    start_screen()

    a.onscreenclick(on_click)

    a.done()
