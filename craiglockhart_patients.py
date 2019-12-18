import sqlite3

while True:
    try:
        sqliteConnection = sqlite3.connect('craiglockhart.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        with open('craiglockhart.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()

        cursor.executescript(sql_script)
        print("SQLite script executed successfully")

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
        
    print("\n")
    print('^'*80)
    print("\n")
    print("# Copyright 2019 Yoana Stankova")
    print('\n')
    print ('-'*80)
    print('Craiglockhart Mental Hospital'.title())
    print("\n")
    print ('^'*80)
    print ("Welcome to Craiglockhart Mental Hospital.") 
    print ('\n')
    instr = input("Would you like to see a guide on how to use the system?")
    print('\n')
    if instr == "yes":
        print ("If you would like to find records of doctors, type in 'doctors, for patients - 'patients'.")
        print ("All of our staff and patients are assigned unique ids. If you want to conduct a search by id, type 'patient/doctor-id'. If you want to search by first/last name, age, diagnosis, military status, social status, or occupation, make sure to type in the key word, putting a hyphen in two word phrases, e.g.'first-name'.")
    elif instr == "no":
        print("Then you can start using our system.")
        print("If you are stuck at some point, just type in 'instructions'.")
    else:
        print ("Invalid input. Returning to main screen...")
    print('\n')
    anw = input("Enter query:")
    print('\n')
    if anw == "instructions":
        print ("If you would like to find records of doctors, type in 'doctors, for patients - 'patients'.")
        print ("All of our staff and patients are assigned unique ids. If you want to conduct a search by id, type 'patient/doctor-id'. If you want to search by first/last name, age, diagnosis, military status, social status, or occupation, make sure to type in the key word, putting a hyphen in two word phrases, e.g.'first-name'.") 
    elif anw == "patients":
        sqlite_select_query = """SELECT * from patients"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "doctors":
        sqlite_select_query = """SELECT * from doctors"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("id: ", row[0])
            print("Name: ", row[1]) 
            print("Age: ", row[2])
            print("Occupation: ", row[3])
            print("\n")
    elif anw == "layard" or "Layard" or "john" or "John":
        sqlite_select_query = """SELECT * from patients WHERE id=1"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "siegfried" or "Siegfried" or "sassoon" or "Sassoon":
        sqlite_select_query = """SELECT * from patients WHERE id=2"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "burns" or "Burns" or "david" or "David":
        sqlite_select_query = """SELECT * from patients WHERE id=3"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "prior" or "Prior" or "billy" or "Billy":
        sqlite_select_query = """SELECT * from patients WHERE id=4"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "anderson" or "Anderson" or "ralph" or "Ralph":
        sqlite_select_query = """SELECT * from patients WHERE id=5"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    elif anw == "willard" or "Willard":
        sqlite_select_query = """SELECT * from patients WHERE id=6"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("id: ", row[0])
            print("First Name: ", row[1]) 
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Diagnosis: ", row[4])
            print("Military Status: ", row[5])
            print("Social Status: ", row[6])
            print("Occupation: ", row[7])
            print("\n")
    
    else:
        print ("Invalid input. Returning to main screen...")
        continue
    print ('\n')
