import csv
def newfile():
	e=[]
	a="Name"
	b="USN"
	e.append(a)
	e.append(b)
	with open('some2.csv','w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(e)
		del e[:]
def ifnotpresent():
	with open('some2.csv') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if row['Name']=='':
				return 0
try:
	ifnotpresent()
except:
	newfile()
with open('some1.csv') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:
		e=[]
		a=int(row["Marks"])
		if(a<60):
			b=row["Name"]
			c=row["USN"]
			e.append(b)
			e.append(c)
			with open('some2.csv','a', newline='') as f:
				writer = csv.writer(f)
				writer.writerow(e)
				del e[:]
