from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class userwindows:
    sqlite_var = 0 #variable to establish connection between python & sqlite3
    theCursor = 0 #variable to store indexing cursor
    curItem = 0 #variable to store currently active record

    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Refreshed")

    def search_record(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Students where name like ? or phone like ?",('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length=str(len(self.result))
            if(length==0):
                messagebox.showinfo("Search Results","No results were found, try again using part of name or phone no")
            if(length!='0'):
                i=0
                for row in self.result:
                    if(i%2==0):
                        self.tree.insert("",END, values=row,tag='1')
                    else:
                        self.tree.insert("",END, values=row,tag='2')
                    i=i+1
        except:
            raise
            print("Couldn't search Data")


        def clear_entries(self):
            self.search_value.set("")

        def update_tree(self):
            try:
                self.tree.delete(*self.tree.get_children())
                self.theCursor.execute("SELECT * FROM Students")
                self.rows = self.theCursor.fetchall()
                i=0
                for row in self.rows:
                    if(i%2==0):
                        self.tree.insert("",END, values=row,tag='1')
                    else:
                        self.tree.insert("",END, values=row,tag='2')  
                    i=i+1                    
            except:
                print("Couldn't Update Data")


        def setup_db(self):
            try:
                self.sqlite_var = sqlite3.connect('student.db')
                self.theCursor = self.sqlite_var.cursor()
            except:
                print("Could not establish connection to sqlite3")

            try:
                self.theCursor.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT , Name TEXT UNIQUE NOT NULL , Phone TEXT NOT NULL,Address TEXT NOT NULL);")
            except:
                print("ERROR : Table not created")
            finally:
                self.sqlite_var.commit()
                self.update_tree()

        def __init__(self):

            self.user_windows=Tk()
            self.user_windows.resizable(False, False)
            self.user_windows.iconbitmap("logo.ico")
            self.user_windows.title("REGIS")

