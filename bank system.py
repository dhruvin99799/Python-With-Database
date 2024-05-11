import mysql.connector as a
con = a.connect(host="localhost", user="root",password="", database="python")


def openAcc():
    name = input("Enter Name : ")
    acno = input("Enter Account No : ")
    pho = input("Enter Phone : ")
    ob = int(input("Enter Opening Balance : "))
    sql1='insert into account(name,acno,pho,ob) values(%s,%s,%s,%s)'
    sql2='insert into amount(name,acno,balance) values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql1,(name,acno,pho,ob))
    c.execute(sql2,(name,acno,ob))
    con.commit()
    print("Data Entered Successfully")
    main()

def depoamo():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    a='select balance from amount where acno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    t=result[0]+am
    sql=('UPDATE amount set balance=%s where acno=%s')
    d=(t,ac)
    c.execute(sql,d)
    con.commit()
    main()

def witham():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    a='select balance from amount where acno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    t=result[0]-am
    sql=('UPDATE amount set balance=%s where acno=%s')
    d=(t,ac)
    c.execute(sql,d)
    con.commit()
    main()


def details():
    ac = input("Enter Account No : ")
    a = "select * from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    result = c.fetchone()
    for i in result:
        print(i)
    main()
    


def main():
    
    print("\n\t\t\t\t***************************")
    print("\n\t\t\t\t        BANK SYSTEM        ")
    print("\n\t\t\t\t***************************")
    
    print("1.CREATE NEW ACCOUNT")
    print("2.DEPOSIT AMOUNT")
    print("3.WITHDRAW AMOUNT")
    print("4.CHACK BLALNCE")
    print("5.EXIT")

    choice = input("\nEnter Any One : ")
    while True:
        if (choice=='1'):
            openAcc()
        elif (choice=='2'):
            depoamo()
        elif (choice=='3'):
            witham()
        elif (choice=='4'):
            details()
        elif(choice=='5'):
            exit()
        else:
            print("/nWrong choice..........")
            main()
main()
