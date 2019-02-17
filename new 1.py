import csv
def newfile():
	e=[]
	a="Name"
	b="USN"
	m="Marks"
	e.append(a)
	e.append(b)
	e.append(m)
	with open('some1.csv','w', newline='') as f:
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
	a=input()
	b=input()
	c=input()
	e.append(a)
	e.append(b)
	e.append(c)
	with open('some1.csv','a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]




		