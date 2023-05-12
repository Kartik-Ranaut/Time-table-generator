from tkinter import *

            
def one():
    global main
  
    main=Tk()
    main.title("Time Table Generator")
    main.geometry('900x600')
    main.minsize(900,600)
    main.maxsize(900,600)
    global name
    global password
    name=StringVar()
    password=StringVar()

    def time():
        global TT
        TT=Tk()
        TT.title("Time Table Generator")
        global thsub
        global ansub
        global labsub
        thsub=IntVar()
        ansub=IntVar()
        labsub=IntVar()
        TT.geometry('950x700')
        TT.minsize(950,700)
        TT.maxsize(950,700)
        Label(TT,text='Enter the Conditions',font=("Arial",15),fg="green").pack(pady=20)
        ttframe=Frame(TT)
        ttframe.pack()
        Label(ttframe,text="No. of theory Subjects").grid(row=0,column=0,pady=3)
        e111=Entry(ttframe,textvariable=thsub)
        e111.grid(row=0,column=1)
        Label(ttframe,text="No. of analytical Subjects").grid(row=1,column=0,pady=3)
        e222=Entry(ttframe,textvariable=ansub)
        e222.grid(row=1,column=1)
        Label(ttframe,text="No. of labs").grid(row=2,column=0,pady=3)
        e333=Entry(ttframe,textvariable=labsub)
        e333.grid(row=2,column=1)
        # Label(ttframe,text="No. of periods to each subject").grid(row=3,column=0,pady=3)
        # Entry(ttframe).grid(row=3,column=1)
        e111.insert(END,"4")
        e222.insert(END,"2")
        e333.insert(END,"2")
        def generateTable():
            Label(TT,text="Wait, it will take some time",fg="green").pack()
            table=Frame(TT)
            table.pack()
            # thsub=thsub.get()
            # ansub=ansub.get()
            # labsub=labsub.get()
#..................... ist row.................
            e00=Entry(table,width=5)
            e00.insert(END,"Days")
            e00.grid(row=0,column=0)
            
            e01=Entry(table,width=7)
            e01.insert(END,"1st Period")
            e01.grid(row=0,column=1)
            
            e02=Entry(table,width=7)
            e02.insert(END,"2nd Period")
            e02.grid(row=0,column=2)

            e03=Entry(table,width=7)
            e03.insert(END,"15m break")
            e03.grid(row=0,column=3)

            e04=Entry(table,width=7)
            e04.insert(END,"3rd Period")
            e04.grid(row=0,column=4)

            e05=Entry(table,width=7)
            e05.insert(END,"4th Period")
            e05.grid(row=0,column=5)

            e06=Entry(table,width=7)
            e06.insert(END,"55m Lunch")
            e06.grid(row=0,column=6)

            e07=Entry(table,width=7)
            e07.insert(END,"5th Period")
            e07.grid(row=0,column=7)

            e08=Entry(table,width=7)
            e08.insert(END,"6th Period")
            e08.grid(row=0,column=8)

            e09=Entry(table,width=7)
            e09.insert(END,"15m break")
            e09.grid(row=0,column=9)

            e0a=Entry(table,width=7)
            e0a.insert(END,"7th period")
            e0a.grid(row=0,column=10)
#..........2nd row.............
            e10=Entry(table,width=5)
            e10.insert(END,"Mon")
            e10.grid(row=1,column=0)

            e20=Entry(table,width=5)
            e20.insert(END,"Tue")
            e20.grid(row=2,column=0)

            e30=Entry(table,width=5)
            e30.insert(END,"Wed")
            e30.grid(row=3,column=0)

            e40=Entry(table,width=5)
            e40.insert(END,"Thur")
            e40.grid(row=4,column=0)

            e50=Entry(table,width=5)
            e50.insert(END,"Fri")
            e50.grid(row=5,column=0)

            e60=Entry(table,width=5)
            e60.insert(END,"Sat")
            e60.grid(row=6,column=0)
