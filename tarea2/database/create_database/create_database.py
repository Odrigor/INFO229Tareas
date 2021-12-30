import mysql.connector
import os, time

def create_database(db_connection,db_name,cursor):
	cursor.execute(f"CREATE DATABASE {db_name};")
	cursor.execute(f"COMMIT;")
	cursor.execute(f"USE {db_name};")
	
	# Tabla news
	cursor.execute('''CREATE TABLE news (
		id_news INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		url TEXT,
		title TEXT, 
		date TEXT,
		media_outlet VARCHAR(50),
		category VARCHAR(100)
        );''')

	cursor.execute("SET GLOBAL time_zone = 'UTC';")
	cursor.execute("SET SESSION time_zone = 'UTC';")

	cursor.execute("COMMIT;") 

def insert_data(cursor):
    print("insert")
    cursor.execute('''IINSERT INTO news (url,title,date,media_outlet,category) VALUES
    ('https://www.thesun.co.uk/sport/17172941/chelsea-1-brighton-1-lukaku-james-welbeck/
','GOOD LUK, BAD LUCK Chelsea 1 Brighton 1: Dramatic Welbeck equaliser cancels out Lukaku opener as Reece James goes off injured in huge blow 
','2021-12-29','The Sun','football'),
    ('https://www.thesun.co.uk/money/17166481/supermarkets-slash-price-xmas-treats-heroes-lindt/
','CHOC OUT Supermarkets including Tesco and Iceland slash price of Xmas treats like Heroes and Lindt by up to 50%
','2021-12-29','The Sun','money'),
    ('https://www.thesun.co.uk/news/17096917/ghislaine-maxwell-guilty-of-grooming-girls/
','EVIL PREDATOR Ghislaine Maxwell GUILTY of grooming girls for paedo Jeffrey Epstein to abuse in sex-trafficking trial
','2021-12-29','The Sun','crime');
    ''')
    cursor.execute("COMMIT;") 

#######################
DATABASE = "sun"

DATABASE_IP = str(os.environ['DATABASE_IP'])

DATABASE_USER = "root"
DATABASE_USER_PASSWORD = "root"
DATABASE_PORT=3306

not_connected = True

while(not_connected):
	try:
		print(DATABASE_IP,"IP")
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		not_connected = False

	except Exception as e:
		time.sleep(3)
		print(e, "error!!!")
		print("can't connect to mysql server, might be intializing")
		
cursor = db_connection.cursor()

try:
	cursor.execute(f"USE {DATABASE}")
	print(f"Database: {DATABASE} already exists")
except Exception as e:
    create_database(db_connection,DATABASE,cursor)
    insert_data(cursor)
    print(f"Succesfully created: {DATABASE}")
