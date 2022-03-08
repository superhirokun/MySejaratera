# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL7V
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211102270 | YAP CHOO KATH MOON | 1211102270@student.mmu.edu.my | 017-3648638
# Member_2: 1211101961 | CHAI DI SHENG      | 1211101961@student.mmu.edu.my | 016-3432580
# Member_3: 1211101726 | TAI JIN PEI        | 1211101726@student.mmu.edu.my | 011-11553789
# Member_4: 1211101506 | LEONG JIA YI       | 1211101506@student.mmu.edu.my | 017-9882201
# *********************************************************
# Task Distribution
# Member_1: Account sign up and login authentication
# Member_2: Menu and result display
# Member_3: Public user update information, auto-categorize priority ranking and status list
# Member_4: Administrator assign appointment, create vaccination center and generate list
# ******************************************t***************
from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# delete registration entry if same username or success register


def entry_delete():
    username_entry.delete(0, END)
    userpassword_entry.delete(0, END)
    age_entry.delete(0, END)
    id_entry.delete(0, END)
    phone_entry.delete(0, END)
    postcode_entry.delete(0, END)
    address_entry.delete(0, END)
    job_entry.delete(0, END)
    state_entry.delete(0, END)
    township_entry.delete(0, END)

# data import from register form


def register_data():
    username_info = username.get()
    userpassword_info = password.get()
    age_info = age.get()
    ID_info = ID.get()
    phone_info = phone.get()
    postcode_info = postcode.get()
    address_info = address.get()
    job_info = job.get()
    state_info = state.get()
    township_info = township.get()


# Make sure the form is filled
    if len(username.get()) < 5 or password.get() == "" or (int(age.get())) < 0 or (int(age.get())) > 122 or ID.get() == "" or phone.get() == "" or postcode.get() == "" or address.get() == "" or job.get() == "" or state.get() == "" or township.get() == "":
        messagebox.showerror('Error', 'Please Enter Your Information')
    else:

        # Make username does not repeate
        try:
            if FileExistsError:
                with open(os.path.join(username_info), 'r') as f2:
                    v = f2.read()
                    if username_info in v:
                        messagebox.showerror('Error', 'Username already exit')
                        entry_delete()
                        f2.close()
                    else:
                        pass
        except FileNotFoundError:

            with open(os.path.join(username_info), 'w') as f:
                f.write(username_info + "\n")
                f.write(userpassword_info + "\n")
                f.write(age_info + "\n")
                f.write(ID_info + "\n")
                f.write(phone_info + "\n")
                f.write(postcode_info + "\n")
                f.write(address_info + "\n")
                f.write(job_info + "\n")
                f.write(state_info + "\n")
                f.write(township_info)
                f.close()
                entry_delete()
                Label(screenR, text="Registration Sucess",
                      fg="green", font=("calibri", 12)).pack()
                Button(screenR, text="Login", height=1, width=20,
                       font=("bold", 12), command=public).pack()


# Register page setting
def register():
    global screenR
    screenR = Toplevel()
    screenR.title("Registration Form")
    screenR.geometry("600x650")

# Global
    global username
    global username_entry
    global password
    global userpassword_entry
    global age
    global age_entry
    global ID
    global id_entry
    global phone
    global phone_entry
    global postcode
    global postcode_entry
    global address
    global address_entry
    global job
    global job_entry
    global state
    global state_entry
    global township
    global township_entry

# StringVar
    username = StringVar()
    password = StringVar()
    age = StringVar()
    ID = StringVar()
    phone = StringVar()
    postcode = StringVar()
    address = StringVar()
    job = StringVar()
    state = StringVar()
    township = StringVar()

# Registration process
    Label(screenR, text="Resgistration Form", bg="light blue",
          width=400, height=2, font=("bold", 16)).pack()
    Label(screenR, text="Full Name as IC : ", font=("bold", 12)).pack()
    username_entry = Entry(screenR, textvariable=username, width=50,)
    username_entry.pack()
    Label(screenR, text="Password :", font=("bold", 12)).pack()
    userpassword_entry = Entry(screenR, textvariable=password, width=50)
    userpassword_entry.pack()
    Label(screenR, text="Age :", font=("bold", 12)).pack()
    age_entry = Entry(screenR, textvariable=age, width=50)
    age_entry.pack()
    Label(screenR, text="ID :", font=("bold", 12)).pack()
    id_entry = Entry(screenR, textvariable=ID, width=50)
    id_entry.pack()
    Label(screenR, text="Phone Number :", font=("bold", 12)).pack()
    phone_entry = Entry(screenR, textvariable=phone, width=50)
    phone_entry.pack()
    Label(screenR, text="Postcode :", font=("bold", 12)).pack()
    postcode_entry = Entry(screenR, textvariable=postcode, width=50)
    postcode_entry.pack()
    Label(screenR, text="Address :", font=("bold", 12)).pack()
    address_entry = Entry(screenR, textvariable=address, width=50)
    address_entry.pack()
    Label(screenR, text="Occupations :", font=("bold", 12)).pack()
    job_entry = Entry(screenR, textvariable=job, width=50)
    job_entry.pack()
    Label(screenR, text="State :", font=("bold", 12)).pack()
    state_entry = Entry(screenR, textvariable=state, width=50)
    state_entry.pack()
    Label(screenR, text="Township :", font=("bold", 12)).pack()
    township_entry = Entry(screenR, textvariable=township, width=50)
    township_entry.pack()
    Label(screenR, text="").pack()
    Button(screenR, text="Registered", height=1, width=20,
           font=("bold", 12), command=register_data).pack()
    Button(screenR, text="Back", height=1, width=20, font=(
        "bold", 12), command=screenR.destroy).pack()

