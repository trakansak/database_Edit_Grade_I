#!/usr/bin/python
from __future__ import print_function
import psycopg2
import csv, sys
import tkinter.filedialog


def main():

	# Get name Database
	dbName = "projectactivity"

	# Get student detail
	objectName = input("Table Name: ")

	
	# Get record from CSV file
	csvfile = tkinter.filedialog.askopenfilename(title='Select CSV file',filetypes = [(("CSV files",".csv"),("all files","*.*"))])

	# Connect to DB
	psycopg2_connection = psycopg2.connect(dbname=dbName ,user='postgres', password='123456',port='3000')
	cursor = psycopg2_connection.cursor()

	# Insert Table Student
	if(objectName == "Student"):
		record = readCSV4(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO Student "
						"(StudentID,StudentName,Groupp,ProjectID) "
						"VALUES (%s,%s,%s,%s);", 
						(subject[0], subject[1], subject[2], subject[3])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))

	# Insert Table Teacher
	elif(objectName == "Teacher"):
		record = readCSV3(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO Teacher "
						"(TeacherID,TeacherName,Groupp) "
						"VALUES (%s,%s,%s);", 
						(subject[0], subject[1], subject[2])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))
	
	# Insert Table Project
	elif(objectName == "Project"):
		record = readCSV3(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO Project "
						"(ProjectID,ProjectName,TeacherID) "
						"VALUES (%s,%s,%s);", 
						(subject[0], subject[1], subject[2])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))
	

	# Insert Table Activity
	elif(objectName == "Activity"):
		record = readCSV3(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO Activity "
						"(ActivityID,ActivityName,Description) "
						"VALUES (%s,%s,%s);", 
						(subject[0], subject[1], subject[2])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))
	
	
	# Insert Table DoneActivity
	elif(objectName == "DoneActivity"):
		record = readCSV2(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO DoneActivity "
						"(StudentID,ActivityID) "
						"VALUES (%s,%s);", 
						(subject[0], subject[1])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))
	

	# Insert Table AdviseActivity
	elif(objectName == "AdviseActivity"):
		record = readCSV2(csvfile)
		for term in record:
			for subject in term:
				try:
					cursor.execute(
						"INSERT INTO AdviseActivity "
						"(TeacherID,ActivityID) "
						"VALUES (%s,%s);", 
						(subject[0], subject[1])
					)
				except psycopg2.Error as error:
					print("Error: {}".format(error))
	

	# Check Status Completed
	print ("Complete: INSERT TABLE "+objectName)
	psycopg2_connection.commit()
	psycopg2_connection.close()

# Import File CSV 4-Column
def readCSV4(csvfile):
		with open(csvfile) as csvfile:
			next(csvfile)
			reader = csv.reader(csvfile)
			record, term = [], []
			for row in reader:			# add object to term
				term.append([row[0],row[1],row[2],row[3]])
				record.append(term)
				term = []
		return record

# Import File CSV 3-Column
def readCSV3(csvfile):
		with open(csvfile) as csvfile:
			next(csvfile)
			reader = csv.reader(csvfile)
			record, term = [], []
			for row in reader:			# add object to term
				term.append([row[0],row[1],row[2]])
				record.append(term)
				term = []
		return record

# Import File CSV 2-Column
def readCSV2(csvfile):
		with open(csvfile) as csvfile:
			next(csvfile)
			reader = csv.reader(csvfile)
			record, term = [], []
			for row in reader:			# add object to term
				term.append([row[0],row[1]])
				record.append(term)
				term = []
		return record
		
main()