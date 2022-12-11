import cx_Oracle

import os
os.environ['PATH'] = 'C:\\instantclient_21_7'

#Establish connection to the database

con=cx_Oracle.connect("t5_lavanya","t5_lavanya","orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com/orcl")

#adding new data
add="INSERT INTO emp VALUES (150,'Ramya',6383620529,'#13sdjfsjd',4000,101)"

#modifing data
upd="Update emp set emp_name='meena' where emp_id=100"

#deleting data
delete = "delete emp where emp_id=103"

cur=con.cursor()
cur.execute(delete)

cur.close()
con.commit()
con.close()

print("completed!!")