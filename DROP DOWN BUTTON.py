import tkinter as t
items=["JAN","FAB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
def show ():
     m=myvar.get()
     showLB=t.Label(win)
     showLB.place(x=10,y=130)
     showLB.config(text="YOU HAVE SELECTED  - " +m,fg="black")
     
    

win=t.Tk()

win.geometry("500x500")

myvar=t.StringVar(win)
myvar.set("CHOOSE A MONTH")



drop=t.OptionMenu(win,myvar,*items)
drop.place(x=10,y=10)
drop.config(bg="BLUE",fg="black",font=("bold",10))
drop["menu"].config(bg="green",fg="yellow",font=("bold",15))


bt=t.Button(win,text="SUBMIT",command=show)
bt.place(x=10,y=70)
bt.config(bg="orange")