# tjp_part


def update():
    # update old data
    now = open("info.txt", "a")
    now = open("info.txt", "r+")
    with now as f:
        read_f = f.readlines()
        f.seek(0)
        for line in read_f:
            if username1 in line:
                f.truncate()
            else:
                f.write(line)

    now.close
    save()

# save command


def save():
    # read data from user's data
    with open(os.path.join(username1), 'r') as tjpfile:
        fileread = tjpfile.read().splitlines()
        age = fileread[2]
        phone = fileread[4]
        postcodetjp = fileread[5]

    prioritycount = 0  # priority counter

    if(int(age) >= 90):
        prioritycount = prioritycount+190
    elif(int(age) < 90 and int(age) >= 80):
        prioritycount = prioritycount+180
    elif(int(age) < 80 and int(age) >= 70):
        prioritycount = prioritycount+170
    elif(int(age) < 70 and int(age) >= 60):
        prioritycount = prioritycount+160
    elif(int(age) < 60 and int(age) >= 50):
        prioritycount = prioritycount+20
    elif(int(age) < 50 and int(age) >= 18):
        prioritycount = prioritycount+10
    else:
        prioritycount = prioritycount+0

    if(sick_var.get() == 1):
        sick_info = 'Yes'
        prioritycount = prioritycount+50
    else:
        sick_info = 'No'
        prioritycount = prioritycount+0

    if(symptom_var.get() == 10):
        symptom_info = 'Yes'
        prioritycount = prioritycount-4
    else:
        symptom_info = 'No'
        prioritycount = prioritycount+0

    if(occupation_var.get() == 3):
        occupation_info = 'Health-Care worker'
        prioritycount = prioritycount+6
    if(occupation_var.get() == 4):
        occupation_info = 'Community Services'
        prioritycount = prioritycount+5
    if(occupation_var.get() == 5):
        occupation_info = 'Energy'
        prioritycount = prioritycount+4
    if(occupation_var.get() == 6):
        occupation_info = 'Food and Transportation'
        prioritycount = prioritycount+3
    if(occupation_var.get() == 7):
        occupation_info = 'Worker'
        prioritycount = prioritycount+2
    if(occupation_var.get() == 8):
        occupation_info = 'Student'
        prioritycount = prioritycount+1
    if(occupation_var.get() == 9):
        occupation_info = 'Non-working'
        prioritycount = prioritycount+1

    try:
        rsvp_var.get()
    except NameError:
        rsvp_info = "''"


# —————————————————————————————————————save data in .txt————————————————————————————————
    s = '\n' + str(prioritycount) + ','+rsvp_info + ', ' + username1 + ', ' + \
        age + ', ' + phone + ',' + postcodetjp + ', ' + sick_info + ', ' + \
        symptom_info + ', ' + occupation_info
    f = open('info.txt', 'a')
    f.write(s)
    f.close

    prioritycount = 0  # clear to 0
    root.destroy()
    login_sucess()

# meaasagebox(pop out)


def msg():
    if(sick_var.get() == 0):
        messagebox.showwarning('missing details', 'missing Q1')

    elif(symptom_var.get() == 0):
        messagebox.showwarning('missing details', 'missing Q2')

    elif(occupation_var.get() == 0):
        messagebox.showwarning('missing details', 'missing Q3')

    else:  # upadate user info
        messagebox.showinfo('Thank You', 'Success registered')
        update()


