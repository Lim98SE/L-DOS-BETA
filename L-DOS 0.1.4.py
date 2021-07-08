# L-DOS 0.1.4 [Rewrite]
import winsound
import turtle
import os
import time
def musread(file):
    print("This requires PyGame.")
    import pygame
    loop = False
    song_to_load = file
    while not os.path.exists(song_to_load):
        song_to_load = input("Song to load: ")
    print("Loading " + song_to_load + "...")
    pygame.init()
    pygame.mixer.music.load(song_to_load)
    pygame.mixer.music.play(loops=0)
    com = ""
    turtle.clear()
    turtle.goto(0, 0)
    ldos.scwrt(0, 0, "Playing Music...", 40, "center", 0, ldos.fg)
    ldos.scwrt(0, -50, file, 15, "center", 0, ldos.fg)
    while not com == "stop":
        com = input("Type media command: ")
        if com == "play":
            pygame.mixer.music.unpause()
        if com == "pause":
            pygame.mixer.music.pause()
        if com == "restart":
            pygame.mixer.music.rewind()
        if "skip" in com:
            pos = float(com[5:len(com)].replace(":", "."))
            pos = pos * 60
            pygame.mixer.music.set_pos(pos)
    pygame.mixer.music.stop()
class ldos:
    version = "0.1.4B0"
    release = "L-DOS 0.1.4 Beta 0"
    ver_int = 5
    ver_flt = 0.14
    turtle.speed(10000000)
    turtle.clear()
    turtle.ht()
    turtle.pu()
    fg = "#000000"
    bg = "#ffffff"
    r = "#ff0000"
    g = "#00ff00"
    b = "#0000ff"
    y = "#ffff00"
    p = "#ff00ff"
    c = "#00ffff"
    bl = "#000000"
    wt = "#ffffff"
    gy = "#999999"
    font = "Arial"
    pid = 0
    getpos = turtle.pos()
    def boot(v):
        return(str(v) + " is loading...")
    def sound(f, l):
        winsound.Beep(f, l)
    def redraw(d, c):
        turtle.title("L-DOS")
        turtle.clear()
        turtle.bgcolor(ldos.bg)
        turtle.ht()
        turtle.pu()
        turtle.goto(0, 0)
        turtle.pencolor(ldos.fg)
        turtle.write(d, align='center', font=(ldos.font, 20))
        turtle.goto(0, -50)
        turtle.write(c, align='center', font=(ldos.font, 20))
        turtle.goto(0, 365)
        turtle.write("L-DOS 0.1.4", align='center', font=(ldos.font, 10))
        ldos.getpos = turtle.pos()
    def bootnoise():
        ldos.sound(1000, 750)
        ldos.sound(1250, 750)
        ldos.sound(1500, 750)
        ldos.sound(2000, 750)
    def loadcol(file):
        if os.path.exists(file):
            f = open(file, 'r')
            ldos.fg = f.readline().replace("\n", "")
            ldos.bg = f.readline().replace("\n", "")
            ldos.r = f.readline().replace("\n", "")
            ldos.g = f.readline().replace("\n", "")
            ldos.b = f.readline().replace("\n", "")
            ldos.y = f.readline().replace("\n", "")
            ldos.p = f.readline().replace("\n", "")
            ldos.c = f.readline().replace("\n", "")
            ldos.bl = f.readline().replace("\n", "")
            ldos.wt = f.readline().replace("\n", "")
            ldos.gy = f.readline().replace("\n", "")
            ldos.font = f.readline().replace("\n", "")
            print("Success!")
        else:
            print("File not found: " + file)
    def scwrt(x, y, txt, size, align, wait, col):
        turtle.goto(x, y)
        turtle.color(col)
        turtle.write(txt, align=align, font=(ldos.font, size))
        time.sleep(wait)
        ldos.getpos = turtle.pos()
    def line(x, y, wd, col):
        turtle.color(col)
        turtle.width(wd)
        turtle.pd()
        turtle.goto(x, y)
        turtle.pu()
        ldos.getpos = turtle.pos()
    def circle(rad, wd, col):
        turtle.color(col)
        turtle.width(wd)
        ypos = turtle.ycor()
        turtle.pd()
        turtle.circle(rad)
        turtle.pu()
        ldos.getpos = turtle.pos()
        turtle.goto(turtle.xcor(), ypos)
    def pos(x, y):
        turtle.goto(x, y)
        ldos.getpos = turtle.pos()
    def poly(ln, sd, wd, col):
        turtle.color(col)
        turtle.width(wd)
        turtle.pd()
        for i in range(sd):
            turtle.rt(360 / sd)
            turtle.fd(ln)
        turtle.pu()
        ldos.getpos = turtle.pos()
    def goto(x, y):
        ldos.pos(x, y)
