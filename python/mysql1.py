# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 17:14:22 2018

@author: 124578
"""

import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', database='mydb1')
cursor = cnx.cursor()



csv_data = csv.reader(file('patient_struc.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO resources(field, min,max,mapping_hl7 )'\
          'VALUES(%s, %s, %s, %s)', 
          row)

cnx.commit()

cursor.close()
cnx.close()