# ————————————————————————pg1————————————————————————
def r1():
    global root
    root = Toplevel()
    root.geometry('500x900')
    root.title('Update status')
    Label(root, text="Update Status", bg="light blue",
          width=400, height=1, font=("Comic Sans MS", 18)).pack()

    global sick_var
    global y
    global n
    global symptom_var
    global y1
    global n1
    global occupation_var
    global hc_button
    global cs_button
    global energy_button
    global foodt_button
    global worker_button
    global student_button

    # Radiobutton
    Label(root, text='''1. Do you with any medical problem listed below?
    ‣ Cardiovascular diseases                       
    ‣ Diabetes                                                  
    ‣ Chronic respiratory disease                  
    ‣ Chronic lung disease                              
    ‣ Chronic kidney disease                          
    ‣ Asthma                                                     
    ‣ Obesity                                                     
    ‣ Hyper-tension                                           
    ‣ Cancer                                                      ''', width=80, height=10, font=('bold', 12)).pack()
    sick_var = IntVar()
    y = Radiobutton(root, text='Yes', variable=sick_var, value='1')
    y.pack()
    n = Radiobutton(root, text='No', variable=sick_var, value='2')
    n.pack()

    Label(root, text='''2. Do you exhibiting any symptoms listed below? Or under-quarantine?
    ‣ Loss of smell / taste                                 
    ‣ Dry Cough                                                
    ‣ Fever                                                        
    ‣ Tiredness                                                 
    ‣ Difficulty breathing                                   ''', width=80, height=6, font=('bold', 12)).pack()
    symptom_var = IntVar()
    y1 = Radiobutton(root, text='Yes', variable=symptom_var, value='10')
    y1.pack()
    n1 = Radiobutton(root, text='No', variable=symptom_var, value='11')
    n1.pack()

    Label(root, text='''3. Do your occupation related to:                           ''', width=80,
          height=1, font=('bold', 12)).pack()                                              # Imprint MT Shadow'
    occupation_var = IntVar()
    hc = Radiobutton(root, text='Health-Care worker      ',
                     font=('MS Reference Sans Serif', 10), variable=occupation_var, value='3')
    hc.pack()
    cs = Radiobutton(root, text='Community Services  ', font=(
        'Lucida Sans Typewriter', 10), variable=occupation_var, value='4')
    cs.pack()
    energy = Radiobutton(root, text='Energy                             ', font=(
        'Bookman Old Style', 10), variable=occupation_var, value='5')
    energy.pack()
    foodt = Radiobutton(root, text='Food and Transportation ', font=(
        'Lucida Sans', 10), variable=occupation_var, value='6')
    foodt.pack()
    worker_button = Radiobutton(root, text='Worker                            ', font=(
        'Goudy Old Style', 11), variable=occupation_var, value='7')
    worker_button.pack()
    student_button = Radiobutton(root, text='Student                            ', font=(
        'Comic Sans MS', 10), variable=occupation_var, value='8')
    student_button.pack()
    Non_button = Radiobutton(root, text='Non-working                      ',
                             font=('Kannada Sangam MN', 10), variable=occupation_var, value='9')
    Non_button.pack()

    # submit and cancel button
    submit_button = Button(root, text='Submit', width=10,
                           bg='light green', font=('bold', 10), command=msg).pack()
    cancel_button = Button(root, text='Cancel', width=10, bg='pink', font=(
        'bold', 10), command=root.destroy).pack()

    root.mainloop()

# Public User Menu
# tjp_part3


def user_data():
    rootjp = Tk()
    rootjp.title('User status')
    rootjp.geometry('550x500')
    # ____________read from info.txt______________
    lines_list = filter(None, open("info.txt", "r").read().splitlines())
    for line in lines_list:
        if username1 in line:
            showthis = line.split(',')
            Label(rootjp, text='Please often update your status', padx=100, pady=10, font=(
                'comic sans ms', 20), bg='light blue').grid(row=0, column=0, columnspan=10)
            show_1 = Label(rootjp, text=(f'RSVP: {showthis[1]}'), font=16)
            show_2 = Label(rootjp, text=(f'NAME: {showthis[2]}'), font=16)
            show_3 = Label(rootjp, text=(f'AGE: {showthis[3]}'), font=16)
            show_4 = Label(rootjp, text=(
                f'PHONE NUMBER: {showthis[4]}'), font=16)
            show_5 = Label(rootjp, text=(f'POSTCODE: {showthis[5]}'), font=16)
            show_6 = Label(rootjp, text=(
                f'MEDICAL PROBLEM: {showthis[6]}'), font=16)
            show_7 = Label(rootjp, text=(
                f'SYMPTHOM/UNDER-QUARANTINE: {showthis[7]}'), font=16)
            show_8 = Label(rootjp, text=(
                f'OCCUPATION: {showthis[8]}'), font=16)

            show_1.grid(row=1, column=0, sticky='w')
            show_2.grid(row=5, column=0, sticky='w')
            show_3.grid(row=7, column=0, sticky='w')
            show_4.grid(row=9, column=0, sticky='w')
            show_5.grid(row=11, column=0, sticky='w')
            show_6.grid(row=15, column=0, sticky='w')
            show_7.grid(row=17, column=0, sticky='w')
            show_8.grid(row=19, column=0, sticky='w')
            close_button = Button(rootjp, text='Close', width=10, bg='pink', font=(
                'bold', 10), command=rootjp.destroy).grid(row=24, column=0, sticky='E')
    rootjp.mainloop()


def rsvp_save():
    global rsvp_save
    now = open("info.txt", "r+")
    with now as f:
        read_f = f.readlines()
        f.seek(0)
        l = list()
        for line in read_f:
            if username1 in line:
                l.extend((line).split(','))
                f.truncate()
            else:
                f.write(line)

        del l[1]
        l.insert(1, rsvp_info)
        f.write('\n'+l[0]+','+l[1]+','+l[2]+','+l[3]+',' +
                l[4]+','+l[5]+','+l[6]+','+l[7]+','+l[8])
    now.close()
    l.clear()
    rsvproot.destroy()


