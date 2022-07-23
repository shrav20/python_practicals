import mysql.connector
db=mysql.connector.connect(host="localhost",user="Shravani",password="Shauv@20",database="my_db")
print(db)
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS student") #This drops the table and replaces it
query="""CREATE TABLE Student2(PRN VARCHAR(30),
NAME VARCHAR(20),middlename VARCHAR(20), Surname VARCHAR(20),address VARCHAR(30),mobilenum VARCHAR(20),emailid VARCHAR(20),DOB date,
AGE INT, )"""
cursor.execute(query)
choice=input("ENTER OPERATION TO PERFORM, INSERT ,UPDATE ,DELETE ,EXIT----> ")
print()
while choice!="EXIT":
    
    if choice=="INSERT":
        
        #INSERTING VALUES
        query="""INSERT INTO Student2(PRN,NAME,SURNAME,AGE)
                VALUES(%s, %s, %s, %s )"""
        val=int(input("PRESS 1 if you want to add more data or PRESS 0 to exit: "))
        print()
        while val!=0:
            records_to_insert = [input("ENTER NAME: "),input("ENTER SURNAME: "),int(input("ENTER AGE: ")),input("ENTER PRN: ")]
            print()
            cursor.execute(query,records_to_insert)
            val=int(input("PRESS 1 if you want to add more data or PRESS 0 to exit: "))
            db.commit()
    elif choice=="UPDATE":
        
        #UPDATE
        P=input("ENTER PRN of STUDENT---> ")
        #changing Age
        A=int(input("ENTER NEW AGE---> "))
        query="update Student2 set AGE={0} where PRN={1}".format(A,P)
        cursor.execute(query)
        db.commit()

    elif choice=="DELETE":
        #DELETE
        P=int(input("ENTER PRN OF STUDENT TO BE DELETED: "))
        query="delete from Student2 where PRN={0}".format(P)
        cursor.execute(query)
        db.commit()
        
        
        
    choice=input("ENTER OPERATION TO PERFORM, INSERT ,UPDATE ,DELETE ,EXIT----> ")
    print()
    

db.close()
