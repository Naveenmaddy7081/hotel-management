from tkinter import *
import pymysql
from tkinter import messagebox,filedialog
from  tkinter import ttk
from datetime import datetime


taz=Tk()
width=taz.winfo_screenwidth()
#print(width)
height=taz.winfo_screenheight()
#print(height)
## data base connection
tazTV=ttk.Treeview(height=10,columns=('item name''rate','type'))
tazTV1=ttk.Treeview(height=10,columns=('Date''name','type','rate','total'))

## for char input
def only_char_input(P):
    if P.isalpha() or P=='':
        return True
    return False
callback=taz.register(only_char_input)
## for digit input
def only_numeric_input(P):
    if P.isdigit() or P=='':
        return True
    return False
callback2=taz.register(only_numeric_input)

def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="my hotel")
    mycursor=conn.cursor()
### clear screen
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()

### log out
def logout():
    clear_screen()
    mainheading()
    loginwindow()
def mainheading():
    label=Label(taz,text='Hotel Taz Management ',fg='blue',bg='yellow',
                font=('arial',40,'bold'),padx=500,pady=0)
    label.grid(row=0,columnspan=4)

usernameVar=StringVar()
passwordVar=StringVar()

def loginwindow():
    usernameVar.set('')
    passwordVar.set('')
    labellogin=Label(taz,text='Admin Login ',fg='red', font=('arial',30,'bold'))
    labellogin.grid(row=1,column=1, columnspan=2,padx=60,pady=20)

    usernamelabel=Label(taz,text='User Name',font=('arial',15,'bold'))
    usernamelabel.grid(row=2,column=1,padx=30,pady=10)

    passwordlabel = Label(taz, text='User Password',font=('arial',15,'bold'))
    passwordlabel.grid(row=3, column=1, padx=30, pady=10)

    usernameEntry=Entry(taz,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=2,padx=30,pady=10)

    passwordEntry=Entry(taz,show='*',textvariable=passwordVar)
    passwordEntry.grid(row=3,column=2,padx=30,pady=10)

    loginButton=Button(taz,text='Login',width=20,height=2,fg='green',bd=5,command=adminlogin)
    loginButton.grid(row=4, column=1,columnspan=2, padx=30, pady=10,)

def welcomewindow():
    clear_screen()
    mainheading()
    welcome = Label(taz, text='Welcome Login ', fg='red', font=('arial', 30, 'bold'))
    welcome.grid(row=1, column=1, columnspan=2, padx=60, pady=20)

    logoutButton = Button(taz, text='Logout', width=20, height=2, fg='green', bd=5, command=adminlogin)
    logoutButton.grid(row=4, column=1, columnspan=2, padx=30, pady=10, )

    managementRest = Button(taz, text='Manage Hotel', width=20, height=2, fg='green', bd=2, command=additemwindow)
    managementRest.grid(row=5, column=1, columnspan=2, padx=30, pady=10, )

    billGen = Button(taz, text='Bill Generation', width=20, height=2, fg='red', bd=10, command=billwindow)
    billGen.grid(row=6, column=1, columnspan=2, padx=30, pady=10, )


itemnameVar=StringVar()
itemrateVar=StringVar()
itemtypeVar=StringVar()
#3 back
def back():
    clear_screen()
    mainheading()
    welcomewindow()

###### bill window
global x
x=datetime.now()
datetimeVar=StringVar()
datetimeVar.set(x)
custmernameVar=StringVar()
mobileVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
cost=StringVar()
qtyvariable=StringVar()

######## combodata
def combo_input():
    dbconfig()
    mycursor.execute('select item_name from itemlist')
    data=[]
    for row in mycursor.fetchall():
        data.append(row[0])
    return data
####### optionCallBack
def optionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    #print(itemname)
    aa=ratelist()
    print(aa)
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j
##### otion call back2
def optionCallBack2(*args):
    global qty
    qty=qtyvariable.get()
    final=int(v)*int(qty)
    cost.set(final)
##### ratelist
def ratelist():
    dbconfig()
    que2='select item_rate from itemlist where item_name=%s'
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    print(data)
    return data
