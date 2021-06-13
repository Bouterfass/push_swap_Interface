import tkinter as tk
from tkinter import Canvas
import tkinter.font as font
import sys

width = 900
height = 700

pileAa = []
pileBb = []

for arg in sys.argv:
    if arg != sys.argv[0]:
        pileAa.append(arg)

pileA = pileAa
pileB = pileBb

actions = []

def swap_A(pileA,pileB, actions):
    if not pileA or len(pileA) == 1:
        print("pile A n'a qu'un élément")
    else:
        actions.append("sa")
        actions.append("⇁")
        pileA[len(pileA) - 1], pileA[len(pileA) - 2] = pileA[len(pileA) - 2], pileA[len(pileA) - 1]
        print_pile(pileA, pileB, actions)

def swapA():
    swap_A(pileA,pileB, actions)

def swap_B(pileA,pileB, actions):
    if not pileB or len(pileB) == 1:
        print("pile B n'a qu'un élément")
    else:
        actions.append("sb")
        actions.append("⇁")
        pileB[len(pileB) - 1], pileB[len(pileB) - 2] = pileB[len(pileB) - 2], pileB[len(pileB) - 1]
        print_pile(pileA, pileB, actions)

def swapB():
    swap_B(pileA,pileB, actions)

def swap_S(pileA, pileB, actions):
    if (not pileB or len(pileB) == 1) or (not pileA or len(pileA) == 1):
        print("pile A ou B n'a qu'un élément ou est vide.")
    else:
        actions.append("ss")
        actions.append("⇁")
        pileA[len(pileA) - 1], pileA[len(pileA) - 2] = pileA[len(pileA) - 2], pileA[len(pileA) - 1]
        pileB[len(pileB) - 1], pileB[len(pileB) - 2] = pileB[len(pileB) - 2], pileB[len(pileB) - 1]
        print_pile(pileA, pileB, actions)


def swapS():
    swap_S(pileA,pileB, actions)

def push_A(pileA, pileB, actions):
    if not pileB:
        print("pileB is empty")
    else:
        tmp = pileB[len(pileB) - 1]
        pileB.pop()
        pileA.append(tmp)
        actions.append("pa")
        actions.append("⇁")
        print_pile(pileA, pileB, actions)

def pushA():
    push_A(pileA,pileB, actions)


def push_B(pileA, pileB, actions):
    if not pileA:
        print("pileA is empty")
    else:
        tmp = pileA[len(pileA) - 1]
        pileA.pop()
        pileB.append(tmp)
        actions.append("pb")
        actions.append("⇁")
        print_pile(pileA, pileB, actions)


def pushB():
    push_B(pileA,pileB, actions)


def rotate_A(pileA, pileB, actions):
    if len(pileA) <= 1:
        print("pileA vide ou ne contient qu'un element")
    else:
        actions.append("ra")
        actions.append("⇁")
        pileA.insert(0, pileA[len(pileA) - 1])
        pileA.pop() 
        print_pile(pileA, pileB, actions)
 

def rotateA():
    rotate_A(pileA, pileB, actions)


def rotate_B(pileA, pileB, actions):
    if len(pileB) <= 1:
        print("pileB est viede ou ne contient qu'un seul element")
    else:
        actions.append("rb")
        actions.append("⇁")
        pileB.insert(0, pileB[len(pileB) - 1])
        pileB.pop()
        print_pile(pileA, pileB, actions)
 

def rotateB():
    rotate_B(pileA, pileB, actions)

def rotate_R(pileA, pileB, actions):
    if len(pileA) <= 1 or len(pileB) <= 1:
        print("une des deux piles est vide ou ne contient qu'un element")
    else:
        actions.append("rr")
        actions.append("⇁")
        pileA.insert(0, pileA[len(pileA) - 1])
        pileA.pop() 
        pileB.insert(0, pileB[len(pileB) - 1])
        pileB.pop() 
        print_pile(pileA, pileB, actions)
    

def rotateR():
    rotate_R(pileA, pileB, actions)

def rotate_reverse_A(pileA, pileB, actions):
    if len(pileA) <= 1:
        print("pile A vide ou ne contient qu'un seul element")
    else: 
        actions.append("rra")
        actions.append("⇁")
        pileA.insert(len(pileA), pileA[0])
        pileA.pop(0)
        print_pile(pileA, pileB, actions)

def rotateReverseA():
    rotate_reverse_A(pileA, pileB, actions)

def rotate_reverse_B(pileA, pileB, actions):
    if len(pileB) <= 1:
        print("pile B est vide ou ne contient qu'un seul element")
    else:
        actions.append("rrb")
        actions.append("⇁")
        pileB.insert(len(pileB), pileB[0])
        pileB.pop(0)
        print_pile(pileA, pileB, actions)

