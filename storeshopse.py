#from _typeshed import Self
#from logging import disable
import os
#import tempfile
from tkinter import *
from tkinter import Image,PhotoImage 
from tkinter import ttk
import tkinter as tk
import random
from tkinter import font
#from tkinter.ttk import Notebook
#from typing_extensions import Self
import mysql.connector
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk ,Image
from mysql.connector import cursor

#############################Login page ###############################
x="pink"
y="lightgreen"
cwidth="6"

top = Tk()  
top.config(bg='gray17') 
top.geometry("400x250") 
top.title("Login Page")
top.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')

# login form 
def submitbtn():
    
    dt=""  
    con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
    cmd=con.cursor() 
    email=emailentry.get()
    password=passentry.get()

    #cmd.execute("select * from admin_register where email='"+str(email)+"' and password='"+str(password)+"'")
    cmd.execute("select * from admin_register where email='"+str(email)+"' and password='"+str(password)+"'")
    
    data=cmd.fetchall()
    for row in data:
        dt="%s"%(row[0])             
    # print("value=",dt)  
    if(dt!=""):
        top.iconify()
        masterform()
        
        #result.config(text="")       
    else:
        result.config(text="Invalid Email or Password")
        messagebox.showerror("ERROR","Invalid Email or Password") 

   
    con.commit()  
    con.close() 

email = Label(top, text = "Email")
email.place(x = 30, y = 50)  
 
password = Label(top, text = "Password")
password.place(x = 30, y = 90)

logsubmitbtn = Button(top, text = "Submit",command=submitbtn,bg=x)
logsubmitbtn.place(x = 90, y = 150)

emailentry = Entry(top)
emailentry.insert(0,"hetvi")
emailentry.place(x = 100, y = 50)    
passentry = Entry(top)
passentry.insert(0,"pass")
passentry.place(x = 100, y = 90) 
result=Label(top,text="Display Message")
result.place(x=110,y=190)


