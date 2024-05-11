import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="bank")
def openacc():
    n = input("Enter Name = ")
    ac = input("Enter Account Number = ")
    db = input("Enter D.O.B = ")
    p = input("Enter Phone Number = ")
    ad = input("Enter Assress = ")
    ob = input("Enter Opening Balance = ")
    data1=(n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    ok1 = "insert into sql1 values(%s,%s,%s,%s,%s,%s)"
    ok2 = "insert into sql2 values(%s,%s,%s)"
    c = con.cursor()
    c.execute(ok1,data1)
    c.execute(ok2,data2)
    con.commit()
    print("Data Is Saved")
    main()
# openacc()

def depoamo():
    am = input("Enter Amount = ")
    ac = input("Enter Account No. = ")
    a = "select balance from sql2 where ac = %s"
    data=(ac)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0]+am
    sql = "update sql2 set balance = %s where ac = %s"
    d = (tam,ac)
    c.execute(sql,d)
    con.commit()
    main()
# depoamo()

def witham():
    am = input("Enter Amount = ")
    ac = input("Enter Account No. = ")
    a = "select balance from amount where ac = %s"
    data=(ac)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0]-am
    sql = "update sql2 set balance = %s where ac = %s"
    d = (tam,ac)
    c.execute(sql,d)
    con.commit()
    main()
# witham()

def balance():
    ac = input("Enter Account No. = ")
    a = "select balance from amount where ac = %s"
    data=(ac)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance For Account No:",ac,"is",myresult[0])
    main()
# balance()

def dispacc():
    ac = input("Enter Account No. = ")
    a = "select balance from amount where ac = %s"
    data=(ac)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()
# dispacc()



def main():
    print("""1.Open New Account
          2.Deposit Amount
          3.Withdraw Amount
          4.Balance Enquiry
          5.Display Customer Details
          """)
    choice = input("Enter Choice = ")
    while True:
        if(choice == '1'):
            openacc()
        elif(choice == '2'):
            depoamo()
        elif(choice == '3'):
            witham()
        elif(choice == '4'):
            balance()
        elif(choice == '5'):
            dispacc()
        else:
            print("Wrong Choice................")
            main()
main()

    
    



# cur=con.cursor()  
# name=(input("Enter Name = "))
# ac=(input("Enter Account Number = "))
# pn=(input("Enter Mobile Number = "))
# ob=(input("Enter Opning blance = "))
