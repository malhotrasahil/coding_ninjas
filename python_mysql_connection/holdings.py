import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="free1234",
  database='classicmodels'  
  #passwd="*E75E2A576177BA140498EB7479B76C4C36604346"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM holdings")

myresult_hol = mycursor.fetchall()
print(type(myresult_hol))
# for x in myresult:
#   print(x)
print(myresult_hol)
print(type(myresult_hol[0]))


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM translation")

myresult_tra = mycursor.fetchall()
print(type(myresult_tra))
# for x in myresult:
#   print(x)
print(myresult_tra)

dict={}
for i in myresult_tra:
    dict[i[0]]=i[1]
	
list_tup=list()
for item in myresult_hol:
    list_tup.append((item[0],dict.get(item[1]),item[2]))
	
mycursor.execute("CREATE TABLE new_holdings (acc int, sec_nm VARCHAR(255), sec_id int)")


sql = "INSERT INTO new_holdings (acc , sec_nm , sec_id ) VALUES (%s,%s, %s)"

for ele in list_tup:
    val = ele
    mycursor.execute(sql, val)
    print(mycursor.rowcount, "record inserted.")
mydb.commit()

mycursor.close()
del mycursor 
mydb.close()