turtle.bgcolor(ldos.bg)
def load():
    ldos.loadcol("theme.ldt")
    ldos.scwrt(0, 0, "L-DOS 0.1.4 is loading...", 30, "center", 0, ldos.bl)
    print(ldos.boot(ldos.release))
    ldos.bootnoise()
    prev = "No Previous Command"
    while 1 == 1:
        ldos.redraw(os.getcwd(), prev)
        cm = input("$>")
        command = cm.lower()
        prev = cm
        if command == "exit":
            exit()
        elif command == "py":
            break
        elif "font" in command:
            ldos.font = cm[5:len(cm)]
        elif "bg" in command:
            ldos.bg = cm[3:len(cm)]
        elif "fg" in command:
            ldos.fg = cm[3:len(cm)]
        elif "scwrt" in command:
            text = cm[6:len(cm)]
            turtle.clear()
            ldos.scwrt(0, 0, text, 20, "center", 5)
        elif "cd" in command:
            goto = cm[3:len(cm)]
            if os.path.exists(goto):
                os.chdir(goto)
            else:
                print("File not found: " + goto)
        elif "dir" in command:
            param = cm[4:len(cm)]
            print("""To go back, type "..\"""")
            print(os.getcwd())
            for x in os.listdir():
                if param in x:
                    print(x)
        elif command == "pd":
            os.chdir("../")
        elif "pal" in command:
            print("Current pallate id: " + str(ldos.pid))
            print("""ID 0: Base
ID 1: Inverted
ID 2: Dark Mode
ID 3: Blue Dark Mode
ID 4: theme.ldt""")
            prm = cm[3:len(cm)]
            if prm == "":
                pal = int(input("New Pallate ID: "))
            else:
                pal = int(prm)
            if pal == 0:
                ldos.fg = "#000000"
                ldos.bg = "#ffffff"
                ldos.r = "#ff0000"
                ldos.g = "#00ff00"
                ldos.b = "#0000ff"
                ldos.y = "#ffff00"
                ldos.p = "#ff00ff"
                ldos.c = "#00ffff"
                ldos.bl = "#000000"
                ldos.wt = "#ffffff"
                ldos.gy = "#999999"
            if pal == 1:
                ldos.fg = "#ffffff"
                ldos.bg = "#000000"
                ldos.r = "#0000ff"
                ldos.g = "#ff0000"
                ldos.b = "#00ff00"
                ldos.y = "#00ffff"
                ldos.p = "#00ffff"
                ldos.c = "#ffff00"
                ldos.bl = "#ffffff"
                ldos.wt = "#000000"
                ldos.gy = "#999999"
            if pal == 2:
                ldos.fg = "#ffffff"
                ldos.bg = "#000000"
                ldos.r = "#ff0000"
                ldos.g = "#00ff00"
                ldos.b = "#0000ff"
                ldos.y = "#ffff00"
                ldos.p = "#ff00ff"
                ldos.c = "#00ffff"
                ldos.bl = "#000000"
                ldos.wt = "#ffffff"
                ldos.gy = "#999999"
            if pal == 3:
                ldos.fg = "#0000ff"
                ldos.bg = "#000000"
                ldos.r = "#ff0000"
                ldos.g = "#00ff00"
                ldos.b = "#0000ff"
                ldos.y = "#ffff00"
                ldos.p = "#ff00ff"
                ldos.c = "#00ffff"
                ldos.bl = "#000000"
                ldos.wt = "#ffffff"
                ldos.gy = "#999999"
            if pal == 4:
                ldos.loadcol("theme.ldt")
            ldos.pid = pal
        elif "play" in command:
            f = cm[5:len(cm)]
            musread(f)
load()