def rsvp_no():
    global rsvpno
    rsvpno = Toplevel()
    rsvpno.geometry('500x500')
    rsvpno.title('RSVP NO')
    Label(rsvpno, text="We Love You, Please Get Vaccinated", bg="light blue",
          width=400, height=1, font=("Comic Sans MS", 18)).pack()

    Label(rsvpno, text='''Reason: ''',
          width=80, height=1, font=('bold', 12)).pack()
    global rsvp_reason
    rsvp_reason = StringVar()
    rsvpno_entry = Entry(rsvpno, textvariable=rsvp_reason, width=50)
    rsvpno_entry.pack()
    Button(rsvpno, text="Submit", height=2, width=40,
           font=("bold", 12), bg='#E6E6FA', command=rsvp_no_if).pack()


def rsvp_no_if():
    if(rsvp_reason.get() == ''):
        messagebox.showwarning('Missing details', 'Please answer')
    else:
        global rsvp_info
        rsvp_info = 'No  ' + rsvp_reason.get()
        messagebox.showinfo('Thank you for responding',
                            'Please get vaccinated ASAP')
        rsvp_save()


def rsvp_if():
    global rsvp_info
    if (rsvp_var.get() == 12):
        rsvp_info = 'Yes'
        rsvp_save()
    elif(rsvp_var.get() == 13):
        rsvp_no()
    else:
        messagebox.showwarning('missing details', 'Please answer')


def rsvp_funct():
    global rsvproot
    rsvproot = Toplevel()
    rsvproot.geometry('500x500')
    rsvproot.title('Update status')
    Label(rsvproot, text='''4. Do you want to be vaccinated?                     ''',
          width=80, height=1, font=('bold', 12)).pack()
    global rsvp_var
    rsvp_var = IntVar()
    rsvpy = Radiobutton(rsvproot, text='Yes', variable=rsvp_var, value='12')
    rsvpy.pack()
    rsvpn = Radiobutton(rsvproot, text='No', variable=rsvp_var, value='13')
    rsvpn.pack()
    Button(rsvproot, text="Submit", height=2, width=40,
           font=("bold", 12), bg='#E6E6FA', command=rsvp_if).pack()
    rsvproot.mainloop()


def button_click():
    top = Tk()
    top.title('Vaccination Details')
    top.geometry('500x500')

    conn = sqlite3.connect('Assignment.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Appointment')
    rows = c.fetchall()

    Label(top, text='Vaccination Details', padx=140, pady=10, font=(
        'Arial', 20), bg='light blue').grid(row=0, column=0, columnspan=10)
    label_1 = Label(top, text='Vaccination Date : ', pady=5)
    label_2 = Label(top, text='Vaccination Time : ', pady=5)
    label_3 = Label(top, text='Vaccination Location : ', pady=5)
    label_4 = Label(top, text='')
    label_5 = Label(top, text='')
    label_1.grid(row=1, column=0, columnspan=2)
    label_2.grid(row=3, column=0, columnspan=2)
    label_3.grid(row=5, column=0, columnspan=2)
    label_4.grid(row=2, column=0, columnspan=2)
    label_5.grid(row=4, column=0, columnspan=2)

    for i in rows:
        if username1 in i:
            label_6 = Label(top, text=i[3])
            label_7 = Label(top, text=i[4])
            label_8 = Label(top, text=i[1])
            label_6.grid(row=1, column=2)
            label_7.grid(row=3, column=2)
            label_8.grid(row=5, column=2)
            break

    Label(top, text=' ').grid(row=6)
    Label(top, text=' ').grid(row=8)

    button_back = Button(
        top, text='RSVP', command=rsvp_funct, padx=100, pady=10)
    button_back.grid(row=7, column=2)
    button_back = Button(
        top, text='Back', command=top.destroy, padx=50, pady=10)
    button_back.grid(row=9, column=2)
    top.mainloop


def login_sucess():
    screen1 = Toplevel()
    screen1.title("User Menu")
    screen1.geometry("600x500")
    Button(screen1, text="Update Personal status", height=3,
           width=30, font=("bold", 12), bg='#7CFC00', command=r1).pack()
    Label(screen1, text='').pack()

    Button(screen1, text="View Personal status", height=3,
           width=30, font=("bold", 12), bg='#B76E79', command=user_data).pack()
    Label(screen1, text='').pack()

    button_1 = Button(screen1, text='Vaccination Details', height=3,
                      width=30, font=('bold', 12), bg='alice blue', command=button_click)
    button_1.pack()

    screen1.mainloop

# login screen choice


def login():
    screenL = Toplevel()
    screenL.title("Login")
    screenL.geometry("600x500")
    Label(screenL, text="Login", bg="light blue",
          width=400, height=2, font=("bold", 16)).pack()
    Label(screenL, text="").pack()
    Button(screenL, text="Public", height=2, width=40,
           font=("bold", 12), command=public).pack()
    Label(screenL, text="").pack()
    Button(screenL, text="Administrator", height=2,
           width=40, font=("bold", 12), command=admin).pack()

# login verification


