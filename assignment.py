import psycopg2
#connecting to database
DB_NAME="library"
DB_USER="postgres"
DB_PASS="Aditya0903$%"
DB_HOST="localhost"
DB_PORT="5432"
con=psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)

#Creating a cursor object
cursor=con.cursor()

#Admin login
def admin_login():
    user_name=input("enter name\t")
    passw=input("enter pass\t")
    user_type="admin"
    #Checking if admin login is avilable in the database
    query='select exists(select * from users where user_name=%s and password=%s and user_type=%s)'
    cursor.execute(query,(user_name,passw,user_type))
    result=(cursor.fetchall())
    if result[0][0]==True:
        print("Admin login Sucessfully")
    else:
        print("Admin not found")
        return
    #Listing the user
    action_=input("Enter 'user' to list the users and 'books' to list all the books")
    if action_=='user':
        query_1='select * from users'
        cursor.execute(query_1)
        result_1=cursor.fetchall()
        for row in result_1:
            print("User_id=",row[0])
            print("User_name=",row[1])
            print("User_type=",row[3])
            print("\n")
    #Listing the books
    else:
        query_1='select * from books'
        cursor.execute(query_1)
        result_1=cursor.fetchall()
        for row in result_1:
            print("Book_id=",row[0])
            print("Book_name=",row[1])
            print("Book_author=",row[2])
            print("No of copies=",row[3])
            print("\n")
        
    return
#User login
def user_login():
    user_name=input("enter name\t")
    passw=input("enter pass\t")
    user_type="user"
    query='select exists(select * from users where user_name=%s and password=%s and user_type=%s)'
    cursor.execute(query,(user_name,passw,user_type))
    result=(cursor.fetchall())
    if result[0][0]==True:
        print("User login Sucessfully")
    else:
        print("User not found")
        return
    book_search=input("Enter the name of the book you want to borrow\t")
    query_2="SELECT book_id,book_name,book_author,no_of_copies FROM books WHERE book_name LIKE %s "
    cursor.execute(query_2,(book_search,))
    con.commit()
    result_1=cursor.fetchall()
    print(result_1)
    for row in result_1:
        print("Book_id=",row[0])
        print("Book_name=",row[1])
        print("Book_author=",row[2])
        print("No of copies=",row[3])
        print("\n")
        

 #New Registration   
def register():
    user_name=input("Enter your name\t")
    user_password=input("Ener your password\t")
    user_type='user'
    user_id='5'
    query="Insert into users(user_id,user_name,password,user_type) values(%s,%s,%s,%s)"
    cursor.execute(query,(user_id,user_name,user_password,user_type))
    con.commit()
    print("User added sucessfully")
    return

if __name__=='__main__':
    while(True):
        action=input("Do you want to Login or Register?\t")
        if action=='Login':
            specigic_login=input("Admin or User\t")
            if specigic_login=='Admin':
                admin_login()
            else:
                user_login()
        else:
            register()