######################  Master Page Form ######################
def masterform():
   
   root = Toplevel(top) 
   root.geometry("800x680")
   root.config(bg='gray17')
   root.title("Master Form")
   root.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')
   successlabel=Label(root,text="Master Page",font =('Verdana', 15))
   successlabel.place(x=300,y=60)
   c=Canvas(root,width=630, height=340, bg='gray')
   c.place(x=50,y=190)

   img = ImageTk.PhotoImage(Image.open("C:\\Users\\Acer\\Desktop\\python\\Dmart.png"))  # PIL solution
   c.create_image(0, 0,  anchor=NW, image=img)


   ##############################  product Master  #################################
   menubar=Menu(root)
   def productmaster():
    root.iconify()
    pmaster=Toplevel(root)
    pmaster.geometry("740x600")
    pmaster.title("Product Master")
   
    pmaster.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')
    pmasterlabel=Label(pmaster,text="Product Master",font = ('Verdana',15))
    pmasterlabel.place(x=120,y=25) 

    def saveproductmasterbtn():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        productname=pnameentry.get()
        productprice=ppriceentry.get()
        producttitle=ptitleentry.get()
        productquality=pquantityentry.get()
        productimage= pimageentry.get()
        cmd.execute("insert into product_master values(NULL,curdate(),%s,%s,%s,%s,%s)",(productname,productprice,producttitle,productquality,productimage))  
        msgbox= messagebox.askquestion("Insert Data", "Sure You Want to Add data?")
        if msgbox == 'no':
            msgbox.destroy()
        resultlabelmasterform.configure(text="insert Data successfully...")
        con.commit()  
        con.close()
       
    submitmasterform=Button(pmaster,text="Insert",bg=y,command=saveproductmasterbtn)
    submitmasterform.place(x=50,y=240)

    def updatemasterformbtn():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        pidentry=pentry.get()
        pname=pnameentry.get()
        pprice=ppriceentry.get()
        ptitle=ptitleentry.get()
        pquantity=pquantityentry.get()
        pimage= pimageentry.get()

        cmd.execute("update product_master set cur_date=CURDATE(), pname='"+str(pname)+"', pprice='"+str(pprice)+"', ptitle='"+str(ptitle)+"', pquantity='"+str(pquantity)+"', pimage='"+str(pimage)+"' where id="+str(pidentry))
        resultlabelmasterform.configure(text="data updated.....")
        con.commit()  
        con.close()

    editcustomerform=Button(pmaster,text="update",bg=y,command=updatemasterformbtn)
    editcustomerform.place(x=120,y=240)
    

    def editmasterformbtn():
       
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        pidentry=pentry.get()
        cmd.execute(" select * from product_master where id="+str(pidentry))
        data=cmd.fetchall()
        
        pdataname=""
        pdataprice=""
        pdatatitle=""
        pdataquantity=""
        pdataimage=""
  
        for row in data:
            pdataname="%s" %(row[1])
            pdataprice="%s" %(row[2])
            pdatatitle="%s"%(row[3])
            pdataquantity="%s"%(row[4])
            pdataimage="%s"%(row[5])
  
        #resultlabelcustomerform.configure(text="data updated...")    
        con.commit()  
        pnameentry.insert(0,pdataname)
        ppriceentry.insert(0,pdataprice)
        ptitleentry.insert(0,pdatatitle)
        pquantityentry.insert(0,pdataquantity)
        pimageentry.insert(0,pdataimage)
        con.close()
 
    submitmasterform=Button(pmaster,text="Edit",bg=y,command=editmasterformbtn)
    submitmasterform.place(x=190,y=240)

    def deletebtnclick():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        cidentry=pentry.get()
        cmd.execute("Delete from product_master where id="+str(cidentry))

        resultlabelmasterform.configure(text="Data Delete Succesfully .....")
        con.commit()
        con.close()

    submitmasterform=Button(pmaster,text="Delete",bg=y,command=deletebtnclick)
    submitmasterform.place(x=50,y=290)

    def clearbtnclick():
     con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
     cmd=con.cursor() 
     pnameentry.delete(0, END)
     ppriceentry.delete(0,END)
     ptitleentry.delete(0,END)
     pquantityentry.delete(0,END)
     pimageentry.delete(0,END)  

     resultlabelmasterform.configure(text="Data Clear Succesfully .....")
     con.commit()
     con.close()

    submitmasterform=Button(pmaster,text="clear",bg=y,command=clearbtnclick)
    submitmasterform.place(x=120,y=290)

    def mshowbtnclick():
     
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        cmd.execute("select * from product_master ")
        data=cmd.fetchall()
        total=cmd.rowcount
        resultlabelmasterform.configure(text="Total data entries : "+str(total))
       
        #vertical scroll
        text_scroll=Scrollbar(pmaster)
        text_scroll.pack(side=RIGHT,fill=Y)

        #horizontal Scroll
        horizontaltext_scroll=Scrollbar(pmaster,orient='horizontal')
        horizontaltext_scroll.pack(side=BOTTOM,fill=X)
        

        inputtxt = Text(pmaster, height=7,width=88,bg = "light yellow",yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=horizontaltext_scroll.set)
        inputtxt.place(x=6,y=440)
        
        
        #inputtext.insert(tk.END,Text)
        text_scroll.config(command=inputtxt.yview)
        horizontaltext_scroll.config(command=inputtxt.xview)

        showdata=""
        for row in data:
            showdata=showdata+"%s\t %s \t %s\t\t %s\t\t %s\t\t\t %s\t %s\n"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    
        inputtxt.insert(END,showdata)
        inputtxt.config(state= DISABLED) 

        con.commit()
        con.close()
       
    mshowbutton=Button(pmaster,text="Show All",bg=x,command=mshowbtnclick,width=cwidth)
    mshowbutton.place(x=210,y=340)


    def exitbtnclick():
        pmaster.destroy()
    submitmasterform=Button(pmaster,text="Exit",bg=y,command=exitbtnclick)
    submitmasterform.place(x=190,y=290)

    idlabel=Label(pmaster,text="Enter id",width=cwidth)
    idlabel.place(x=290,y=250)
    

    pentry=Entry(pmaster)
    pentry.place(x=340,y=250)

    pname=Label(pmaster,text="Product Name")
    pname.place(x=20,y=70)
    pnameentry=Entry(pmaster)
    pnameentry.place(x=120,y=70)

    ppricelabel=Label(pmaster,text="Product Price")
    ppricelabel.place(x=20,y=120)
    ppriceentry=Entry(pmaster)
    ppriceentry.place(x=120,y=120)

    ptitlelabel=Label(pmaster,text="Product Title")   
    ptitlelabel.place(x=240,y=70)
    ptitleentry=Entry(pmaster)
    ptitleentry.place(x=340,y=70)

    pquantity=Label(pmaster,text="Product Quantity")
    pquantity.place(x=240,y=120)
    pquantityentry=Entry(pmaster)
    pquantityentry.place(x=340,y=120)

    def imagefunction():
        f=filedialog.askopenfilename(title='Select image') 
        return f

    def open_image():
            global img, filename
            con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
            cmd=con.cursor()


            con.commit()
            con.close()


            x = imagefunction()
            #opens the image
            img = Image.open(x)
            ran= random.randint(1,5000)
            #list=[ran]
            random.sample(range(ran),ran)
            
            img= img.save("productimage\\D-mart "+str(ran)+".png")
            print("run")   
            # resize the image and apply a high-quality down sampling filter
            
        
            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)
        
            # create a label
            panel = Label(root, image = img)
            
            # set the image as img 
            panel.image = img
            panel.grid(row = 2)

             
    
   

    pimage=Label(pmaster,text="ProductImage")
    pimage.place(x=80,y=190)
    pimageentry=Button(pmaster,text="Upload_image",bg=x,command=open_image )
    pimageentry.place(x=200,y=190)

   

    resultlabelmasterform=Label(pmaster,text="diplay")
    resultlabelmasterform.place(x=240,y=390)
    pmaster.mainloop()
    
 ########################### Customer form #############################
   menubar=Menu(root) 
   def customerform():
    
    cform=Toplevel(root)
    cform.geometry("1000x600")
    cform.title('Customer Form')
    cform.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')


    clabelname=Label(cform,text="Customer Form",font = ("Verdana ",15))
    clabelname.place(x=180,y=20) 

    cname=Label(cform,text="Name",width=cwidth)

    cname.place(x=20,y=70)
    cnameentry=Entry(cform)
    cnameentry.place(x=70,y=70) 

    caddress=Label(cform,text="Address",width=cwidth)
    caddress.place(x=20,y=120)
    caddressentry=Entry(cform)
    caddressentry.place(x=70,y=120)
    
    cphonelabel=Label(cform,text="PhoneNumber")   
    cphonelabel.place(x=20,y=170)
    cphoneentry=Entry(cform)
    cphoneentry.place(x=110,y=170)
    
    cage=Label(cform,text="Age",width=cwidth)
    cage.place(x=240,y=70)
    cageentry=Entry(cform)
    cageentry.place(x=280,y=70)
    
    cemail=Label(cform,text="Email",width=cwidth)
    cemail.place(x=240,y=120)
    cemailentry=Entry(cform)
    cemailentry.place(x=280,y=120)
    
    
    radio=IntVar()
    r1=Radiobutton(cform,text="Male",variable=radio,value=1)
    r1.place(x=300,y=200)

    r2=Radiobutton(cform,text="Female",variable=radio,value=2)
    r2.place(x=370,y=200)

    cradioLabel=Label(cform,text="Select your gender")
    cradioLabel.place(x=310,y=170)

    def customerformbtn():
        
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        cname=cnameentry.get()
        caddress=caddressentry.get()
        cphone=cphoneentry.get()
        cage=cageentry.get()
        cemail= cemailentry.get()

        cgender=" "
        if radio.get() == 1:
          cgender="Male"
        else:
          cgender="Female" 
        cmd.execute("insert into customer_info values(NULL,%s,%s,%s,%s,%s,%s)",(cname,caddress,cphone,cage,cemail,cgender))  
        resultlabelcustomerform.configure(text="insert success...")
        con.commit()  
        con.close()
    
    submitcustomerform=Button(cform,text="Insert",bg=x,command=customerformbtn,width=cwidth)
    submitcustomerform.place(x=30,y=250)

    
    def updatecustomerformbtn():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        cidentry=centry.get()
        cname=cnameentry.get()
        caddress=caddressentry.get()
        cphone=cphoneentry.get()
        cage=cageentry.get()
        cemail= cemailentry.get()

        cgender=" "
        if radio.get() == 1:
          cgender="Male"
        else:
          cgender="Female" 
        cmd.execute("update customer_info set name='"+str(cname)+"', address='"+str(caddress)+"', phone='"+str(cphone)+"', Age='"+str(cage)+"', email='"+str(cemail)+"',gender='"+str(cgender)+"' where id="+str(cidentry))
        resultlabelcustomerform.configure(text="data updated.....")
        con.commit()  
        con.close()

    updatecustomerform=Button(cform,text="Update",bg=x,width=cwidth,command=updatecustomerformbtn)
    updatecustomerform.place(x=120,y=250)

    idlabel=Label(cform,text="Enter id",width=cwidth)
    idlabel.place(x=290,y=250)

    centry=Entry(cform)
    centry.place(x=340,y=250)

    def editcustomerformbtn():
        dt=""
        datat=""
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        cidentry=centry.get()
        cmd.execute(" select * from customer_info where id="+str(cidentry))
        data=cmd.fetchall()
        
        dataname=""
        dataaddress=""
        dataphone=""
        dataage=""
        dataemail=""
        gender=""
       
        for row in data:
            dataname="%s" %(row[1])
            dataaddress="%s" %(row[2])
            dataphone="%s"%(row[3])
            dataage="%s"%(row[4])
            dataemail="%s"%(row[5])
            gender="%s"%(row[6])
            if gender=="Male":
                r1.select()
            else:
                r2.select() 
       
    
        con.commit()  
        cnameentry.insert(0,dataname)
        caddressentry.insert(0,dataaddress)
        cphoneentry.insert(0,dataphone)
        cageentry.insert(0,dataage)
        cemailentry.insert(0,dataemail)

        '''data=cmd.fetchall()           
        for row in data:
         datat=datat+"%s %s  %s %s"%(row[0],row[1],row[2],row[3])
         print("%s \t %s\t %s\t %s"%(row[0],row[1],row[2],row[3]))
        #print(tabulate(dt,tablefmt="grid"))
        displayresult=datat

        resultlabelcustomerform.configure(text=displayresult) 
        con.close()'''

    

    editcustomerform=Button(cform,text="Edit",bg=x,command=editcustomerformbtn,width=cwidth)
    editcustomerform.place(x=210,y=250)

    def deletebtnclick():
     con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
     cmd=con.cursor() 
     cidentry=centry.get()
     cmd.execute("Delete from customer_info where id="+str(cidentry))

     resultlabelcustomerform.configure(text="Data Delete Succesfully .....")
     con.commit()
     con.close()
    

    deletecustomerform=Button(cform,text="Delete",bg=y,width=cwidth,command=deletebtnclick)
    deletecustomerform.place(x=30,y=290)

    def pshowbtnclick():
     
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        cmd.execute("select * from customer_info")
        data=cmd.fetchall()
        total=cmd.rowcount
        resultlabelcustomerform.configure(text="Total data entries : "+str(total))

        #vertical scroll
        text_scroll=Scrollbar(cform)
        text_scroll.pack(side=RIGHT,fill=Y)

        #horizontal Scroll
        horizontaltext_scroll=Scrollbar(cform,orient='horizontal')
        horizontaltext_scroll.pack(side=BOTTOM,fill=X)
        

        inputtxt = Text(cform, height=7,width=120,bg = "light yellow",yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=horizontaltext_scroll.set)
        inputtxt.place(x=6,y=440)
        
        
        #inputtext.insert(tk.END,Text)
        text_scroll.config(command=inputtxt.yview)
        horizontaltext_scroll.config(command=inputtxt.xview)

        showdata=""
        for row in data:
            showdata=showdata+"%s\t %s \t %s\t\t\t\t%s\t\t\t %s\t\t%s\t\t\t %s\n"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    
        inputtxt.insert(END,showdata)
        inputtxt.config(state= DISABLED) 

        con.commit()
        con.close()


       

    editcustomerform=Button(cform,text="Show All",bg=x,command=pshowbtnclick,width=cwidth)
    editcustomerform.place(x=210,y=340)

    def clearbtnclick():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor() 
        cnameentry.delete(0, END)
        caddressentry.delete(0,END)
        cphoneentry.delete(0,END)
        cageentry.delete(0,END)
        cemailentry.delete(0,END)
        r1.deselect()
        r2.deselect()    

        resultlabelcustomerform.configure(text="Data Clear Succesfully .....")
        con.commit()
        con.close()
    clearcustomerform=Button(cform,text="Clear",bg=y,width=cwidth,command=clearbtnclick)
    clearcustomerform.place(x=120,y=290)

    def exitbtnclick():
        cform.destroy()

    Exitcustomerform=Button(cform,text="Exit",bg=y,width=cwidth,command=exitbtnclick)
    Exitcustomerform.place(x=210,y=290)

    resultlabelcustomerform=Label(cform,text="diplay")
    resultlabelcustomerform.place(x=230,y=380)
    cform.mainloop()

