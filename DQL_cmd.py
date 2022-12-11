import cx_Oracle

import os
os.environ['PATH'] = 'C:\\instantclient_21_7'

#Establish connection to the database

con=cx_Oracle.connect("t5_lavanya","t5_lavanya","orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com/orcl")

#Query execution
query="select * from emp"
cur=con.cursor()
cur.execute(query)

for clos in cur:
    print(clos[0],"         ",clos[1],"         ",clos[2])

cur.close()
con.commit()
con.close()

print("completed!!")