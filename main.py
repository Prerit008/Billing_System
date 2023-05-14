import sqlite3 as sqlt
from datetime import date

conn = sqlt.connect("ebs.sql")
cur = conn.cursor()
cur.execute(
  "CREATE TABLE IF NOT EXISTS consumer(acc_no int(4) PRIMARY KEY,name varchar(255) ,addr varchar(255), contact int(10), P_cost int(20));"
)
conf = 'Successfull Login!'
cur.execute('SELECT acc_no FROM consumer')
records = cur.fetchall()


def login(user, passwd):
  if user == '1':
    if passwd == '1':
      return conf
    else:
      print("Incorrect username or password!!")
  else:
    print('Incorrect username or password!!')


def list_consumers():
  print('_________________________________________________')
  print('List of All Consumers')
  cur.execute('SELECT * FROM consumer')
  records = cur.fetchall()
  for record in records:
    print(record)


def add_consumer():
  print('_________________________________________________')
  print('Add a Consumer')
  vacc_no = int(input("Enter Account No.:"))
  vname = input("Enter Name of Consumer:")
  vaddr = input("Enter Address of Consumer:")
  vcontact = int(input("Enter a contact no of Consumer:"))
  vP_cost = int(input("Enter Power Consumption(in Watt):"))
  cur.execute("INSERT INTO consumer (acc_no, name, addr, contact, P_cost) VALUES(?,?,?,?,?)",(vacc_no, vname, vaddr, vcontact, vP_cost))
  conn.commit()


def del_consumer(del_acc):
  print('_________________________________________________')
  print('Deleting account', del_acc)
  if (del_acc, ) in records:
    cur.execute("DELETE FROM consumer WHERE acc_no = ?", (del_acc, ))
    conn.commit()
    print("Consumer Account Deleted Successfully")
  else:
    print("This account doesn't exist !")


def modify_consumer(pk):
  print('_________________________________________________')
  print('Modifing account', pk)
  if (pk, ) in records:
    vname = input("Enter Name of Consumer:")
    vaddr = input("Enter Address of Consumer:")
    vcontact = int(input("Enter a contact no of Consumer:"))
    vP_cost = int(input("Enter Power Consumption(in Watt):"))
    cur.execute("DELETE FROM consumer WHERE acc_no = ?", (pk, ))
    cur.execute(
      "INSERT INTO consumer (acc_no, name, addr, contact,P_cost) VALUES(?,?,?,?,?)",
      (pk, vname, vaddr, vcontact, vP_cost))
    conn.commit()
  else:
    print("This account doesn't exist !")


def generate_bill(a):
  rate = int(input("Enter the Rate of Power:"))
  print('\n\n\n______________________________________________')
  print("""______Uttar Pradesh Electrical Deparment______
__________Contact No.:+91-0000000000__________""")
  if (a, ) in records:
    cur.execute('SELECT acc_no, name, addr, contact, P_cost FROM consumer')
    for i in cur.fetchall():
      if i[0] == a:
        today = date.today()
        day = 1
        month = today.month
        year = today.year
        Date = "{}-{}-{}".format(day, month, year)
        print(
          '\n Account No.:', i[0], '\n Account Name:', i[1], '\n Address:',
          i[2], '\n Date:', today, '\n Consumer Contact:', i[3],
          '\n Meter Info:',
          '\n ---------------------------------------------- \n',
          '  Date      Usage    Cost(per kWh)    Amount',
          '\n ---------------------------------------------- \n',
          "{}    {}           {}           {}".format(Date, i[4], rate,
                                                      i[4] * rate),
          '\n ---------------------------------------------- \n',
          '\n Bill Summary:\n', 'Total Due :', i[4] * rate, '\n', "Due Date:",
          "{}-{}-{}".format(30, month, year), '\n', "E&OE", '\n',
          "FOR Uttar Pradesh Electrical Department",
          '\n ---------------------------------------------- \n\n\n')


print('_______Uttar Pradesh Electrical Department_______')
print('_____________Username:1 | Password:1_____________')
print('_________________________________________________')
username = input("Enter UserName:")
password = input("Enter PassWord:")
a = login(username, password)
menu = "\n 1. List of all consumers\n 2. Add a consumer\n 3. Delete a consumer\n 4. Modify a consumer\n 5. Generate Bill for a consumer\n 6. Logout"
if a == conf:
  print('_________________________________________________\n')
  print(conf)
  ask = 1
  while ask != 6:
    print(menu)
    ask = int(input("\nChoose the task :"))
    if ask == 1:
      list_consumers()
    elif ask == 2:
      add_consumer()
    elif ask == 3:
      del_acc = int(input("Enter account no which is to be deleted:"))
      del_consumer(del_acc)
    elif ask == 4:
      pk = int(input("Enter account no which is to be modified:"))
      modify_consumer(pk)
    elif ask == 5:
      billing_acc = int(input("Enter account no which is to be evaluated:"))
      generate_bill(billing_acc)
    elif ask == 6:
      print('_________________________________________________')
      print('Successfully Logout!')
    else:
      print('_________________________________________________')
      print('Please Choose appropriate Choices given above!')