##########
def billwindow():
    clear_screen()
    mainheading()
    billitem = Label(taz, text='Generate bill ', fg='red', font=('arial', 30, 'bold'))
    billitem.grid(row=1, column=1, columnspan=2, padx=60, pady=20)

    logoutButton = Button(taz, text='Logout', width=20, height=2, fg='green', bd=5, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1, )

    backButton = Button(taz, text='Back', width=20, height=2, fg='green', bd=5, command=back)
    backButton.grid(row=4, column=0, columnspan=1, )

    printButton = Button(taz, text='Print Bill', width=20, height=2, fg='green', bd=5, command=printbill)
    printButton.grid(row=5, column=0, columnspan=1, )

    datetimelabel=Label(taz,text='Date & Time',font=('arial', 15, 'bold'))
    datetimelabel.grid(row=2,column=1,padx=20,pady=5)

    datetimeEntry=Entry(taz,textvariable=datetimeVar,font=('arial', 15, 'bold'))
    datetimeEntry.grid(row=2, column=2, padx=20, pady=5)

    custmernamelabel = Label(taz, text='Custmer Name', font=('arial', 15, 'bold'))
    custmernamelabel.grid(row=3, column=1, padx=20, pady=5)

    custmernameEntry = Entry(taz, textvariable=custmernameVar, font=('arial', 15, 'bold'))
    custmernameEntry.grid(row=3, column=2, padx=20, pady=5)
    custmernameEntry.configure(validate='key', validatecommand=(callback, '%P'))

    mobilelabel = Label(taz, text='Contact No', font=('arial', 15, 'bold'))
    mobilelabel.grid(row=4, column=1, padx=20, pady=5)

    mobileEntry = Entry(taz, textvariable=mobileVar, font=('arial', 15, 'bold'))
    mobileEntry.grid(row=4, column=2, padx=20, pady=5)
    mobileEntry.configure(validate='key', validatecommand=(callback2, '%P'))

    selectlabel = Label(taz, text='Select Item', font=('arial', 15, 'bold'))
    selectlabel.grid(row=5, column=1, padx=20, pady=5)

    l=combo_input()
    c=ttk.Combobox(taz,values=l,textvariable=combovariable,font=('arial', 15, 'bold'))
    c.set('Select Item')
    combovariable.trace('w',optionCallBack)
    c.grid(row=5,column=2,padx=20,pady=5)

    ratelabel = Label(taz, text='Item Rate', font=('arial', 15, 'bold'))
    ratelabel.grid(row=6, column=1, padx=20, pady=5)

    rateEntry = Entry(taz, textvariable=baserate, font=('arial', 15, 'bold'))
    rateEntry.grid(row=6, column=2, padx=20, pady=5)

    qtylabel = Label(taz, text='Select Quantity', font=('arial', 15, 'bold'))
    qtylabel.grid(row=7, column=1, padx=20, pady=5)

    global qtyvariable
    l2 = [1,2,3,4,5]
    qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable, font=('arial', 15, 'bold'))
    qty.set('Select Quantity')
    qtyvariable.trace('w', optionCallBack2)
    qty.grid(row=7, column=2, padx=20, pady=5)

    costlabel = Label(taz, text='Cost', font=('arial', 15, 'bold'))
    costlabel.grid(row=8, column=1, padx=20, pady=5)

    costEntry = Entry(taz, textvariable=cost, font=('arial', 15, 'bold'))
    costEntry.grid(row=8, column=2, padx=20, pady=5)

    billbutton=Button(taz,text='Save Bill',width=20,height=2,bd=10,fg='red',bg='yellow',command=savebill)
    billbutton.grid(row=9,column=2,padx=20,pady=5)
#########save bill
def savebill():
    dt=datetimeVar.get()
    custname=custmernameVar.get()
    mobile=mobileVar.get()
    item_name=itemname
    itemrate=v
    itemqty=qtyvariable.get()
    total=cost.get()
    dbconfig()
    insqu="insert into bill(datetime,custmer_name,contact_no,item_name,item_rate,item_qlt,cost)"\
    "values(%s,%s,%s,%s,%s,%s,%s)"
    val=(dt,custname,mobile,item_name,itemrate,itemqty,total)
    mycursor.execute(insqu,val)
    conn.commit()
    messagebox.showinfo('save data ','bill saved successfully')
    custmernameVar.set('')
    mobileVar.set('')
    itemnameVar.set('')
    cost.set('')