####################### BIlling  Form ################     

   def Billingform():
    root.iconify()
    bform = Toplevel(top) 
    bform.geometry("850x590")
    bform.title("Billing Form")
    bform.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')
    
    con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
    cmd=con.cursor()
    dt=[]
    cmd.execute("select id,name from customer_info")
    data=cmd.fetchall()
    for i in data:
        dt.append(str(i[0])+"-"+i[1])
    def lookupbilling(event):
        global cid 
        option=mycombo.get()
        cid=option.split("-")[0]
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
    
        query=cmd.execute("select * from  customer_info where id='"+str(cid)+"'")
        #cmd.execute(query,cid)
        rows=cmd.fetchall()  
        for i in rows:
            addressentryvar.set(i[2])
            qauntityentryvar.set(i[3])
        
    n=StringVar()
    Label(bform,textvariable=n,width=30)
    mycombo=ttk.Combobox(bform,textvariable=n)
    mycombo.set("Pick an Option")
    mycombo['values']=dt
    mycombo.place(x=20,y=90)
    #mycombo.current(0)
    mycombo.bind("<<ComboboxSelected>>",lookupbilling)

    btitlename=Label(bform,text="Billing ",font = ("Verdana ",15))
    btitlename.place(x=200,y=20)

    addressentryvar=StringVar()
    qauntityentryvar=StringVar()


    addbtn = Button(bform, text = "Add product" )  
    addbtn.place(x=50,y=230)


    customerid=Label(bform,text="Customer id")
    customerid.place(x=30,y=50)
    
    rate =Label(bform,text="Address")
    rate.place(x=180,y=70)
    addressentryentry=Entry(bform,textvariable=addressentryvar)
    addressentryentry.place(x=180,y=100)
    qauntity =Label(bform,text="Number")
    qauntity.place(x=320,y=70)
    qauntityentry=Entry(bform,textvariable=qauntityentryvar)
    qauntityentry.place(x=340,y=100)
            
    lbl = Label(bform,text = "Product")  
    lbl.place(x=20,y=120)  
    bentry=Entry(bform,width=17)
    bentry.place(x=20,y=160)

    ratelabel=Label(bform,text="Rate")
    ratelabel.place(x=140,y=120)
    rateentry1=Entry(bform,width=15)
    rateentry1.place(x=130,y=160)        

    qauntitylabel=Label(bform,text="Quantity")
    qauntitylabel.place(x=220,y=120)

    e3= StringVar()
    qauntityentry1=Entry(bform,width=30,textvariable=e3)
    qauntityentry1.place(x=230,y=160)
    qauntityentry1.insert(0,0)  

    amountlabel=Label(bform,text="Amount")
    amountlabel.place(x=320,y=120)
   
    amountentry=Entry(bform,width=17)
    amountentry.place(x=330,y=160)
    amountentry.delete(0,END)
    amountentry.insert(0,0)


    listbox=Listbox(bform) 
    listbox.place(x=20,y=200)

    def totalbutton(amount):
        if qauntityentry1!="":
            con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
            cmd=con.cursor() 
            prate=rateentry1.get()
            pqauntity=qauntityentry1.get()
            amount=int(prate)*int(pqauntity) 
            amountentry.delete(0,END)
            amountentry.insert(0,str(amount)) 
        else:
            qauntityentry1.delete(0,END)
        
            qauntityentry1.insert(0,0)         
    
       
    e3.trace("w", lambda  name, index, mode, e3=e3: totalbutton(amountentry))

   
    def showdata():
       
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        cmd.execute("select * from  addtocart")
        bdata=cmd.fetchall()
        total=cmd.rowcount 
        showdata=""
        for row in bdata:
            showdata=showdata+"%s\t %s \t %s\t %s\t %s\t %s\t %s\n"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    
        inputtxt.insert(END,showdata)
        inputtxt.config(state= DISABLED) 
        con.commit()
        con.close()

    invoicenumber=Label(bform,text="INVOICE NO:",font=font.BOLD,fg="blue")
    invoicenumber.place(x=490,y=250)   

    nullinvoice=Label(bform,text="",font=font.BOLD,fg="blue")
    nullinvoice.place(x=590,y=250)
     
    
    addtocartid=Label(bform,text="ID")
    addtocartid.place(x=320,y=280)

    cartProductid=Label(bform,text="Product_Id")
    cartProductid.place(x=360,y=280)

    userid=Label(bform,text="User_id")
    userid.place(x=430,y=280)

    invoice=Label(bform,text="Invoice")
    invoice.place(x=490,y=280)

    totalqut=Label(bform,text="TotalQuantity")
    totalqut.place(x=550,y=280)

    totalamt=Label(bform,text="TotalAmount")
    totalamt.place(x=640,y=280)

    curdate=Label(bform,text="Date")
    curdate.place(x=730,y=280)


    showbtn=Button(bform,text="Show Data", command=showdata,bg=y)
    showbtn.place(x=170,y=200)

    def savebtnclick():
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        totalamt=amountentry.get()
        cmd.execute("insert into cart_master values(NULL,%s,%s,%s,curdate())",(cid,randnum,totalamt))
        #cmd.fetchall()
        con.commit()
        con.close()

        
        print("sucess")
    ############################### Bill print form ##################################    
        msgbox= messagebox.askquestion("FinalBill", "Sure you want Forward print process?")
        if msgbox == 'no':
            msgbox.destroy()
       
        printbill = Toplevel(bform) 
        bform.iconify()
        printbill.geometry("850x590")
        printbill.title("FinalBill")
        printbill.iconbitmap('C:\\Users\\Acer\\Desktop\\python\\pratise pratical\\icon-icons.ico')
            
        billdiscount=Label(printbill,text="Get Dicount Amount : ")
        billdiscount.place(x=120,y=320)

        dicounttotal=Label(printbill,text="")
        dicounttotal.place(x=260,y=320)

        billnetamount=Label(printbill,text="Net Amount: ")
        billnetamount.place(x=120,y=340)

        nettotal=Label(printbill,text="")
        nettotal.place(x=200,y=340)


        thankyoulabel=Label(printbill,text="----------------------------\nThank You\n-----------------------------")
        thankyoulabel.place(x=300,y=370)

        def billbttn():
            con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
            cmd=con.cursor() 
            #Inner join Query
            sql=cmd.execute("SELECT pm.ptitle, pm.pprice,pm.cur_date FROM product_master pm JOIN addtocart c ON pm.id = c.productid where c.invoice='"+str(randnum)+"'")
            cmd.execute(sql)
              
            file=open("C:\\Users\\Acer\\Desktop\\python\\shoppingsystempython\\storesshopbill.txt","w")
               
            productnamevar=""
            myresult = cmd.fetchall()
                #print(myresult)
            for row in myresult:
                 
                productnamevar=productnamevar+"%s\t %s\n %s\n"%(row[0],row[1],row[2]) 

            s="ProductName\t\t" "Price\t\t\n" " "
            file.write(s)
            file.write(productnamevar)
            file.close()
            print("file successfully created...")
               

        billbtn=Button(printbill,text="Print form",command=billbttn)
        billbtn.place(x=330,y=460)

        billtitlelabel=Label(printbill,text="#################################\nDmart\n#################################")
        billtitlelabel.place(x=150,y=30)

        billaddress=Label(printbill,text="D-Mart, Ambavadi Police Line, himmatnagar\n Himatnagar, Gujarat 383001\n........................................................")
        billaddress.place(x=150,y=70)

        displaybill=Label(printbill,text="")
        displaybill.place(x=150,y=130)

        
        
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        sql=cmd.execute("SELECT pm.ptitle, pm.pprice FROM product_master pm JOIN addtocart c ON pm.id = c.productid where c.invoice='"+str(randnum)+"'")
        cmd.execute(sql)
    
        myresult = cmd.fetchall()
        print(myresult)
        showdata=""
        for row in myresult:
          showdata=showdata+"%s\t %s \n"%(row[0],row[1])
        displaybill.config(text=showdata)

        cmd.execute("SELECT sum(totalamt) FROM addtocart where invoice='"+str(randnum)+"'")
        totalamount=cmd.fetchall()
        
        #print(totalamount)
        for row in totalamount:
            billdata="%s"%(row[0])
        #print(billdata)

        if (float(billdata)>=1500):
            dicount=float(billdata)*15/100
        elif (float(billdata)>=1000):
            dicount=float(billdata)*10/100
        elif (float(billdata)>=500):
            dicount=float(billdata)*5/100
        elif (float(billdata)<500):
            dicount=float(billdata)*0/100  
         
        dicounttotal.configure(text=dicount)

        netprice=float(billdata)-dicount 
        nettotal.configure(text=str(netprice))
        
        con.commit()
        con.close()

    savebtn=Button(bform,text="Save",width=cwidth,command=savebtnclick,bg="#f8ba5c")
    savebtn.place(x=250,y=200)
