import csv
import os
def newfile():
	e=[]
	a="Key"
	e.append(a)
	with open('some3.csv','w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]
def ifnotpresent():
	with open('some3.csv') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if row['Key']=='':
				return 0
try:
	ifnotpresent()
except:
	newfile()
print("Enter the no of records")
input1=int(input())
e=[]
for i in range(0,input1):
	a=input()
	e.append(a)
	with open('some3.csv','a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]
print("Enter the key")
a=input()
c=0
with open('some3.csv') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:
		c=c+1
		if row['Key']==a:
			print("Found the key at position",c)


opt=input("do you want to open csv file press y/n")
if(opt=="y"):
	subprocess.call(['xdg-open some3.csv'])
else:
	os.system('exit')
