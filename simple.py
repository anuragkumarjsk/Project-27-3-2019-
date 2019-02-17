import xlwt
import string
import os
print ('hello')

def callinput():
    a=input("usn is:")
    b=input("name is:")
    c=input("sem is:")
    return a,b,c




def main():
    book=xlwt.Workbook()
    sheet=book.add_sheet("sheet1")
    sheet.write(0,0,'usn')
    sheet.write(0,1,'name')
    sheet.write(0,2,'sem')
    z=int(input('enter the no of students'))
    for i in range(1,z+1):
        name,usn,sem=callinput()
        sheet.append(i,0,usn)
        sheet.append(i,1,name)
        sheet.append(i,2,sem)

    g1=i
    book.save('sample.xls')
    os.system('xdg-open sample.xls')

if __name__=='__main__':
    main()
