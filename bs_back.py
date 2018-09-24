# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:53:30 2018

@author: Dinesh
"""

import sqlite3 as sq

def create():
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
	con.commit()
	con.close()
 
def insert(title,auth,year,isbn):
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,auth,year,isbn,))
	con.commit()
	con.close()

def view():
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	con.close()
	return rows

def search(title="",auth="",year="",isbn=""):
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,auth,year,isbn))
	rows=cur.fetchall()
	con.close()
	return rows

def delete(id):
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,))
	con.commit()
	con.close()
	
def update(id,title,auth,year,isbn):
	con=sq.connect("bookstore_db.db")
	cur=con.cursor()
	cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,auth,year,isbn,id))
	con.commit()
	con.close()

create()
