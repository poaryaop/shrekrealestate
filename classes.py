import sqlite3
import tkinter as tk

conn = sqlite3.connect("database.db")
c = conn.cursor()

def createnewaccount(username,password):
    a = []
    c.execute("SELECT * FROM data")
    length = c.fetchall()

    for i in range(1,len(length)):
        a.append(c.fetchone()[0])
    if username not in a:
        c.execute("INSERT INTO data VALUES ("+username+","+password+","+str(0)+")")
    else:
        print("Username is not available")


class user:
    def __init__(self,username="root",password="toor",budget=0):
        self.username=username
        self.password=password
        self.budget=budget
    def changeusername(self,other:str):
        self.username=other
        c.execute('UPDATE data SET username'+other+' WHERE password ='+self.password+" ")         
    def changepassword(self,other):
        self.password=other
        c.execute('UPDATE data SET password'+other+' WHERE username ='+self.username+" ")     
    def whoami(self):
        return self.username,self.password

    def addbudget(self,other:int):
        self.budget += other
        c.execute('UPDATE data SET budget'+str(other)+' WHERE username ='+self.username+" ")     
    def takebudget(self,other:int):
        if(other > self.budget):
            print("Error")
        else:
            self.budget -= other
            c.execute('UPDATE data SET budget'+str(self.budget)+' WHERE username ='+self.username+" ")     
    def currentproperty(self,other):
        c.execute("SELECT * FROM data")
        a = c.fetchall()
        for i in range(1,len(a)):
            if(self.username == a[0]):
                print(a[2])


class property:
    def __init__(self,propertyID,area,location,price):
        self.propertyID = propertyID
        self.area = area
        self.price = price
        self.location = location
    def save(self,other):
        c.execute("INSERT INTO housesforsale VALUES ("+self.propertyID+","+self.price+","+self.area+","+self.location+")")


class requests:
    def __init__(self,propertyID,username,password):
        self.propertyID = propertyID
        self.username=username
        self.password = password
    
    
    def buy(self):
        c.execute("SELECT * FROM data")
        users=c.fetchall()
        bud=0
        for i in range(1,len(users)):
            if(c.fetchone()[0] == self.username):
                bud = c.fetchone()[2]
        c.execute("SELECT * FROM housesforsale")
        houses = c.fetchall()
        houseprice=0
        cur=0
        for i in range(0,len(houses)):
            if(c.fetchone()[0] == self.propertyID):
                houseprice = c.fetchone()[1]
                cur = i
        if(houseprice > bud):
            print("FAILED: not enough money")
        else:
            c.execute('UPDATE data SET currentpropertyID ='+ str(self.propertyID) +" WHERE username ="+self.username+" ")
            c.execute('UPDATE data SET budget'+(bud - houseprice)+' WHERE username ='+self.username+" ")
            c.execute('DELETE FROM housesforsale WHERE rowid ='+str(cur)+" ")

    
    def sell(self):
        c.execute("SELECT * FROM data")
        users=c.fetchall()
        bud=0
        for i in range(1,len(users)):
            if(c.fetchone()[0] == self.username):
                bud = c.fetchone()[2]
        houseprice=0
        c.execute("SELECT * FROM housesforsale")
        houses = c.fetchall()
        for i in range(0,len(houses)):
            if(c.fetchone()[0] == self.propertyID):
                houseprice = c.fetchone()[1]
        c.execute('UPDATE data SET currentpropertyID =0 WHERE username ='+self.username+" ")
        c.execute('UPDATE data SET budget'+(bud + houseprice)+' WHERE username ='+self.username+" ")
        c.execute("INSERT INTO housesforsale VALUES ("+self.propertyID+","+self.price+","+self.area+","+self.location+")")
