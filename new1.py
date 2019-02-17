import csv
import os
def newfile():
	e=[]
	a="Name"
	b="USN"
	m="Marks"
	e.append(a)
	e.append(b)
	e.append(m)
	with open('some1.csv','w') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]
def ifnotpresent():
	with open('some1.csv') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if row['Name']=='':
				return 0
try:
	ifnotpresent()
except:
	newfile()
print("Enter the no of records")
input1=int(input())
e=[]
for i in range(1,input1):
	a=raw_input()
	b=raw_input()
	c=raw_input()
	e.append(a)
	e.append(b)
	e.append(c)
	with open('some1.csv','a') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]
os.system('xdg-open some1.csv')
