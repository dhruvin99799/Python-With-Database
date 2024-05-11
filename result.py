class option():
    def option1(s):
        # Inseart Quary
        import mysql.connector
        con = mysql.connector.connect(host="localhost",user="root",password="",database="python")
        cur = con.cursor()
        name=(input("Enter Name = "))
        english=(input("Enter Subject-1= "))
        maths=(input("Enter Subject-2= "))
        eco=(input("Enter Subject-3= "))
        computer=(input("Enter Subject-4= "))
        prectical=(input("Enter Subject-5= "))
        # sql = "insert into result(name,english,maths,eco,computer,prectical) values(%d,%d,%d,%d,%d,%d)"
        # cur.execute(sql,(name,english,maths,eco,computer,prectical))
        # total=sum(english,maths,eco,computer,prectical)
        maximum=max(english,maths,eco,computer,prectical)
        minimum=min(english,maths,eco,computer,prectical)
        sql = "insert into result(name,english,maths,eco,computer,prectical,maximum,minimum) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql = "insert into students(name,email,password,contact)"
        cur.execute(sql,(name,english,maths,eco,computer,prectical,maximum,minimum))
        con.commit()
obj = option()
obj.option1()