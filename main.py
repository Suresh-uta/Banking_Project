import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Suresh@11',database='BANK_MANAGMENT')

def OpenAcc():
    n=input("Enter The Name: ")
    s=input("Enter the ssn: ")
    ac=input ("Enter The Account No: ")
    date=input ("Enter The Date : ")
    br=input ("Enter The branch: ")
    cn=input ("Enter The Contact Number: ")
    ob=int (input ("Enter The Opening Balance: "))
    data1=(ac, ob,date, br )
    data2= (s,n,cn)
    sql1=('insert into Account values (%s,%s,%s,%s)')
    sql2=('insert into people values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x .execute(sqL2,data2)
    mydb.commit()
    print ("Data Entered Successfully..")
    main()

def DepoAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac = input("Enter The Account No: ")
    a='select balance from amount where AccNO=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=resutt[0]+amount
    sql=('update amount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WITHDRAWAMOUNT():
     amount = input("Enter the amount you want to withdraw: ")
     ac = input("Enter The Account No: ")
     a = 'select balance from amount where AccNO=%s'
     data = (ac,)
     x = mydb.cursor()
     x.execute(a, data)
     result = x.fetchone()
     t = result[0]-amount
     sql = ('update amount set balance where AccNo=%s')
     d = (t, ac)
     x.execute(sql, d)
     mydb.commit()
     main()

def BalEnq():
     ac=input("Enter the account no: ")
     a = 'select * from amount where AccNo =%s'
     data=(ac,)
     x=mydb.cursor()
     x.execute(a,data)
     result=x.fetchone()
     print("Balance for account: ", ac, "is", result[-1])
     main()

def DisDetails():
    ac = input("Enter the account no: ")
    a = 'select * from amount where AccNo =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
       print(i)
    main()

def CloseAcc():
    ac = input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where  AccNo=%s'
    data = (ac,)
    x=mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.comnit()
    main()




def main():
       print('''  
                  1. OPEN NEW ACCOUNT
                  2. DEPOSIT AMOUNT
                  3. WITHDRAW AMOUNT
                  4. BALANCE ENQUIRY
                  5. DISPLAY CUSTOMER DETAILS
                  6. CLOSE AN ACCOUNT''')
       choice =input("Enter The Task You Want To Perform:")
       if (choice=='1'):
           OpenAcc()
       elif (choice=='2'):
           DespoAmo()
       elif (choice=='3'):
           WithdrawAmount()
       elif (choice=='4'):
           BalEnq()
       elif (choice=='5'):
          DisDetails()
       elif (choice=='6'):
          CloseAcc()
       else:
          print("invalid choice")
          
main()