#################################################################################################
    def exitbtnclick():
        bform.destroy()

    exitbtn=Button(bform,text="Exit",width=cwidth,command=exitbtnclick,bg="lightpink")
    exitbtn.place(x=370,y=200)

    billtotaltext=Label(bform,text="Your Total Amount : ")
    billtotaltext.place(x=460,y=400)

    amounttotal=Label(bform,text="")
    amounttotal.place(x=600,y=400)

    billdiscount=Label(bform,text="Get Dicount Amount : ")
    billdiscount.place(x=460,y=420)

    dicounttotal=Label(bform,text="")
    dicounttotal.place(x=600,y=420)

    billnetamount=Label(bform,text="Net Amount: ")
    billnetamount.place(x=460,y=440)

    nettotal=Label(bform,text="")
    nettotal.place(x=600,y=440)

   
    def addtocart():
        dt=[]
        invoice=""
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        quantity=qauntityentry1.get()
        totalamt=amountentry.get()
        a=lid["text"]

        result=cmd.execute("insert into addtocart values(NULL,%s,%s,%s,%s,%s,curdate())",(a,cid,randnum,quantity,totalamt))
        data=cmd.fetchall()
        con.commit()
        con.close()


        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
        

        cmd.execute("select * from  addtocart where invoice='"+str(randnum)+"'")
        #cmd.execute("select * from  addtocart")
        
        bdata=cmd.fetchall()
        
        total=cmd.rowcount 
        showdata=""
        bill=""
        for row in bdata:
            showdata="%s\t %s \t %s\t %s\t %s\t %s\t %s\n"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        print(showdata)    
        nullinvoice.configure(text=randnum)
        inputtxt.delete(tk.END,END)
        inputtxt.insert(END,showdata)
        
        
        cmd.execute("SELECT sum(totalamt) FROM addtocart where invoice='"+str(randnum)+"'")
        totalamount=cmd.fetchall()
        
        #print(totalamount)
        for row in totalamount:
            billdata="%s"%(row[0])
        #print(billdata)

        if (float(billdata)>=1500):
            dicount=float(billdata)*15/100
        elif (float(billdata)>=1000):
            dicount=float(billdata)*10/100
        elif (float(billdata)>=500):
            dicount=float(billdata)*5/100
        elif (float(billdata)<500):
            dicount=float(billdata)*0/100  
        amounttotal.configure(text=str(billdata))        
        dicounttotal.configure(text=dicount)

        netprice=float(billdata)-dicount 
        nettotal.configure(text=str(netprice)) 

        
        con.commit()
        con.close()
        
        #inputtxt.config(state= DISABLED)    
        
    
    
         
    finalbtn=Button(bform,text="Add",width=cwidth, command=addtocart,bg="#879afd")
    finalbtn.place(x=310,y=200)

    #vertical scroll
    text_scroll=Scrollbar(bform)
    text_scroll.pack(side=RIGHT,fill=Y)

    #horizontal Scroll
    horizontaltext_scroll=Scrollbar(bform,orient='horizontal')
    horizontaltext_scroll.pack(side=BOTTOM,fill=X)
    

    inputtxt = Text(bform, height=6,width = 60,bg = "light yellow",yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=horizontaltext_scroll.set)
    inputtxt.place(x=310,y=300)
    
    
    #inputtext.insert(tk.END,Text)
    text_scroll.config(command=inputtxt.yview)
    horizontaltext_scroll.config(command=inputtxt.xview)

    ran=random.randint(1000,9999)
    invoice=int(ran)
    randnum=str(invoice)
    
    
    lid=Label(bform,text="lid",foreground="#eff1f2")
    lid.place(x=310,y=230) 
    
   
    def update(data):
        listbox.delete(0,END)
        for item in data:
            listbox.insert(END,item)

    def fillout(e):
        bentry.delete(0,END)
        bentry.insert(0,listbox.get(ACTIVE))
        option=listbox.get(ACTIVE)
        
        con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
        cmd=con.cursor()
    
        query=cmd.execute("select * from product_master where ptitle='"+str(option)+"'")
        rows=cmd.fetchall()  
        
        for i in rows:
            rateentry1.delete(0,END)
            rateentry1.insert(0,i[3])
            lid.config(text=str(i[0]))

    def check(e):
        typed=bentry.get()
        if typed =='':
          data=dt
        else:
            data=[]
            for item in dt:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)          

   
    con=mysql.connector.connect(host="localhost",user="root",password="",database="storesoftware")
    cmd=con.cursor()
    
    dt=[]
    
    cmd.execute("select * from product_master")
    data=cmd.fetchall()
    for row in data:
        x="%s "%(row[4])

        dt.append(x)
    countries=dt 
    
    
    update(dt) 
    listbox.bind("<<ListboxSelect>>",fillout)   

    bentry.bind("<KeyRelease>",check)


   menubar.add_command(label="Product Master",command=productmaster)
   menubar.add_command(label="Customer Master",command=customerform)
   menubar.add_command(label="Billing",command=Billingform)
   menubar.add_command(label="Exit",command=root.quit) 
   root.config(menu=menubar) 
   root.resizable(False,False)
   root.mainloop()


mainloop()