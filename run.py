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
            self.user_windows.title("REGISTRX")



            # 5TH ROW
            self.tree = ttk.Treeview(self.user_windows,selectmode="browse",column=("column1", "column2", "column3","column4"), show='headings')
            self.tree.column1("column",width=100,minwidth=100,stretch=NO)
            self.tree.heading("#1", text="ADMISSION")
            self.tree.column("column2",width=180,minwidth=180,stretch=NO)
            self.tree.heading("#2", text="NAME")
            self.tree.column("column3",width=180,minwidth=180,stretch=NO)
            self.tree.heading("#3", text="PHONE")
            self.tree.column("column4",width=450,minwidth=450,stretch=NO)
            self.tree.heading("#4", text="ADDRESS")
            self.tree.tag_configure('1', background='ivory2')
            self.tree.tag_configure('2', background='alice blue')
            self.tree.grid(row=4,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)

            Label(self.user_windows,text="Search by Part of NAME or Phone No:").grid(row=5,column=0,columnspan=2,pady=9,padx=9,sticky=E)
            self.search_value = StringVar(self.user_window, value="")
            Entry(self.user_window,textvariable=self.search_value).grid(row=5,column=2,pady=9,padx=9,sticky=W+E)
            self.search_button = ttk.Button(self.user_window,text="Search",command=self.search_record)
            self.search_button.grid(row=5,column,padx=9,pady=9,sticky=W+E)

            self.refresh_button = ttk.Button(self.user_window,text="Refresh",command=self.refresh)
            self.search_button.grid(row=6,column=2,padx=9,pady=9,sticky=W+E)


            self.setup_db()
            self.user_window.mainloop()


class adminwindows:

    sqlite_var = 0 
    theCursor = 0
    curItem = 0

    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Refreshed")

        def search_record(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Students where name like ? or phone like  ?",('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
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

    def reset_db(self):
        yesno=messagebox.askquestion("RESET DB", "All data in DB will be lost, continue?")
        if(yesno='yes'):
            self.theCursor.execute("DROP TABLE Students")
            print("Database Reset")
            self.setup_db()
            self.update_tree()

    def clear_entries(self):
        self.Name_entry.delete(0,"end")