def login_verify():
    global username1
    global userpassword1
    username1 = username_verify.get()
    userpassword1 = userpassword_verify.get()

    username_entryP.delete(0, END)
    userpassword_entryP.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        f1 = open(username1, 'r')
        v1 = f1.read().splitlines()
        if userpassword1 in v1:
            Label(screenP, text="Login Success",
                  fg="green", font=("calibri", 12)).pack()
            login_sucess()
        else:
            messagebox.showwarning('Invalid', 'Invalid Password')
    else:
        messagebox.showwarning('Invalid', 'Invalid Username')

# public user login


def public():
    global screenP
    screenP = Toplevel()
    screenP.title("Public User")
    screenP.geometry("600x500")
    Label(screenP, text="Public User Login", bg="light blue",
          width=400, height=2, font=("bold", 16)).pack()
    Label(screenP, text="").pack()
    Label(screenP, text="Please enter details below", font=("bold", 16)).pack()
    Label(screenP, text="").pack()

    global username_verify
    global userpassword_verify
    username_verify = StringVar()
    userpassword_verify = StringVar()
    global username_entryP
    global userpassword_entryP

    Label(screenP, text="Name : ", font=("bold", 12)).pack()
    username_entryP = Entry(screenP, textvariable=username_verify, width=50)
    username_entryP.pack()
    Label(screenP, text="").pack()

    Label(screenP, text="Password :", font=("bold", 12)).pack()
    userpassword_entryP = Entry(
        screenP, textvariable=userpassword_verify, width=50)
    userpassword_entryP.pack()
    Label(screenP, text="").pack()
    Button(screenP, text="Login", command=login_verify,
           height=1, width=20, font=("bold", 12)).pack()
    Button(screenP, text="Back", command=screenP.destroy,
           height=1, width=20, font=("bold", 12)).pack()

# tjp_part2


def treeviewlist():
    global my_tree
    global listpg
    listpg = Tk()
    listpg.geometry('990x430')
    listpg.title("Users' status list")

    my_tree = ttk.Treeview(listpg)
    my_tree['column'] = ('priority', 'rsvp', 'username', 'age',
                         'phone', 'postcode', 'medical problem', 'sympthom', 'occupation')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('priority', anchor=W, width=65, minwidth=25)
    my_tree.column('rsvp', anchor=W, width=70, minwidth=25)
    my_tree.column('username', anchor=W, width=140, minwidth=25)
    my_tree.column('age', anchor=W, width=50, minwidth=25)
    my_tree.column('phone', anchor=W, width=100, minwidth=25)
    my_tree.column('postcode', anchor=W, width=100, minwidth=25)
    my_tree.column('medical problem', anchor=W, width=120, minwidth=25)
    my_tree.column('sympthom', anchor=W, width=120, minwidth=25)
    my_tree.column('occupation', anchor=W, width=180, minwidth=25)

    my_tree.heading('#0', text='label', anchor=W)
    my_tree.heading('priority', text='Priority', anchor=W)
    my_tree.heading('rsvp', text='RSVP', anchor=W)
    my_tree.heading('username', text='Username', anchor=W)
    my_tree.heading('age', text='Age', anchor=W)
    my_tree.heading('phone', text='Phone Number', anchor=W)
    my_tree.heading('postcode', text='Postcode', anchor=W)
    my_tree.heading('medical problem', text='Medical Problem', anchor=W)
    my_tree.heading('sympthom', text='Sympthom', anchor=W)
    my_tree.heading('occupation', text='Occupation', anchor=W)

    # read from info.txt and show in treeviewlist
    l = list()
    lines_list = filter(None, open("info.txt", "r").read().splitlines())
    for line in lines_list:
        l.append(line.split(','))
    # - is to reverse
    l.sort(key=lambda x: ((len(x[1])), -(int(x[0]))))
    count = 0
    for record in l:
        my_tree.insert(parent='', index='end', iid=count, values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1
    my_tree.pack()
    close_button = Button(listpg, text='Close', width=10, bg='pink', font=(
        'bold', 10), command=listpg.destroy).pack()
    listpg.mainloop()


def vaccination():
    global root
    global address
    global state
    global city
    global poscode
    global capacity
    global c

    root = Toplevel()
    root.title('Vaccination Center')

    conn = sqlite3.connect('Assignment.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Vaccination(
     address text,
     city text,
     state text,
     poskod integer,
     capacity integer)""")

    label6 = Label(root, text='Add vaccination center',
                   font=('comic sans ms', 16)).grid(row=0, column=1, columnspan=2)
    label1 = Label(root, text='Address', font=('comic sans ms', 16))
    label2 = Label(root, text='State', font=('comic sans ms', 16))
    label3 = Label(root, text='City', font=('comic sans ms', 16))
    label4 = Label(root, text='Poscode', font=('comic sans ms', 16))
    label5 = Label(root, text='Capacity', font=('comic sans ms', 16))
    label1.grid(row=1, column=0, sticky=W, padx=10)
    label2.grid(row=2, column=0, sticky=W, padx=10)
    label3.grid(row=3, column=0, sticky=W, padx=10)
    label4.grid(row=4, column=0, sticky=W, padx=10)
    label5.grid(row=5, column=0, sticky=W, padx=10)
    address = Entry(root, width=40)
    state = Entry(root, width=40)
    city = Entry(root, width=40)
    poscode = Entry(root, width=40)
    capacity = Entry(root, width=40)
    address.grid(row=1, column=1)
    state.grid(row=2, column=1)
    city.grid(row=3, column=1)
    poscode.grid(row=4, column=1)
    capacity.grid(row=5, column=1)

    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    poscode.delete(0, END)
    capacity.delete(0, END)

    root.geometry('800x600')
    Button(root, command=submit_button, padx=50,
           pady=20, text='Submit').grid(column=1)
    Button(root, text="Assign appointment", height=1,
           width=20, font=("bold", 12), command=assign).grid(column=1)
    conn.close()

    root.mainloop()


def submit_button():

    conn = sqlite3.connect('Assignment.db')
    c = conn.cursor()

    if address.get() == '' or state.get() == '' or city.get() == '' or city.get() == '' or poscode.get() == '' or capacity.get() == '':
        messagebox.showinfo('Warning', 'Please fill up all boxes')

    else:
        conn = sqlite3.connect('Assignment.db')
        c = conn.cursor()

        c.execute("INSERT INTO 'Vaccination' VALUES(:Address,:State,:City,:Poscode,:Capacity)",
                  {
                      'Address': address.get(),
                      'State': state.get(),
                      'City': city.get(),
                      'Poscode': poscode.get(),
                      'Capacity': capacity.get()})
        address.delete(0, END)
        state.delete(0, END)
        city.delete(0, END)
        poscode.delete(0, END)
        capacity.delete(0, END)
    root.geometry('800x600')
    conn.commit()
    print('Successfully added to database')
    conn.close()

    root.geometry('800x600')


def dot():
    global screen_b
    global conn
    global c
    global tv

    screen_b = Tk()
    screen_b.geometry('1500x500')
    screen_b.title('Appointment list')

    conn = sqlite3.connect('Assignment.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS Appointment(
     Name text,
     
     Vaccination_place text,
     Phone_number integer,

     Date integer,
     time integer)""")

    sql = 'SELECT * FROM Appointment'
    c.execute(sql)
    rows = c.fetchall()
    total = c.rowcount
    print('Total data Entries:'+str(total))
    # print(rows)

    tv = ttk.Treeview(screen_b, columns=(1, 2, 3, 4, 5, ),
                      show='headings', height='5')

    tv.heading(1, text='Name')

    tv.heading(2, text='Vaccination_place')
    tv.heading(3, text='Phone_number')
    tv.heading(4, text='Date')
    tv.heading(5, text='time')

    for i in rows:
        tv.insert('', 'end', values=i,)
        tv.pack()

    conn.close()


