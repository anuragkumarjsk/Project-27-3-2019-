import csv
import os

def newfile():
    e=[]
    a="name"
    b="usn"
    c="marks"
    e.append(a)
    e.append(b)
    e.append(c)
    #write
    with open("trial.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow(e)
        del e[:]


def ifnotpresent():
    with open("trial.csv") as csvfil:
        reader=csv.DictReader(csvfil)
        for row in reader:
            if row["name"]=='':
                return 0

try:
    ifnotpresent()
except:
    newfile()

n=int(input("enter the no of students"))
for j in range(1,n+1):
    e=[]
    a=input("name")
    b=input("usn")
    c=input("marks")
    e.append(a)
    e.append(b)
    e.append(c)
    with open("trial.csv","a",newline='') as f:
        writer=csv.writer(f)
        writer.writerow(e)
        del e[:]

os.system('xdg-open trial.csv')