#..........break and lunch.........
            e13=Entry(table,width=5)
            e13.insert(END,"X")
            e13.grid(row=1,column=3)

            e23=Entry(table,width=5)
            e23.insert(END,"X")
            e23.grid(row=2,column=3)

            e33=Entry(table,width=5)
            e33.insert(END,"X")
            e33.grid(row=3,column=3)

            e43=Entry(table,width=5)
            e43.insert(END,"X")
            e43.grid(row=4,column=3)

            e53=Entry(table,width=5)
            e53.insert(END,"X")
            e53.grid(row=5,column=3)

            e63=Entry(table,width=5)
            e63.insert(END,"X")
            e63.grid(row=6,column=3)


            e19=Entry(table,width=5)
            e19.insert(END,"X")
            e19.grid(row=1,column=9)

            e29=Entry(table,width=5)
            e29.insert(END,"X")
            e29.grid(row=2,column=9)

            e39=Entry(table,width=5)
            e39.insert(END,"X")
            e39.grid(row=3,column=9)

            e49=Entry(table,width=5)
            e49.insert(END,"X")
            e49.grid(row=4,column=9)

            e59=Entry(table,width=5)
            e59.insert(END,"X")
            e59.grid(row=5,column=9)

            e69=Entry(table,width=5)
            e69.insert(END,"X")
            e69.grid(row=6,column=9)

#.............lunch
            e16=Entry(table,width=5)
            e16.insert(END,"X")
            e16.grid(row=1,column=6)

            e26=Entry(table,width=5)
            e26.insert(END,"X")
            e26.grid(row=2,column=6)

            e36=Entry(table,width=5)
            e36.insert(END,"X")
            e36.grid(row=3,column=6)

            e46=Entry(table,width=5)
            e46.insert(END,"X")
            e46.grid(row=4,column=6)

            e56=Entry(table,width=5)
            e56.insert(END,"X")
            e56.grid(row=5,column=6)

            e66=Entry(table,width=5)
            e66.insert(END,"X")
            e66.grid(row=6,column=6)

#......monday
            e11=Entry(table,width=5)
            e11.insert(END,"T2")
            e11.grid(row=1,column=1)

            e12=Entry(table,width=5)
            e12.insert(END,"T4")
            e12.grid(row=1,column=2)

            e14=Entry(table,width=5)
            e14.insert(END,"T3")
            e14.grid(row=1,column=4)

            e15=Entry(table,width=5)
            e15.insert(END,"CCR")
            e15.grid(row=1,column=5)

            e17=Entry(table,width=5)
            e17.insert(END,"LT1")
            e17.grid(row=1,column=7)

            e18=Entry(table,width=5)
            e18.insert(END,"LT1")
            e18.grid(row=1,column=8)

            e1a=Entry(table,width=5)
            e1a.insert(END,"LT1")
            e1a.grid(row=1,column=10)
#......Tuesday
            e21=Entry(table,width=5)
            e21.insert(END,"T1")
            e21.grid(row=2,column=1)

            e22=Entry(table,width=5)
            e22.insert(END,"T4")
            e22.grid(row=2,column=2)

            e24=Entry(table,width=5)
            e24.insert(END,"T2")
            e24.grid(row=2,column=4)

            e25=Entry(table,width=5)
            e25.insert(END,"T1")
            e25.grid(row=2,column=5)

            e27=Entry(table,width=5)
            e27.insert(END,"LT2")
            e27.grid(row=2,column=7)

            e28=Entry(table,width=5)
            e28.insert(END,"LT2")
            e28.grid(row=2,column=8)

            e2a=Entry(table,width=5)
            e2a.insert(END,"LT2")
            e2a.grid(row=2,column=10)
#......Wednes
            e31=Entry(table,width=5)
            e31.insert(END,"T3")
            e31.grid(row=3,column=1)

            e32=Entry(table,width=5)
            e32.insert(END,"T2")
            e32.grid(row=3,column=2)

            e34=Entry(table,width=5)
            e34.insert(END,"T1")
            e34.grid(row=3,column=4)

            e35=Entry(table,width=5)
            e35.insert(END,"T4")
            e35.grid(row=3,column=5)

            e37=Entry(table,width=5)
            e37.insert(END,"Club")
            e37.grid(row=3,column=7)

            e38=Entry(table,width=5)
            e38.insert(END,"Club")
            e38.grid(row=3,column=8)

            e3a=Entry(table,width=5)
            e3a.insert(END,"LIB")
            e3a.grid(row=3,column=10)
