import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="python")
obj = con.cursor()

class register:
        
    ifsc=acn=pin=em=nm=None
    blc=0
    def __init__(self,obj,log):
        self.obj = obj
        self.log = log
        
    def selc(self,acn):
        sql = "SELECT * FROM `bank_account` WHERE `account_number`=%s"
        self.obj.execute(sql,(acn,))
        row = self.obj.fetchone()
        return row
        
    def account_number(self):
        acn = input('Enter account number : ')
        row = self.selc(acn)
        if row==None:
            return acn
        elif row!=None:
            print('Invalid account number !')
            acn = self.account_number()
        else:
            print('Invalid account number !')
    
    def balance_ac(self):
        print('\nAccount balance should be >2000 !\n')
        amount = int(input('Enter opening balance :'))
        if amount>=4000 or len(str(amount))>=4:
            return str(amount)
        else:
            self.balance_ac()
        
    def ins(self,nm,acn,ifsc,pin,blc):
        sql="INSERT INTO `bank_account`(`name`,`balance`, `pin`, `account_number`, `ifsc`)VALUES (%s,%s,%s,%s,%s)"
        self.obj.execute(sql,(nm,blc,pin,acn,ifsc))
        con.commit()
        
    def PIN(self,pin):
        pin = input('Enter 4 digit PIN : ')
        if len(pin)==4:
            print('your PIN setted succesfully !')
            return pin
        else:
            self.PIN(pin)
        
    def get_data(self):
        nm = input('Enter name : ')
        self.acn = self.account_number()
        ifsc = input('Enter IFSC code : ')
        self.pin = self.PIN(self.pin)
        self.blc = str(self.balance_ac())
        self.ins(nm,self.acn,ifsc,self.pin,self.blc)
        print('\nYour account succesfully opened !\nYou are redirecting to Login page !\n')
        self.log.check(self.acn,self.pin)
        self.log.choice()
        
#=================== new login class================
class login:
    
    row = cpin = lacn = None
        
    def __init__(self,obj,con):
        self.obj=obj
        self.con=con
            
    def check(self,lacn,cpin):
        sql = "SELECT * FROM `bank_account` WHERE `account_number`=%s AND `pin`=%s"
        if self.lacn==None and self.cpin==None:
            self.lacn = input('\nEnter your Account number :')
            self.cpin = input('Enter your PIN code :')
            obj.execute(sql,(self.lacn,self.cpin,))
            self.row = self.obj.fetchone()
            if self.row==None:
                print('\nInvalid PIN or Account number !')
                print('Please try again !\n')
                self.cpin=self.lacn=None
                self.row = self.check(self.lacn,self.cpin)
            else:
                print('\nYou Logged in successfully!\n')
                return self.row
        else:
            obj.execute(sql,(lacn,cpin,))
            self.row = self.obj.fetchone()
            if self.row==None:
                print('\nInvalid PIN or Account number !')
                print('Please try again !\n')
                self.row = self.check(lacn,cpin)
            else:
                return self.row
        
    def disp(self):
        row = self.check(self.lacn,self.cpin)
        print('\n1.Details show page...')
        print('\n============Details============\n')
        print('Your Name : ',row[1])
        print('Your Account balance : ',row[2])
        print('Your PIN : ',row[3])
        print('Your Account Number : ',row[4])
        print('Your IFSC : ',row[5])
        print('\n===============================\n\n')
        
    def depo(self):
        print('\n2.Deposit page.....\n')
        row = self.check(self.lacn,self.cpin)
        balance = int(row[2])
        acn = row[4]
        print('Availabl Balance : ',balance)
        d_am = int(input('Enter deposit amount : '))
        balance=str(balance+d_am)
        sql = "UPDATE `bank_account` SET `balance`=%s WHERE `account_number`=%s"
        self.obj.execute(sql,(balance,acn,))
        con.commit()
        print()
        
    def clm(self):
        print('\n3.Widthdraw page...\n')
        row = self.check(self.lacn,self.cpin)
        balance = int(row[2])
        acn = row[4]
        print('Available Balance : ',balance)
        amount = int(input('Enter withdraw amount : '))
        if amount>balance:
            print('\nInsufficient Balance !\n')
            self.clm()
        else:
            balance=str(balance-amount)
            sql = "UPDATE `bank_account` SET `balance`=%s WHERE `account_number`=%s"
            self.obj.execute(sql,(balance,acn,))
            con.commit()
            
    def pinchange(self):
        print('\n4.PIN change page...\n')
        row = self.check(self.lacn,self.cpin)
        pin = row[3]
        acn = row[4]
        cpin = input('Enter your old PIN : ')
        if pin==cpin:
            newpin = input('Enter your new PIN : ')
            sql = "UPDATE `bank_account` SET `pin`=%s WHERE `account_number`=%s"
            self.obj.execute(sql,(newpin,acn,))
            con.commit()
            pin=self.cpin=newpin
            print('\nYour PIN changen successfully !\n')
        else:
            print('\nIncorrect PIN !\n')
            self.pinchange()
    
    def choice(self):
        print('\n1.Show Details\n2.Depostite\n3.Withdraw\n4.Change PIN\n0.Exit\n')
        ch = int(input('Enter your choice : '))
        if ch==1:
            self.disp()
            self.choice()
        elif ch==2:
            self.depo()
            self.choice()
        elif ch==3:
            self.clm()
            self.choice()
        elif ch==4:
            self.pinchange()
            self.choice()
        elif ch==0:
            print('\nLoggin out......')
            self.con.close()
            print('Logged out successfully ! \n\n')


def main():
    print('\n\n1.Login\n2.Register\n')
    l = int(input('Enter your choice : '))
    obj_log = login(obj,con)
    obj_reg = register(obj,obj_log)
    if l==1:
        obj_log.disp()
        obj_log.choice()
    elif l==2:
        obj_reg.get_data()
    else:
        print('\nPlease enter valid choice !\n')
        
main()