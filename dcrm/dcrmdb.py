import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '@XammyLove1452!'


	)
#cussor obj

cursorobject = dataBase.cursor()

#create database

cursorobject.execute("CREATE DATABASE dcrmdb")

print("All Done")