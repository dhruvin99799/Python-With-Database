import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="", database="python")


def openAcc():
    n = input("Enter Name : ")
    ac = input("Enter Account No : ")
    p = input("Enter Phone : ")
    ob = int(input("Enter Opening Balance : "))
    data1=(n,ac,p,ob)
    data2=(n,ac,ob)
    sql1=("insert into account(n,ac,p,ob) values(%s,%s,%s,%s)")
    sql2=("insert into amount(n,ac,) values(%s,%s,%s)")
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data Entered Successfully")
    main()


def depoamo():
    am = int(input("Enter Amount : "))
    ac = input("Enter Account No : ")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fethone()
    tam = myresult[0] + am
    sql = "update amount set balance = %s where acno = %s"
    d = (tam, ac)
    c.execute(sql, d)
    con.commit()
    main()


def witham():
    am = int(input("Enter Amount : "))
    ac = input("Enter Account No : ")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fethone()
    tam = myresult[0] - am
    sql = "update amount set balance = %s where acno = %s"
    d = (tam,ac)
    c.execute(sql,d)
    con.commit()
    main()


def balance():
    ac = input("Enter Account No : ")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print("Balance for Account : ", ac, "is ", myresult[0])
    main()


def main():
    print("1.CREATE NEW ACCOUNT")
    print("2.DEPOSIT AMOUNT")
    print("3.WITHDRAW AMOUNT")
    print("4.CHACK BLALNCE")

    choice = input("Enter Task No : ")
    while True:
        if (choice=='1'):
            openAcc()
        elif (choice=='2'):
            depoamo()
        elif (choice=='3'):
            witham()
        elif (choice=='4'):
            balance()
        else:
            print("Wrong choice..........")
            main()


main()
