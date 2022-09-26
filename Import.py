<!---
File to import csv
--->

import mariadb
import csv

conn = mariadb.connect('filename')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS temp')
cur.execute('''
CREATE TABLE "temp"(
	"name" TEXT,
	"name" INT,     
	"name" DATE
	INDEX index_name (name)
	CONSTRAINT temp_pk PRIMARY KEY (colum1,column2....)
	CONSTRAINT temp_unique UNIQUE (colum1)
)
''')


# BOOLEAN, TINYINT, SMALLINT, MEDIUMINT, INT, FLOAT, TEXT, MEDIUMTEXT, TINYTEXT, 
# BINARY, DATE, TIME, DATETIME,  AUTO_INCREMENT, BIT
	
fname="filename of csv"

with open(fname) as csv_file:
	csv_reader = csv.reader(csv.file, delimiter=',')
	for row in csv_reader:
		print(row)
		item1=row[0]
		item2=row[1]
		item3=float(row[3])
		cur.execute('''INSERT INTO temp(item1,item2,item3)
		    VALUES (?,?,?)''', (item1, item2, item3))
		conn.commit()
		
		