##### print
def printbill():
    clear_screen()
    mainheading()
    printitem = Label(taz, text='Bill Details ', fg='green', font=('arial', 30, 'bold'))
    printitem.grid(row=1, column=1, columnspan=2, padx=60, pady=20)

    logoutButton = Button(taz, text='Logout', width=20, height=2, fg='green', bd=5, command=logout)
    logoutButton.grid(row=1, column=0, columnspan=1, )

    backButton = Button(taz, text='Back', width=20, height=2, fg='green', bd=5, command=back)
    backButton.grid(row=1, column=3, columnspan=1, )

    clickbutton = Button(taz, text='Double Click To Treeview Print Bill ', fg='green', font=('arial', 30, 'bold'))
    clickbutton.grid(row=2, column=1, columnspan=3, padx=40, pady=20)

    ###triview
    tazTV1.grid(row=5, column=0, columnspan=4)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure('Treeview', fieldbackground='green')
    scrollbarr = Scrollbar(taz, orient='vertical', command=tazTV.yview)
    scrollbarr.grid(row=5, column=5, sticky='NSE')

    tazTV1.configure(yscrollcommand=scrollbarr.set)
    tazTV1.heading('#0', text='Date/time')
    tazTV1.heading('#1', text='name')
    tazTV1.heading('#2', text='mobile')
    tazTV1.heading('#3', text='Selected Food')
    tazTV1.heading('#4', text='total Cost')
    displaybill()


########### display bill #####
def displaybill():
    # to delet already insterted data
    records = tazTV1.get_children()
    for x in records:
        tazTV1.delete(x)

    conn = pymysql.connect(host='localhost', user='root', db='my hotel')
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query1 = 'select * from bill'
    mycursor.execute(query1)
    data = mycursor.fetchall()
    # print(data)
    for row in data:
        tazTV1.insert('', 'end', text=row['datetime'], values=(row['custmer_name'], row['contact_no'],row['item_name'],row['item_qlt'],row['cost']))
    conn.close()
    tazTV1.bind('<Double-1>', OnDoubleClick2)

#######OnDoubleClick2
def OnDoubleClick2(event):
    item = tazTV1.selection()
    global itemnameVar11
    itemnameVar11 = tazTV1.item(item, 'text')
    item_detail1 = tazTV1.item(item, 'values')
    receipt()

####### receipt
def receipt():
    billstring=''
    billstring+='=====My Hotel Bill=====\n\n'
    billstring += '=====Custmer Details=====\n\n'
    dbconfig()
    query='select * from bill where datetime="{}";'.format(itemnameVar11)
    mycursor.execute(query)
    data=mycursor.fetchall()
    print(data)
    for row in data:
        billstring+="{}{:<20}{:<10}\n".format('date/Time','',row[1])
        billstring += "{}{:<20}{:<10}\n".format('Custmer Name', '', row[2])
        billstring += "{}{:<20}{:<10}\n".format('Contact No', '', row[3])
        billstring += "\n======= Item Details ======\n"
        billstring +="{:<15}{:<15}{:<15}{:<15}".format('Item Name','Rate','Quantity','Total Cost')
        billstring+="\n{:<10}{:<10}{:<25}{:<25}".format(row[4],row[5],row[6],row[7])
        billstring+="===============================\n"
        billstring+="{}{:<10}{:<15}{:<10}\n".format('Total Cost','','',row[7])
        billstring+="\n\n ========== Thanks Please Visit Again ==========\n"
    billfile=filedialog.asksaveasfile(mode='w',defaultextension='.text')
    if billfile is None:
        messagebox.showerror('File Name Error','Invalid File Name')
    else:
        billfile.write(billstring)
        billfile.close()


########