# DATABASE

# Create a database or connect to one
    conn = sqlite3.connect('Assignment.db')

# Create cursor
    c = conn.cursor()
    # c.execute("""CREATE TABLE Appointment(
    # Name text,
    # RSVP text,
    # Vaccination_place text,
    # Phone_number integer,

    # Date integer,
    # time integer)""")

# Create table


def updateljy():
    # Create a database or connect to one
    conn = sqlite3.connect('Assignment.db')

    # Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Appointment(
     Name text,
     
     Vaccination_place text,
     Phone_number integer,

     Date integer,
     time integer)""")

    # Date integer,
    # time integer)""")

    record_id = delete_box.get()

    c.execute("""UPDATE Appointment SET
        Name = :name, 
        
        Vaccination_place = :vp,
        Phone_number = :pn,
        Date = :date,
        Time = :time  

        WHERE oid = :oid""",
              {
                  'name': Name_editor.get(),


                  'pn': phone_editor.get(),
                  'date': date_editor.get(),
                  'time': Time_editor.get(),
                  'vp': vaccination_editor.get(),
                  'oid': record_id
              })

    # Commit change
    conn.commit()

    # Close connection
    conn.close()
    editor.destroy()


# Create edit function to update a record


def edit():
    global editor
    editor = Toplevel()
    editor.title('Update A Record')
    editor.geometry('500x500')

    # Create a database or connect to one
    conn = sqlite3.connect('Assignment.db')

    # Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Appointment(
     Name text,
     
     Vaccination_place text,
     Phone_number integer,

     Date integer,
     time integer)""")

    # Date integer,
    # time integer)""")

    record_id = delete_box.get()
    # Query the database
    c.execute('SELECT * FROM Appointment WHERE oid='+record_id)
    records = c.fetchall()

    # Create global variables for text box names

    global Name_editor
    global phone_editor
    global date_editor
    global Time_editor
    global vaccination_editor

    # Create text box
    Name_editor = Entry(editor, width=30)
    Name_editor.grid(row=0, column=1, padx=20)

    vaccination_editor = Entry(editor, width=30)
    vaccination_editor.grid(row=1, column=1, padx=20)

    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=2, column=1, padx=20)

    date_editor = Entry(editor, width=30)
    date_editor.grid(row=3, column=1, padx=20)

    Time_editor = Entry(editor, width=30)
    Time_editor.grid(row=4, column=1, padx=20)

    # Create text box label
    name_label = Label(editor, text='Name :')
    name_label.grid(row=0, column=0)

    vaccination_label = Label(editor, text='Vaccination place:')
    vaccination_label.grid(row=1, column=0)

    phone_label = Label(editor, text='Phone number:')
    phone_label.grid(row=2, column=0)

    date_label = Label(editor, text='Date :')
    date_label.grid(row=3, column=0)

    Time_label = Label(editor, text='Time :')
    Time_label.grid(row=4, column=0)

    # Loop Thru Result
    for data in records:
        Name_editor.insert(0, data[0])

        vaccination_editor.insert(0, data[1])
        phone_editor.insert(0, data[2])
        date_editor.insert(0, data[3])
        Time_editor.insert(0, data[4])

    # Create a save button to save editor record
    save_button = Button(editor, text='Save records', command=updateljy)
    save_button.grid(row=6, column=0, columnspan=2,
                     pady=10, padx=10, ipadx=144)


