import tkinter as t
import sys
import mysql.connector
sys.setrecursionlimit(999999999)
grandmacount=0
grandmaprice=10
cookiecount=0

def increase():
    global cookiecount
    global grandmacount
    global grandmaprice
    cookiecount += 1
    countL.config(text = "cookies : " + str(cookiecount)+'\ngrandma price : '+str(grandmaprice)+'\ngrandma count : '+str(grandmacount))

def grandm():
    global cookiecount
    
    cookiecount += 1
    countL.config(text = "cookies : " + str(cookiecount)+'\ngrandma price :'+str(grandmaprice)+'\ngrandma count : '+str(grandmacount))
    countL.after(1000,grandm)
    
def ab():
    a=0
    
def price():
    global cookiecount,grandmacount
    global grandmaprice
    cookiecount -=grandmaprice
    grandmaprice+=10
    grandmacount +=1


tk1=t.Tk()
countL = t.Label(tk1, text = "cookies : " + str(cookiecount)+'\ngrandma price : '+str(grandmaprice)+'\ngrandma count : '+str(grandmacount))
countL.grid(row = 0, column = 0)
Cmain = t.Button(tk1,text = "substitue\ncookie",padx = 50,pady=50,command = increase)
Cmain.grid(row = 1,column = 0)
Grandma = t.Button(tk1,text = "substitue\ngrandma",padx = 50,pady=50,command = lambda:[grandm(),price()] if cookiecount>=grandmaprice else ab())
Grandma.grid(row = 1,column = 1)
