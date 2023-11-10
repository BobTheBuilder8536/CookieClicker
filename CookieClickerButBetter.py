import tkinter as t
import sys
import ctypes
sys.setrecursionlimit(999999999)
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def increase():
    global cookiecount,buff
    cookiecount += 1

    cMain.config(image = cImg2)
    countL.config(
        text="cookies : " + str(cookiecount) + "\ncookies per second : " + str(buff)
    )
    cMain.config(image = cImg)
    


def cps():
    global cookiecount,buff

    cookiecount += buff
    countL.config(text="cookies : " + str(cookiecount) + "\ncookies per second : " + str(buff))
    countL.after(1000, cps)


def ab():
    a = 0

def icon(item):
    global BgImg,BoImg,BfImg
    if item == "grandma":
        granIcon = t.Label(tk1,bg="#fff",image=BgImg)
        granIcon.place(x = 0, y=0)
        granIcon.after(1000,granIcon.destroy)
    elif item == "oven":
        ovenIcon = t.Label(tk1,bg="#fff",image=BoImg)
        ovenIcon.place(x =0, y=0)
        ovenIcon.after(1000,ovenIcon.destroy)
    elif item == "factory":
        factIcon = t.Label(tk1,bg="#fff",image=BfImg)
        factIcon.place(x = 0, y=0)
        factIcon.after(1000,factIcon.destroy)


def grandma():
    global cookiecount, grandmacount,grandmaprice, buff
    icon("grandma")
    cookiecount -= grandmaprice
    grandmaprice += 10
    grandmacount += 1
    buff += 1
    infoG.config(
        text="Grandma price : "
        + str(grandmaprice)
        + "\nGrandma count : "
        + str(grandmacount)
    )

def oven():
    global cookiecount, ovencount, ovenprice,buff
    icon("oven")
    cookiecount -= ovenprice
    ovenprice += 100
    ovencount += 1
    buff += 10
    infoO.config(
        text="Oven price : "
        + str(ovenprice)
        + "\nOven count : "
        + str(ovencount)
    )

def factory():
    global cookiecount, factorycount, factoryprice, buff
    icon("factory")
    cookiecount -= factoryprice
    factoryprice += 10000
    factorycount += 1
    buff += 500
    infoF.config(
        text="Factory price : "
        + str(factoryprice)
        + "\nFactory count : "
        + str(factorycount)
    )

tk1 = t.Tk()
tk1.title("Cookie Clicker")
tk1.geometry("510x510")
tk1.minsize(510,510)
tk1.maxsize(510,510)
tk1.configure(bg="#fff")

cImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\cookie.png")
cImg2 = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\cookie2.png")

gImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\grandma.png")
BgImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\biggrandma.png")
oImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\oven.png")
BoImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\bigoven.png")
fImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\factory.png")
BfImg = t.PhotoImage(file = r"C:\Prateek Stuff\Coding\CookieClicker\bigfactory.png")


grandmacount = 0
grandmaprice = 10

ovencount = 0
ovenprice = 100

factorycount = 0
factoryprice = 10000

cookiecount = 0

buff = 0


countL = t.Label(
    tk1,
    justify = t.CENTER,
    bg = "#fff",
    text="Cookies : " + str(cookiecount) + "\n\nCookies Per Second : " + str(buff)
)
countL.grid(row=0, column=0,rowspan=2)


cMain = t.Button(
    tk1,
    bg = "#fff",
    fg = "#fff",
    image = cImg,
    height = 300,
    width = 300,
    borderwidth=0, 
    command=increase
)
cMain.grid(row=2, column=0,rowspan=4)


infoG = t.Label(
    tk1,
    bg = "#fff",
    text="Grandma price : " + str(grandmaprice) + "\nGrandma Count : " + str(grandmacount)
)
infoG.grid(pady=3.5,row=0, column=1)

infoO = t.Label(
    tk1,
    bg = "#fff",
    text="Oven price : " + str(ovenprice) + "\nOven count : " + str(ovencount)
)
infoO.grid(pady=3.5,row=2, column=1)

infoF = t.Label(
    tk1,
    bg = "#fff",
    text="Factory price : " + str(factoryprice) + "\nFactory count : " + str(factorycount)
)
infoF.grid(pady=3.5,row=4, column=1)


Grandma = t.Button(
    tk1,
    bg = "#fff",
    image=gImg,
    height=102,
    width = 210,
    borderwidth=0,
    command=lambda: [grandma()] if cookiecount >= grandmaprice else ab(),
)
Grandma.grid(row=1, column=1)

Oven = t.Button(
    tk1,
    bg = "#fff",
    image=oImg,
    height=102,
    width = 210,
    borderwidth=0,
    command=lambda: [oven()] if cookiecount >= ovenprice else ab(),
)
Oven.grid(row=3, column=1)

Factory = t.Button(
    tk1,
    bg = "#fff",
    image=fImg,
    height=102,
    width = 210,
    borderwidth=0,
    command=lambda: [factory()] if cookiecount >= factoryprice else ab(),
)
Factory.grid(row=5, column=1)

cps()
tk1.mainloop()