def additemwindow():
    clear_screen()
    mainheading()
    additem = Label(taz, text='Insert Item ', fg='red', font=('arial', 30, 'bold'))
    additem.grid(row=1, column=1, columnspan=2, padx=60, pady=20)

    itemnamelabel=Label(taz,text='Item Name',font=('arial', 30, 'bold'))
    itemnamelabel.grid(row=2,column=1,padx=20,pady=5)

    itemratelabel = Label(taz, text='Item Rate', font=('arial', 30, 'bold'))
    itemratelabel.grid(row=3, column=1, padx=20, pady=5)

    itemtypelabel = Label(taz, text='Item type', font=('arial', 30, 'bold'))
    itemtypelabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry=Entry(taz,textvariable=itemnameVar)
    itemnameEntry.grid(row=2,column=2,padx=20,pady=5)
    # for validation
    itemnameEntry.configure(validate='key',validatecommand=(callback,'%P'))

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate='key', validatecommand=(callback2, '%P'))

    itemtypeEntry = Entry(taz, textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4, column=2, padx=20, pady=5)
    itemtypeEntry.configure(validate='key', validatecommand=(callback, '%P'))

    additembutton=Button(taz,text='Add Item',width=20,height=2,fg='green',bd=5,command=additemprocess)
    additembutton.grid(row=3,column=3,columnspan=1)

    updatebutton=Button(taz, text='Update', width=20, height=2, fg='green', bd=5, command=updateitem)
    updatebutton.grid(row=4, column=3, columnspan=1)

    deletbutton = Button(taz, text='delete', width=20, height=2, fg='green', bd=5, command=deletitem)
    deletbutton.grid(row=5, column=3, columnspan=1)

    logoutButton = Button(taz, text='Logout', width=20, height=2, fg='green', bd=5, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1, )

    backButton = Button(taz, text='Logout', width=20, height=2, fg='green', bd=5, command=back)
    backButton.grid(row=3, column=0, columnspan=1, )
####
    tazTV.grid(row=8,column=0,columnspan=3)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure('Treeview',fieldbackground='green')
    scrollbarr=Scrollbar(taz,orient='vertical',command=tazTV.yview)
    scrollbarr.grid(row=8,column=2,sticky='NSE')

    tazTV.configure(yscrollcommand=scrollbarr.set)
    tazTV.heading('#0',text='item name')
    tazTV.heading('#1', text='rate')
    tazTV.heading('#2', text='type')

    getItemInTreeview()



def additemprocess():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    query='insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)'
    val=(name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo('save item','item saved successfully')
    itemnameVar.set('')
    itemrateVar.set('')
    itemtypeVar.set('')
    getItemInTreeview()

########
def getItemInTreeview():
    # to delet already insterted data
    records=tazTV.get_children()
    for x in records:
        tazTV.delete(x)

    conn=pymysql.connect(host='localhost',user='root',db='my hotel')
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    query1='select * from itemlist'
    mycursor.execute(query1)
    data=mycursor.fetchall()
    #print(data)
    for row in data:
        tazTV.insert('','end',text=row['item_name'],values=(row['item_rate'],row['item_type']))
    conn.close()
    tazTV.bind('<Double-1>',OnDoubleClick)


########## doubleclick
def OnDoubleClick(event):
    item=tazTV.selection()
    itemnameVar1=tazTV.item(item,'text')
    item_detail = tazTV.item(item, 'values')
    itemnameVar.set(itemnameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])

#############
### update
def updateitem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que='update itemlist set item_rate=%s,item_type=%s where item_name=%s'
    val=(rate,type,name)
    mycursor.execute(que,val)
    conn.commit()
    messagebox.showinfo('updation confirmation','Item updated successfully')
    itemnameVar.set('')
    itemrateVar.set('')
    itemtypeVar.set('')
    getItemInTreeview()
##### delete item
def deletitem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que1='delete from  itemlist where item_name=%s'
    val=(name)
    mycursor.execute(que1,val)
    conn.commit()
    messagebox.showinfo('delete confirmation','Item deleted successfully')
    itemnameVar.set('')
    itemrateVar.set('')
    itemtypeVar.set('')
    getItemInTreeview()


def adminlogin():
    dbconfig()
    username=usernameVar.get()
    password=passwordVar.get()
    que='select * from user_info where user_id=%s and user_pass=%s'
    val=(username,password)
    mycursor.execute(que,val)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True
    conn.close()
    if flag==True:
        welcomewindow()
    else:
        messagebox.showerror('Invalid user credential','Either user name or password incorrect')
        usernameVar.set('')
        passwordVar.set('')
mainheading()
loginwindow()

taz.title('hotel taz management system')
taz.geometry('%dx%d+0+0'%(width,height))
taz.mainloop()




