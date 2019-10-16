import mysql.connector
from datetime import date

to_date = str(date.today())
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "vts"
)		
mycursor = mydb.cursor()

def addCustomer(fname, lname, email, mo, number_plate, city, land_mark, ty):
    sql = "INSERT INTO data_customer (fname,lname,email,mo,number_plate,city,land_mark,type,date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (fname,lname,email,mo,number_plate,city,land_mark,ty,to_date)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Added!")
    return True