def rotateReverseB():
    rotate_reverse_B(pileA, pileB, actions)

def rotate_reverse_R(pileA, pileB, actions):
    if len(pileA) <= 1 or len(pileB) <= 1:
        print("une des deux piles est vide ou ne contient qu'un seul element")
    else:
        actions.append("rrr")
        actions.append("⇁")
        pileA.insert(len(pileA), pileA[0])
        pileA.pop(0)
        pileB.insert(len(pileB), pileB[0])
        pileB.pop(0)
        print_pile(pileA, pileB, actions)

def rotateReverseR():
    rotate_reverse_R(pileA, pileB, actions)   


def reset():
    reset_all(pileA, pileB, actions)

root = tk.Tk(className="Push_swap")
root.geometry(str(width)+"x"+str(height))
root.resizable(height = None, width = None) 

buttonStyle = font.Font(family='Helvetica', weight='bold')

sa = tk.Button(root, text="sA", bg="#F1C40F", font=buttonStyle, command=swapA)
sb = tk.Button(root, text="sB", bg="#F1C40F", font=buttonStyle, command=swapB)
ss = tk.Button(root, text="ss", bg="#9B59B6", font=buttonStyle, command=swapS)

pa = tk.Button(root, text="pA", bg="#2980B9", font=buttonStyle, command=pushA)
pb = tk.Button(root, text="pB", bg="#2980B9", font=buttonStyle, command=pushB)

ra = tk.Button(root, text="rA", bg="#E74C3C", font=buttonStyle, command=rotateA)
rb = tk.Button(root, text="rB", bg="#E74C3C", font=buttonStyle, command=rotateB)
rr = tk.Button(root, text="rr", bg="#9B59B6", font=buttonStyle, command=rotateR)

rra = tk.Button(root, text="rrA", bg="#E74C3C", font=buttonStyle, command=rotateReverseA)
rrb = tk.Button(root, text="rrB", bg="#E74C3C", font=buttonStyle, command=rotateReverseB)
rrr = tk.Button(root, text="rrr", bg="#9B59B6", font=buttonStyle, command=rotateReverseR)

reset = tk.Button(root, text="reset", bg="grey", font=buttonStyle, width=10, height=3, command=reset)

sa.place(x=(width/11)+600, y=(height*0.2))
sb.place(x=(width/11)+650, y=(height*0.2))
ss.place(x=(width/11)+700, y=(height*0.2))
pa.place(x=(width/11)+600, y=(height*0.3))
pb.place(x=(width/11)+650, y=(height*0.3))
ra.place(x=(width/11)+600, y=(height*0.4))
rb.place(x=(width/11)+650, y=(height*0.4))
rr.place(x=(width/11)+700, y=(height*0.4))
rra.place(x=(width/11)+600, y=(height*0.5))
rrb.place(x=(width/11)+650, y=(height*0.5))
rrr.place(x=(width/11)+700, y=(height*0.5))
reset.place(x=(width/11)+620, y=(height*0.7))


canvas = tk.Canvas(root, width=width-300, height=height, 
                   borderwidth=0, highlightthickness=0, bg="wheat")
canvas.pack(anchor=tk.W)
canvas.create_line(200, 500, 250, 500, width=8)
canvas.create_line(350, 500, 400, 500, width=8)

canvas.create_text(225,530,fill="darkblue",font="Times 20 bold",
                        text="A")

canvas.create_text(375,530,fill="darkblue",font="Times 20 bold",
                        text="B")
canvas.pack()

def reset_all(pileA, pileB, actions):
    pileA.clear()
    for arg in sys.argv:
        if arg != sys.argv[0]:
            pileA.append(arg)
    pileB.clear()
    actions.clear()
    canvas.delete("actions")
    print_pile(pileA, pileB, actions)


def clear_print(pileA, pileB):
    canvas.delete("pile")
    canvas.delete("coup")

def print_pile(pileA, pileB, actions):
    clear_print(pileA, pileB)
    i = len(pileA) - 1
    while i >= 0:
        canvas.create_text(225,(480-i*26),fill="red",font="Times 20 bold",
                        text=str(pileA[i]), tag="pile")
        i = i - 1
    i = len(pileB) - 1
    while i >= 0:
        canvas.create_text(375,(480-i*26),fill="red",font="Times 20 bold",
                        text=str(pileB[i]), tag="pile")
        i = i - 1
    i = 0
    h = 0
    j = 0
    while i < len(actions) - 1:
        if (50+j*20 > 580):
            j = 0
            h = h + 25
        canvas.create_text(50+j*20,(50 + h),fill="black",font="Times 12 bold",
                        text=actions[i], tag='actions')
        i = i + 1
        j = j + 1

print_pile(pileA, pileB, actions)
root.mainloop()