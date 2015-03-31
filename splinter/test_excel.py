#encoding=utf-8
import xlrd
import sys

rfile = xlrd.open_workbook("111.xlsx")

#table = rfile.sheet_by_index(0)

def open_excel(file="111.xlsx"):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file="111.xlsx",colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []

    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            
            #print range(len(colnames))
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                #print colnames[i]
                #print row[i]
            list.append(app)
    return list

#print nrows
#print table.row_values(0)


tables = excel_table_byindex()
for row in tables:
    print row