# Create submit function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('Assignment.db')

    # Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Appointment(
     Name text,
     
     Vaccination_place text,
     Phone_number integer,

     Date integer,
     time integer)""")
    # Insert Into Table
    c.execute("INSERT INTO 'Appointment' VALUES(:Name ,:Vaccination_place,:Phone_number,:Date,:Time)",
              {
                  'Name': name.get(),

                  'Vaccination_place': vaccination_p.get(),
                  'Phone_number': ph.get(),
                  'Date': date.get(),
                  'Time': time.get(), })

    # Commit change
    conn.commit()

    # Close connection
    conn.close()

    # Clear text box
    name.delete(0, END)

    vaccination_p.delete(0, END)
    ph.delete(0, END)
    date.delete(0, END)
    time.delete(0, END)

# Create query funtion


def query():
    root = Toplevel()
    root.title('Records')
    # Create a database or connect to one
    conn = sqlite3.connect('Assignment.db')

    # Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Appointment(
     Name text,
    
     Vaccination_place text,
     Phone_number integer,

     Date integer,
     time integer)""")

    # Query the database
    c.execute('SELECT *, oid FROM Appointment')
    records = c.fetchall()
    # print(records)

    # Loop Thru Result
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit change
    conn.commit()

    # Close connection
    conn.close()


def ed1():
    global newtab
    global query_button
    global delete_button
    global edit_button
    global delete_box
    newtab = Toplevel()
    newtab.title('Show And Edit Records')
    delete_label = Label(newtab, text='Last No: ',
                         font=('comic sans ms', 16),)
    delete_label.grid(row=0, column=0, columnspan=1,
                      pady=5, padx=5)
    delete_box = Entry(newtab, width=30)
    delete_box.grid(row=0, column=2, columnspan=2,
                    pady=10, padx=10)
    edit_buttons = Button(
        newtab, text='Edit Records', command=edit)
    edit_buttons.grid(row=1, column=2, columnspan=1,
                      pady=10, padx=10)
    query_button = Button(newtab, text='Show records', command=query)
    query_button.grid(row=1, column=0, columnspan=2,
                      pady=10, padx=10)


def assign():
    global name
    global vaccination_p
    global ph
    global date
    global time
    global submit_buttons

    root = Toplevel()
    conn = sqlite3.connect('Assignment.db')
    root.title('Assign Appointment')
    root.geometry('1200x500')
