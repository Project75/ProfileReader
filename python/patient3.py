# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:53:53 2017

@author: 124578
"""

import xml.etree.cElementTree as ET
import csv
filename = r'C:\Users\124578\Documents\python\patient3.xml'
#profiles-resources.xml'
tree = ET.parse(filename)
root0 = tree.getroot()

# open a file for writing

Resident_data = open('C:/Users/124578/Documents/python/resources-out.csv', 'wb')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for root1 in root0.findall('{http://hl7.org/fhir}entry'):
	root2 = root1.find('{http://hl7.org/fhir}resource').find('{http://hl7.org/fhir}StructureDefinition').find('{http://hl7.org/fhir}snapshot')
	for member in root2.findall('{http://hl7.org/fhir}element'):
		fieldsList = []

		
		code = ""
		name = member.find('{http://hl7.org/fhir}path').get('value')
		print name
		fieldsList.append(name)
		Min = member.find('{http://hl7.org/fhir}min').get('value')
		fieldsList.append(Min)
		Max = member.find('{http://hl7.org/fhir}max').get('value')
		fieldsList.append(Max)
		for dtypes in member.findall('{http://hl7.org/fhir}type'):
			DType = dtypes.find('{http://hl7.org/fhir}code').get('value')
			fieldsList.append(DType)
		for mapping in member.iter('{http://hl7.org/fhir}mapping'):
			type= mapping.find('{http://hl7.org/fhir}identity').get('value')
			if type == 'v2':
				code= mapping.find('{http://hl7.org/fhir}map').get('value') #('value')
				#print code 
				code =  code.replace(",", "|")
				#print code
		fieldsList.append(code)
		csvwriter.writerow(fieldsList)

Resident_data.close()