#......Thursday
            e41=Entry(table,width=5)
            e41.insert(END,"A1")
            e41.grid(row=4,column=1)

            e42=Entry(table,width=5)
            e42.insert(END,"A1")
            e42.grid(row=4,column=2)

            e44=Entry(table,width=5)
            e44.insert(END,"T2")
            e44.grid(row=4,column=4)

            e45=Entry(table,width=5)
            e45.insert(END,"A2")
            e45.grid(row=4,column=5)

            e47=Entry(table,width=5)
            e47.insert(END,"A2")
            e47.grid(row=4,column=7)

            e48=Entry(table,width=5)
            e48.insert(END,"T2")
            e48.grid(row=4,column=8)

            e4a=Entry(table,width=5)
            e4a.insert(END,"T3")
            e4a.grid(row=4,column=10) 

#......Friday
            e51=Entry(table,width=5)
            e51.insert(END,"A2")
            e51.grid(row=5,column=1)

            e52=Entry(table,width=5)
            e52.insert(END,"A2")
            e52.grid(row=5,column=2)

            e54=Entry(table,width=5)
            e54.insert(END,"T3")
            e54.grid(row=5,column=4)

            e55=Entry(table,width=5)
            e55.insert(END,"A1")
            e55.grid(row=5,column=5)

            e57=Entry(table,width=5)
            e57.insert(END,"A1")
            e57.grid(row=5,column=7)

            e58=Entry(table,width=5)
            e58.insert(END,"T3")
            e58.grid(row=5,column=8)

            e5a=Entry(table,width=5)
            e5a.insert(END,"T1")
            e5a.grid(row=5,column=10)   

#......Saturda6
            e61=Entry(table,width=5)
            e61.insert(END,"T4")
            e61.grid(row=6,column=1)

            e62=Entry(table,width=5)
            e62.insert(END,"T1")
            e62.grid(row=6,column=2)

            e64=Entry(table,width=5)
            e64.insert(END,"T4")
            e64.grid(row=6,column=4)

            e65=Entry(table,width=5)
            e65.insert(END,"T2")
            e65.grid(row=6,column=5)

            e67=Entry(table,width=5)
            e67.insert(END,"T3")
            e67.grid(row=6,column=7)

            e68=Entry(table,width=5)
            e68.insert(END,"T2")
            e68.grid(row=6,column=8)

            e6a=Entry(table,width=5)
            e6a.insert(END,"T1")
            e6a.grid(row=6,column=10)


            Label(TT,text="Tn:Theory subject n",fg="blue").pack(pady=3)
            Label(TT,text="An:Analytic subject n",fg="blue").pack(pady=3)
            Label(TT,text="LTn:Lab of subject n",fg="blue").pack(pady=3)
#.................lab periods............
            

        Button(TT,text="Generate Time Table",command=generateTable).pack()



        TT.mainloop()

    def data():
      
        name_d=name.get()
        password_d=password.get()
        
        if name_d=="Kartik" and password_d=="2008":
            Label(main,text='you enter correct data',font=("Arial",15),fg="green").pack()
            time()
        else: 
            Label(main,text='you enter wrong data',font=("Arial",15),fg="red").pack()
    Label(main,text='Welcome to Time Table Generator',font=("Arial",15),height="7").pack(side='top')
    Label(main,text='Log In',font=("Arial", 25)).pack()
    login=Frame(main)
    login.pack()
    Label(login,text='User Id ',font=("Arial",15)).grid(row=0,column=0,pady=25)
    Entry(login,textvariable=name).grid(row=0,column=1)
    Label(login,text='Password',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Entry(login,textvariable=password,show='*').grid(row=1,column=1)
    
        

    Button(main,text="Enter",font=("Arial",25),command=data).pack(pady=50)
    main.mainloop()


one()