#_____________________________treeview_2_____________________
    treeview_frame=Frame(root)
    treeview_frame.grid(row=0, column=1)

    my_tree = ttk.Treeview(root)
    my_tree['column'] = ('priority', 'rsvp', 'username', 'age',
                         'phone', 'postcode', 'medical problem', 'sympthom', 'occupation')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('priority', anchor=W, width=65, minwidth=25)
    my_tree.column('rsvp', anchor=W, width=70, minwidth=25)
    my_tree.column('username', anchor=W, width=140, minwidth=25)
    my_tree.column('age', anchor=W, width=50, minwidth=25)
    my_tree.column('phone', anchor=W, width=100, minwidth=25)
    my_tree.column('postcode', anchor=W, width=100, minwidth=25)
    my_tree.column('medical problem', anchor=W, width=120, minwidth=25)
    my_tree.column('sympthom', anchor=W, width=120, minwidth=25)
    my_tree.column('occupation', anchor=W, width=180, minwidth=25)

    my_tree.heading('#0', text='label', anchor=W)
    my_tree.heading('priority', text='Priority', anchor=W)
    my_tree.heading('rsvp', text='RSVP', anchor=W)
    my_tree.heading('username', text='Username', anchor=W)
    my_tree.heading('age', text='Age', anchor=W)
    my_tree.heading('phone', text='Phone Number', anchor=W)
    my_tree.heading('postcode', text='Postcode', anchor=W)
    my_tree.heading('medical problem', text='Medical Problem', anchor=W)
    my_tree.heading('sympthom', text='Sympthom', anchor=W)
    my_tree.heading('occupation', text='Occupation', anchor=W)

    # read from info.txt and show in treeviewlist
    l = list()
    lines_list = filter(None, open("info.txt", "r").read().splitlines())
    for line in lines_list:
        l.append(line.split(','))
    # - is to reverse
    l.sort(key=lambda x: ((len(x[1])), -(int(x[0]))))
    count = 0
    for record in l:
        my_tree.insert(parent='', index='end', iid=count, values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1
    my_tree.grid(row=0, column=1, padx=20)

#_______________________________________________
    c = conn.cursor()

    query1 = "SELECT Address,State,City,Poskod FROM Vaccination"
    mydata = c.execute(query1)
    total = c.rowcount
    rows = c.fetchall()
    name = Entry(root, width=30)

    name.grid(row=1, column=1, padx=20)

    vaccination_p = ttk.Combobox(root, values=rows)
    vaccination_p.grid(row=2, column=1, padx=20)

    ph = Entry(root, width=30)
    ph.grid(row=3, column=1, padx=20)

    date = Entry(root, width=30)
    date.grid(row=4, column=1, padx=20)

    time = Entry(root, width=30)
    time.grid(row=5, column=1, padx=20)


# Create text box label
    Name = Label(root, text=' Name :', font=('comic sans ms', 16))
    Name.grid(row=1, column=0)

    vp = Label(root, text='Vaccination place :', font=('comic sans ms', 16))
    vp.grid(row=2, column=0)

    phone = Label(root, text='Phone Number:', font=('comic sans ms', 16))
    phone.grid(row=3, column=0)

    Date = Label(root, text='Date :', font=('comic sans ms', 16))
    Date.grid(row=4, column=0)

    Time = Label(root, text='Time :', font=('comic sans ms', 16))
    Time.grid(row=5, column=0)

    # Create submit button
    submit_buttons = Button(
        root, text='Add records', command=submit)
    submit_buttons.grid(row=6, column=0, columnspan=2,
                        pady=10, padx=10, ipadx=100)

    ed = Button(root, text='Show&Edit Records', command=ed1).grid(row=7, column=0, columnspan=2,
                                                                  pady=10, padx=10, ipadx=100)


def admin_menu():
    global screen_Admin
    screen_Admin = Toplevel()
    screen_Admin.title("Administration Menu")
    screen_Admin.geometry("600x500")
    Button(screen_Admin, text="List covid-19 status", height=3,
           width=30, font=("bold", 12), command=treeviewlist).pack()
    Label(screen_Admin, text='').pack()
    Button(screen_Admin, text="Create Vaccination Center&Assign Appointment", height=3,
           width=30, font=("bold", 12), command=vaccination, padx=100, pady=20).pack()
    Label(screen_Admin, text='').pack()
    Button(screen_Admin, text="Assignment list", height=3,
           width=30, font=("bold", 12), command=dot).pack()

    screen_Admin.mainloop


def admin_verify():
    global admin_name
    global admin_password
    admin_name = nameA_verify.get()
    admin_password = passwordA_verify.get()

    nameA_entry.delete(0, END)
    passwordA_entry.delete(0, END)

    if admin_name == "NoobMaster69" and admin_password == "a":
        Label(screenA, text="Login Sucess",
              fg="green", font=("calibri", 12)).pack()
        admin_menu()
    else:
        messagebox.showwarning('Failure', 'You are a failure')


def admin():
    global screenA
    screenA = Toplevel()
    screenA.title("Administrator")
    screenA.geometry("600x500")
    Label(screenA, text="Administrator Login", bg="light blue",
          width=400, height=2, font=("bold", 16)).pack()
    Label(screenA, text="").pack()
    Label(screenA, text="Please enter details below", font=("bold", 16)).pack()
    Label(screenA, text="").pack()

    global nameA_verify
    global passwordA_verify
    nameA_verify = StringVar()
    passwordA_verify = StringVar()
    global nameA_entry
    global passwordA_entry

    Label(screenA, text="Name : ", font=("bold", 12)).pack()
    nameA_entry = Entry(screenA, textvariable=nameA_verify, width=50)
    nameA_entry.pack()
    Label(screenA, text="").pack()
    Label(screenA, text="Password :", font=("bold", 12)).pack()
    passwordA_entry = Entry(screenA, textvariable=passwordA_verify, width=50)
    passwordA_entry.pack()
    Label(screenA, text="").pack()
    Button(screenA, text="Login", command=admin_verify,
           height=1, width=20, font=("bold", 12)).pack()
    Button(screenA, text="Back", command=screenA.destroy,
           height=1, width=20, font=("bold", 12)).pack()

# Main Screen


def main_screen():
    screen = Tk()
    screen.geometry("550x450")
    screen.title("Covid-19 Vaccination Registration ")
    Label(text="Covid-19 Vaccination Registration ", bg="light blue",
          width=400, height=2, font=("bold", 16)).pack()
    Label(text="").pack()
    Button(text="Login", height=2, width=40,
           font=("bold", 12), command=login).pack()
    Label(text="").pack()
    Button(text="Register", height=2, width=40,
           font=("bold", 12), command=register).pack()
    screen.mainloop()


main_screen()
