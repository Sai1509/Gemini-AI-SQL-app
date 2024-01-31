import sqlite3

### Connect to sqlite
connection=sqlite3.connect('student.db')

## Create a cursor object to insert record, create table, retrive
cursor=connection.cursor()

# Create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Sai Gowtham', 'Data Science', 'B', 90)''')
cursor.execute('''Insert Into STUDENT values('Karthika', 'Computer Science', 'A', 100)''')
cursor.execute('''Insert Into STUDENT values('Harsha', 'Data Science', 'A', 80)''')
cursor.execute('''Insert Into STUDENT values('Pavan', 'Information Systems', 'B', 66)''')
cursor.execute('''Insert Into STUDENT values('Rahul', 'Mechanical', 'A', 93)''')

## Display all the records
print('The inserted records are')

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close() 

