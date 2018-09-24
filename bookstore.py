# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:19:59 2018

@author: Dinesh
"""
from tkinter import *
import bs_back as bk
window=Tk()
window.wm_title("Bookstore")
def view_com():
	listb1.delete(0,END)
	for x in bk.view():
		listb1.insert(END,x)

def search_com():
	listb1.delete(0,END)
	for x in bk.search(title.get(),author.get(),year.get(),isbn.get()):
		listb1.insert(END,x)

def insert_com():
	bk.insert(title.get(),author.get(),year.get(),isbn.get())
	listb1.delete(0,END)
	listb1.insert(END,(title.get(),author.get(),year.get(),isbn.get()))

def update_com():
	bk.update(row[0],title.get(),author.get(),year.get(),isbn.get())
	
def delete_com():
	bk.delete(row[0])
	
lb1=Label(window,text="Title")
lb1.grid(row=1,column=0)

title=StringVar()
e1=Entry(window,textvariable=title)
e1.grid(row=1,column=1)

lb2=Label(window,text="Author")
lb2.grid(row=1,column=2)

author=StringVar()
e2=Entry(window,textvariable=author)
e2.grid(row=1,column=3)

lb3=Label(window,text="Year")
lb3.grid(row=2,column=0)

year=StringVar()
e3=Entry(window,textvariable=year)
e3.grid(row=2,column=1)

lb4=Label(window,text="ISBN")
lb4.grid(row=2,column=2)

isbn=StringVar()
e4=Entry(window,textvariable=isbn)
e4.grid(row=2,column=3)

listb1=Listbox(window,height=8,width=38)
listb1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

listb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listb1.yview)

def get_id(event):
	global row
	index=listb1.curselection()[0]
	row=listb1.get(index)
	e1.delete(0,END)
	e1.insert(END,row[1])
	e2.delete(0,END)
	e2.insert(END,row[2])
	e3.delete(0,END)
	e3.insert(END,row[3])
	e4.delete(0,END)
	e4.insert(END,row[4])
	
listb1.bind('<<ListboxSelect>>',get_id)

bt1=Button(window,text="View All",command=view_com,width=13)
bt1.grid(row=3,column=3)

bt2=Button(window,text="Search Entry",command=search_com,width=13)
bt2.grid(row=4,column=3)

bt3=Button(window,text="Add Entry",command=insert_com,width=13)
bt3.grid(row=5,column=3)

bt4=Button(window,text="Update",command=update_com,width=13)
bt4.grid(row=6,column=3)

bt5=Button(window,text="Delete ",command=delete_com,width=13)
bt5.grid(row=7,column=3)

bt6=Button(window,text="Close",command=window.destroy,width=13)
bt6.grid(row=8,column=3)

window.mainloop()