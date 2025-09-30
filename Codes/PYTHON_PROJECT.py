from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from OWN_FILES import login as l1
import mysql.connector as mysql
from random import randint , sample

#Mysql connecting Part----------------------------------------------------------------->

#Connecting MYSQL Database with python 
my_DB=mysql.connect(user="root",password="Thillai@05",host="localhost")
if my_DB.is_connected()==True:
    print("Database connected sucessfully...")
else:
    print("Error in connecting Python With Database")

cursor=my_DB.cursor()

#-------------------------------------------------------------------------------------->

def Retuning_First_Things_To_False():

    #Assigning default False value to the values so that once their event started they turn to True
    global Confirm_button_click_check
    global username_check_button
    
    Confirm_button_click_check=False
    new_user_SEX="--Select--"
    username_check_button=False
    
def new_user_request():
    global personal_details_message
    global SEX_entry
    global New_User_AGE
    global NEW_Mobile_Len
    global New_User_Mobile_No
    global NEW_Aadar_Len
    global New_User_Aadar_No
    global personal_details_message_Says
    global NEW_Pincode_Len
    global New_User_Pincode
    global Parmanent_address_message_Says
    global NEW_DOB_Len
    global New_User_DOB_check_1
    global NEW_USER_DOB_1
    global Current_address_message
    global NEW_C_Pincode_Len
    global New_User_C_Pincode
    global Current_address_message_Says

    personal_details_message=False
    SEX_entry=False
    New_User_AGE=False
    NEW_Mobile_Len=False
    New_User_Mobile_No=False
    NEW_Aadar_Len=False
    New_User_Aadar_No=False
    personal_details_message_Says=False
    New_User_Pincode=False
    NEW_Pincode_Len=False
    Parmanent_address_message_Says=False
    NEW_DOB_Len=False
    New_User_DOB_check_1=False
    NEW_USER_DOB_1=False
    Current_address_message=False
    NEW_C_Pincode_Len=False
    New_User_C_Pincode=False
    Current_address_message_Says=False
    

    #checking whether all the entries in Personal Details are filled or not -------------------------------------------------------------------------------------------->
    if new_user_name.get()!="None" and new_user_father.get()!="None" and new_user_mother.get()!="None" and new_user_DOB.get()!="None":
        if new_user_AGE.get()!="None" and new_user_Aadar.get()!="None" and new_user_mobile.get()!="None" and new_user_email.get()!="None" and new_user_EDQ.get()!="None":
            personal_details_message=True
        else:
            personal_details_message=False
    else:
        personal_details_message=False

    if SEX_combobox.get()=="Male" or SEX_combobox.get()=="Female" or SEX_combobox.get()=="Transgender":
        SEX_entry=True
    else:
        SEX_entry=False

    #DOB Check whether input is integer or notvand in correct format ------------->1     
    if len(new_user_DOB.get())==8:
        NEW_DOB_Len=True
    else:
        NEW_DOB_Len=False

    if NEW_DOB_Len==True:
        if new_user_DOB.get().isdigit():
            New_User_DOB_check_1=True
        else:
            New_User_DOB_check_1=False
    else:
        New_User_DOB_check_1=False

    if New_User_DOB_check_1==True:
        NEW_DOB_1_Check=new_user_DOB.get()
        aa1=int(NEW_DOB_1_Check)
        aa2=aa1%10000
        New_User_DOB_Year=aa1//10000
        New_User_DOB_Month=aa2//100
        New_User_DOB_Date=aa2%100

        #Giving Year contition between 1940 and present
        if New_User_DOB_Year>=1940 and New_User_DOB_Year<=2023:

            #Month Should Be between 1 and 12
            if New_User_DOB_Month>=1 and New_User_DOB_Month<=12:

                #Separating Months With 31 Days , 30 Days and 28 Days
                if New_User_DOB_Month==1 or New_User_DOB_Month==3 or New_User_DOB_Month==5 or New_User_DOB_Month==7 or New_User_DOB_Month==8 or New_User_DOB_Month==10 or New_User_DOB_Month==12:
                    if New_User_DOB_Date>=1 and New_User_DOB_Date<=31:
                        NEW_USER_DOB_1=True
                    else:
                        NEW_USER_DOB_1=False
                        
                elif New_User_DOB_Month==4 or New_User_DOB_Month==6 or New_User_DOB_Month==9 or New_User_DOB_Month==11:
                    if New_User_DOB_Date>=1 and New_User_DOB_Date<=30:
                        NEW_USER_DOB_1=True
                    else:
                        NEW_USER_DOB_1=False
                        
                elif New_User_DOB_Month==2:
                    if New_User_DOB_Date>=1 and New_User_DOB_Date<=28:
                        NEW_USER_DOB_1=True
                    else:
                        NEW_USER_DOB_1=False
                else:
                    NEW_USER_DOB_1=False
                    
            else:
                NEW_USER_DOB_1=False

        else:
            NEW_USER_DOB_1=False

    else:
        NEW_USER_DOB_1=False

    #AGE Check whether AGE input is integer or not ------------->2
    if new_user_AGE.get().isdigit():
        New_User_AGE=True
    else:
        New_User_AGE=False

    #Mobile Number Check whether input is integer or not ------------->3
    if len(new_user_mobile.get())==10:
        NEW_Mobile_Len=True
    else:
        NEW_Mobile_Len=False

    if NEW_Mobile_Len==True:
        if new_user_mobile.get().isdigit():
            New_User_Mobile_No=True
        else:
             New_User_Mobile_No=False
    else:
        New_User_Mobile_No=False

    #Aadar Number Check whether input is integer or not ------------->4
    if len(new_user_Aadar.get())==12:
        NEW_Aadar_Len=True
    else:
        NEW_Aadar_Len=False

    if NEW_Aadar_Len==True:
        if new_user_Aadar.get().isdigit():
            New_User_Aadar_No=True
        else:
            New_User_Aadar_No=False
    else:
        New_User_Aadar_No=False

    #FULL CORRECTION OF PERSONAL DETAILS---------------------------------->>> 1
    if personal_details_message==True and SEX_entry==True and NEW_USER_DOB_1==True and New_User_AGE==True and  New_User_Mobile_No==True and New_User_Aadar_No==True:
        personal_details_message_Says=True
    else:
        personal_details_message_Says=False

    #checking whether all the entries in parmanent_address are filled or not--------------------------------------------------------------------------------->
    if new_user_nationality.get()!="None" and new_user_state.get()!="None" and new_user_district.get()!="None":
        if new_user_P_address_1.get()!="None" and new_user_P_address_2.get()!="None" and new_user_P_address_3.get()!="None" and new_user_P_address_4.get()!="None":
            Parmanent_address_message=True
        else:
            Parmanent_address_message=False
    else:
        Parmanent_address_message=False

    #Pincode For Parmanent Address Check whether input is integer or not ------------->5
    if len(new_user_P_address_4.get())==6:
        NEW_Pincode_Len=True
    else:
        NEW_Pincode_Len=False

    if NEW_Pincode_Len==True:
        if new_user_P_address_4.get().isdigit():
            New_User_Pincode=True
        else:
            New_User_Pincode=False
    else:
        New_User_Pincode=False

    #FULL CORRECTION OF Parmanent Address---------------------------------->>> 2
    if Parmanent_address_message==True and New_User_Pincode==True:
        Parmanent_address_message_Says=True
    else:
        Parmanent_address_message_Says=False

    #Checking whether current address Chosen For Entry and its entries are correct ------------->6
    if Current_Address_Entry==True:
        if new_user_CA_1.get()!="None" and new_user_CA_2.get()!="None" and new_user_C_address_1.get()!="None" and new_user_C_address_2.get()!="None" and new_user_C_address_3.get()!="None" and new_user_C_address_4.get()!="None":
            if new_user_CA_1.get()!="" and new_user_CA_2.get()!="" and new_user_C_address_1.get()!="" and new_user_C_address_2.get()!="" and new_user_C_address_3.get()!="" and new_user_C_address_4.get()!="":
                Current_address_message=True
            else:
                Current_address_message=False
        else:
            Current_address_message=False
    else:
        Current_address_message=False

    #Pincode For Current Address Check whether input is integer or not ------------->7
    if Current_Address_Entry==True:        
        if len(new_user_C_address_4.get())==6:
            NEW_C_Pincode_Len=True
        else:
            NEW_C_Pincode_Len=False

        if NEW_C_Pincode_Len==True:
            if new_user_C_address_4.get().isdigit():
                New_User_C_Pincode=True
            else:
                 New_User_C_Pincode=False
        else:
            New_User_C_Pincode=False
    else:
        pass

    #FULL CORRECTION OF Current Address if Chosen---------------------------------->>> 3
    if Current_address_message==True and New_User_C_Pincode==True:
        Current_address_message_Says=True
    else:
        Current_address_message_Says=False


    
    
        
    def Add_Details_To_Database():

        #Getting The Entered Values And Making it f'string And Adding the Details to the New User Database
        NEW_Username=new_user_username.get()
        NEW_Password=new_user_password.get()
        NEW_Name=new_user_name.get()
        NEW_Sex=SEX_combobox.get()
        NEW_Father=new_user_father.get()
        NEW_Mother=new_user_mother.get()
        NEW_DOB=new_user_DOB.get()
        NEW_Age=new_user_AGE.get()
        NEW_Aadar=new_user_Aadar.get()
        NEW_Mobile=new_user_mobile.get()
        NEW_Email=new_user_email.get()
        NEW_Education=new_user_EDQ.get()
        NEW_Nationality=new_user_nationality.get()
        NEW_State=new_user_state.get()
        NEW_District=new_user_district.get()
        NEW_P_A_1=new_user_P_address_1.get()
        NEW_P_A_2=new_user_P_address_2.get()
        NEW_P_A_3=new_user_P_address_3.get()
        NEW_P_A_4=new_user_P_address_4.get()

        #Step 2 ----> Storing the values in f'string
        global NEW_Username_1
        global NEW_Password_1
        global NEW_Name_1
        global NEW_Sex_1
        global NEW_Father_1
        global NEW_Mother_1
        global NEW_DOB_1
        global NEW_Age_1
        global NEW_Aadar_1
        global NEW_Mobile_1
        global NEW_Email_1
        global NEW_Education_1
        global NEW_Nationality_1
        global NEW_State_1
        global NEW_District_1
        global NEW_P_A_1_1
        global NEW_C_A_1_1
        global NEW_C_A_2_1
        global NEW_C_A_3_1
        
        NEW_Username_1=f"'{NEW_Username}'"
        NEW_Password_1=f"'{NEW_Password}'"
        NEW_Name_1=f"'{NEW_Name}'"
        NEW_Sex_1=f"'{NEW_Sex}'"
        NEW_Father_1=f"'{NEW_Father}'"
        NEW_Mother_1=f"'{NEW_Mother}'"
        NEW_DOB_1=f"'{NEW_DOB}'"
        NEW_Age_1=f"'{NEW_Age}'"
        NEW_Aadar_1=f"'{NEW_Aadar}'"
        NEW_Mobile_1=f"'{NEW_Mobile}'"
        NEW_Email_1=f"'{NEW_Email}'"
        NEW_Education_1=f"'{NEW_Education}'"
        NEW_Nationality_1=f"'{NEW_Nationality}'"
        NEW_P_A_1_1=f"'{NEW_P_A_1},\n{NEW_P_A_2},\n{NEW_State},{NEW_P_A_3},\n{NEW_P_A_4}'"

        
        if Current_Address_Entry==True:
            NEW_C_A_1=new_user_CA_1.get()
            NEW_C_A_2=new_user_CA_2.get()
            NEW_C_A_3=new_user_C_address_1.get()
            NEW_C_A_4=new_user_C_address_2.get()
            NEW_C_A_5=new_user_C_address_3.get()
            NEW_C_A_6=new_user_C_address_4.get()
            
            NEW_C_A_3_1=f"'{NEW_C_A_3},\n{NEW_C_A_4},\n{NEW_C_A_1},{NEW_C_A_5},\n{NEW_C_A_6}'"

        else:
            pass
               
        if Current_Address_Entry==True:
            #P Address NOT Same As C Address
            Database_Insert_1=f"Insert into New_User_Details VALUES ({NEW_Username_1},{NEW_Password_1},{NEW_Name_1},{NEW_Sex_1},{NEW_Father_1},{NEW_Mother_1},{NEW_DOB_1},{NEW_Age_1},{NEW_Aadar_1},{NEW_Mobile_1},{NEW_Email_1},{NEW_Education_1},{NEW_Nationality_1},{NEW_P_A_1_1},{NEW_C_A_3_1})"
            cursor.execute("use new_user_account")
            cursor.execute(Database_Insert_1)
            my_DB.commit()
        else:
            #P Address Same As C Address
            Database_Insert_2=f"Insert into New_User_Details VALUES ({NEW_Username_1},{NEW_Password_1},{NEW_Name_1},{NEW_Sex_1},{NEW_Father_1},{NEW_Mother_1},{NEW_DOB_1},{NEW_Age_1},{NEW_Aadar_1},{NEW_Mobile_1},{NEW_Email_1},{NEW_Education_1},{NEW_Nationality_1},{NEW_P_A_1_1},'SAME AS PARMANENT ADDRESS')"
            cursor.execute("use new_user_account")
            cursor.execute(Database_Insert_2)
            my_DB.commit()

    #Current Address Errors----------------------------------------------->>>>1
    def New_User_Request_Cuurent_Address_Error():
        
        if Current_address_message==False:
            messagebox.showerror('ERROR','Fill Everything In Current Address Box')
        else:
            pass

        if Current_address_message==True:
            if NEW_C_Pincode_Len==False:
                messagebox.showerror('ERROR','Fll Current Address Pincode properly\n(ONLY 6 Digits)')
            elif New_User_C_Pincode==False:
                messagebox.showerror('ERROR','Current Address Pincode Also should only in Numbers')
            else:
                messagebox.showerror('ERROR','Unknown Error In Current Address Box')
        else:
            pass
        
    #Personal Details and Parmanent Address Errors----------------------------------------------->>>>2 
    def New_User_Request_Personal_Permanent_Address_Error():

        if personal_details_message==False and Parmanent_address_message==False:
            messagebox.showerror('ERROR','Fill Everything In Personal Details and Parmanent Address Box')
        elif personal_details_message==False:
            messagebox.showerror('ERROR','Fill Everything In Personal Details Box')
        elif Parmanent_address_message==False:
            messagebox.showerror('ERROR','Fill Everything In Parmanent Address Box')
        else:
            pass
        if personal_details_message==True:
            #Personal Details Error----------->
            if SEX_entry==False and NEW_USER_DOB_1==False and New_User_AGE==False and  New_User_Mobile_No==False and New_User_Aadar_No==False:
                messagebox.showerror('ERROR','Fill SEX , Date Of Birth\nAGE , Mobile Number\nand Aadar Numer Properly')
            else:                
                if SEX_entry==False:
                    messagebox.showerror('ERROR','Fill SEX Properly')
                else:
                    pass

                if New_User_DOB_check_1==False:
                    messagebox.showerror('ERROR','DOB should only in Numbers and ONLY 8 Digits')
                elif NEW_USER_DOB_1==False:
                    
                    #Any Uates in the Future Year mus be corrected here tooo--------------------------->
                    if New_User_DOB_Year<1940 or New_User_DOB_Year>2023:
                        messagebox.showerror('ERROR','Year Must Be Between 1940 and 2023')
                    else:
                        messagebox.showerror('ERROR','Give Correct Format of DOB (YYYYMMDD)...!')
                else:
                    pass


                if NEW_Mobile_Len==False:
                    messagebox.showerror('ERROR','Fll the Mobile Number properly\n(ONLY 10 Characters)')
                elif NEW_Mobile_Len==True and New_User_Mobile_No==False:
                    messagebox.showerror('ERROR','Mobile Number should only in Numbers')
                else:
                    pass


                if NEW_Aadar_Len==False:
                    messagebox.showerror('ERROR','Fll the Aadar Number properly\n(ONLY 12 Characters)')
                elif NEW_Aadar_Len==True and New_User_Aadar_No==False:
                    messagebox.showerror('ERROR','Aadar Number should only in Numbers')
                else:
                    pass
            
        if Parmanent_address_message==True:
            #Parmanent Address Error----------->
            if NEW_Pincode_Len==False:
                messagebox.showerror('ERROR','Fill Pincode properly\n(ONLY 6 Digits)')
            elif NEW_Pincode_Len==True and New_User_Pincode==False:
                messagebox.showerror('ERROR','Pincode should only in Numbers')
            else:
                pass
        else:
            pass

    #Buttons Error----------------------------------------------->>>>3
    def New_User_Request_Buttons_Error():

        if personal_details_message==False and Parmanent_address_message==False and Confirm_button_click_check==False and username_check_button==False:
            messagebox.showerror('ERROR',"Inputs Reqired\nWithouts Inputs Request Can't Be Raised")
        else:
            if Confirm_button_click_check==False and username_check_button==False:
                messagebox.showerror('ERROR','Click On Confirm Button In Current Address Box\nCheck Your UserName Availability And Password Eligibility')
            elif username_check_button==False:
                messagebox.showerror('ERROR','Check Your UserName Availability And Password Eligibility')
            elif Confirm_button_click_check==False:
                messagebox.showerror('ERROR','Click On Confirm Button In Current Address Box')
            else:
                messagebox.showerror('ERROR','Unknown Error In Buttons')
            
        
    #Checking All the Inputs Incase any error sending to error section and poping the error If every input is correct then thankyou message will be shown and request will be sent to the admin 
    if Confirm_button_click_check==True and username_check_button==True:
        if personal_details_message_Says==True and Parmanent_address_message_Says==True:
            if Current_Address_Entry==True:
                if Current_address_message_Says==True:
                    messagebox.showinfo('MESSAGE','Thank You\nRequest Submited Sucessfully...')
                    messagebox.showinfo('MESSAGE','Once Your Request Is Approved\nYour Account Number and Passbook\nWill Reach You Current Address Through Post')
                    messagebox.showinfo('MESSAGE','And A Default Balence Rs.5000/- Will Be Added On Your Behalf')
                    Add_Details_To_Database()
                    Retuning_First_Things_To_False()
                    new_user_frm.destroy()
                    user_frm1.destroy()
                    
                else:
                    New_User_Request_Cuurent_Address_Error()
            else:
                messagebox.showinfo('MESSAGE','Thank You\nRequest Submited Sucessfully...')
                messagebox.showinfo('MESSAGE','Once Your Request Is Approved\nYour Account Number and Passbook\nWill Reach You Address Through Post')
                messagebox.showinfo('MESSAGE','And A Default Balence Rs.5000/- Will Be Added On Your Behalf')
                Add_Details_To_Database()
                Retuning_First_Things_To_False()
                new_user_frm.destroy()
                user_frm1.destroy()
                
        else:
            New_User_Request_Personal_Permanent_Address_Error()
    else:
        New_User_Request_Buttons_Error()
            


    

def New_User_Page():

    #Assigning global to every identifier so that these can be used outside the function
    global new_user_frm
    global new_user_Label_frm_1
    global new_user_Label_frm_2
    global new_user_Label_frm_4
    global new_user_Label_frm_5
    global new_user_name
    global new_user_father
    global new_user_mother
    global new_user_DOB
    global new_user_AGE
    global new_user_Aadar
    global new_user_mobile
    global new_user_email
    global new_user_EDQ
    global new_user_nationality
    global new_user_state
    global new_user_district
    global new_user_P_address_1
    global new_user_P_address_2
    global new_user_P_address_3
    global new_user_P_address_4
    global new_user_username
    global new_user_password
    global new_User_Back
    global new_user_submit
    global Confirm_button_click_check
    global username_check_button
    global personal_details_message_Says
    global Parmanent_address_message_Says
    global Current_Address_Entry

    Confirm_button_click_check=False
    username_check_button=False
    personal_details_message_Says=False
    Parmanent_address_message_Says=False
    Current_Address_Entry=False
 

    def back_2():
        new_user_frm.destroy()

    
    #If User don't have an Acc his details will be cllected in this new frame and request will be raised to admin 
    new_user_frm=Frame(user_frm1,width=1509,height=942,bg="white")
    new_user_frm.place(x=0,y=0)

    #Personal Details Entry Frame--------------------------------------->
    '''
    None Word will defaultly be shown in the entry box once we click the cursor it will dissappeare and we can give a fresh entry
    '''
    def on_enter_1(e):
        name=new_user_name.get()
        if name=='None':
            new_user_name.delete(0,"end")
        else:
            pass

    def on_leave_1(e):
        name=new_user_name.get()
        if name=='':
            new_user_name.insert(0,"None")
            
    
    new_user_Label_frm_1=LabelFrame(new_user_frm,text="Personal Details",font=("dubai","14","bold"),fg="black",bg="white")
    new_user_Label_frm_1.place(x=90,y=70,width=470,height=490)

    new_user_Label_1=Label(new_user_Label_frm_1,text="Account Holder's Name :",font=("dubai","11"),fg="black",bg="white")
    new_user_Label_1.place(x=19,y=13)
    new_user_name=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_name.place(x=190,y=15)
    new_user_name.insert(0,"None")
    new_user_name.bind("<FocusIn>",on_enter_1)
    new_user_name.bind("<FocusOut>",on_leave_1)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=37)#That line under the entry


    new_user_Label_SEX=Label(new_user_Label_frm_1,text="SEX                               :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_SEX.place(x=20,y=49)

    #ComboBox for entering SEX    
    def Comboget(event):
        global new_user_SEX
        new_user_SEX=SEX_combobox.get()
        
    
    SEX_options=["--Select--",
                 "Male",
                 "Female",
                 "Transgender",]
    
    global SEX_combobox
    
    SEX_combobox=ttk.Combobox(new_user_Label_frm_1,width=19,values=SEX_options,justify="center")
    SEX_combobox.current(0)
    SEX_combobox.bind("<<ComboboxSelected>>",Comboget)
    SEX_combobox.place(x=190,y=54)
    
    def on_enter_2(e):
        name=new_user_father.get()
        if name=='None':
            new_user_father.delete(0,"end")
        else:
            pass

    def on_leave_2(e):
        name=new_user_father.get()
        if name=='':
            new_user_father.insert(0,"None")
    
    new_user_Label_2=Label(new_user_Label_frm_1,text="Father's Name              :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_2.place(x=20,y=90)
    new_user_father=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_father.place(x=190,y=95)
    new_user_father.insert(0,"None")
    new_user_father.bind("<FocusIn>",on_enter_2)
    new_user_father.bind("<FocusOut>",on_leave_2)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=117)#That line under the entry 
    
    def on_enter_3(e):
        name=new_user_mother.get()
        if name=='None':
            new_user_mother.delete(0,"end")
        else:
            pass

    def on_leave_3(e):
        name=new_user_mother.get()
        if name=='':
            new_user_mother.insert(0,"None")

    new_user_Label_3=Label(new_user_Label_frm_1,text="Mother's Name             :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_3.place(x=20,y=135)
    new_user_mother=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_mother.place(x=190,y=140)
    new_user_mother.insert(0,"None")
    new_user_mother.bind("<FocusIn>",on_enter_3)
    new_user_mother.bind("<FocusOut>",on_leave_3)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=162)#That line under the entry 

    def on_enter_4(e):
        name=new_user_DOB.get()
        if name=='None':
            new_user_DOB.delete(0,"end")
        else:
            pass

    def on_leave_4(e):
        name=new_user_DOB.get()
        if name=='':
            new_user_DOB.insert(0,"None")

    new_user_Label_4=Label(new_user_Label_frm_1,text="Date Of Birth                 :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_4.place(x=20,y=180)
    new_user_Label_5=Label(new_user_Label_frm_1,text="(YYYYMMDD)",font=("dubai","8"),fg="black",bg="white")
    new_user_Label_5.place(x=20,y=202)
    new_user_DOB=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_DOB.place(x=190,y=185)
    new_user_DOB.insert(0,"None")
    new_user_DOB.bind("<FocusIn>",on_enter_4)
    new_user_DOB.bind("<FocusOut>",on_leave_4)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=206)#That line under the entry

    def on_enter_5(e):
        name=new_user_AGE.get()
        if name=='None':
            new_user_AGE.delete(0,"end")
        else:
            pass

    def on_leave_5(e):
        name=new_user_AGE.get()
        if name=='':
            new_user_AGE.insert(0,"None")

    new_user_Label_6=Label(new_user_Label_frm_1,text="AGE                               :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_6.place(x=20,y=225)
    new_user_AGE=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_AGE.place(x=190,y=230)
    new_user_AGE.insert(0,"None")
    new_user_AGE.bind("<FocusIn>",on_enter_5)
    new_user_AGE.bind("<FocusOut>",on_leave_5)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=252)#That line under the entry 

    def on_enter_6(e):
        name=new_user_Aadar.get()
        if name=='None':
            new_user_Aadar.delete(0,"end")
        else:
            pass

    def on_leave_6(e):
        name=new_user_Aadar.get()
        if name=='':
            new_user_Aadar.insert(0,"None")

    new_user_Label_7=Label(new_user_Label_frm_1,text="Aadar Number              :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_7.place(x=20,y=269)
    new_user_Aadar=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_Aadar.place(x=190,y=274)
    new_user_Aadar.insert(0,"None")
    new_user_Aadar.bind("<FocusIn>",on_enter_6)
    new_user_Aadar.bind("<FocusOut>",on_leave_6)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=296)#That line under the entry 

    def on_enter_7(e):
        name=new_user_mobile.get()
        if name=='None':
            new_user_mobile.delete(0,"end")
        else:
            pass

    def on_leave_7(e):
        name=new_user_mobile.get()
        if name=='':
            new_user_mobile.insert(0,"None")

    new_user_Label_8=Label(new_user_Label_frm_1,text="Mobile Number             :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_8.place(x=20,y=317)
    new_user_mobile=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_mobile.place(x=190,y=322)
    new_user_mobile.insert(0,"None")
    new_user_mobile.bind("<FocusIn>",on_enter_7)
    new_user_mobile.bind("<FocusOut>",on_leave_7)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=343)#That line under the entry 

    def on_enter_8(e):
        name=new_user_email.get()
        if name=='None':
            new_user_email.delete(0,"end")
        else:
            pass

    def on_leave_8(e):
        name=new_user_email.get()
        if name=='':
            new_user_email.insert(0,"None")

    new_user_Label_9=Label(new_user_Label_frm_1,text="Email ID                        :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_9.place(x=20,y=367)
    new_user_email=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_email.place(x=190,y=372)
    new_user_email.insert(0,"None")
    new_user_email.bind("<FocusIn>",on_enter_8)
    new_user_email.bind("<FocusOut>",on_leave_8)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=394)#That line under the entry 

    def on_enter_9(e):
        name=new_user_EDQ.get()
        if name=='None':
            new_user_EDQ.delete(0,"end")
        else:
            pass

    def on_leave_9(e):
        name=new_user_EDQ.get()
        if name=='':
            new_user_EDQ.insert(0,"None")

    new_user_Label_10=Label(new_user_Label_frm_1,text="Education Qualification :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label_10.place(x=19,y=410)
    new_user_EDQ=Entry(new_user_Label_frm_1,width=28,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_EDQ.place(x=190,y=415)
    new_user_EDQ.insert(0,"None")
    new_user_EDQ.bind("<FocusIn>",on_enter_9)
    new_user_EDQ.bind("<FocusOut>",on_leave_9)
    Frame(new_user_Label_frm_1,width=200,height=2,bg="black").place(x=190,y=437)#That line under the entry
    
    #Address Entry Frame--------------------------------------->
    new_user_Label_frm_2=LabelFrame(new_user_frm,text="Parmanent Address",font=("dubai","14","bold"),fg="black",bg="white")
    new_user_Label_frm_2.place(x=600,y=70,width=450,height=345)

    def on_enter_p1(e):
        name=new_user_nationality.get()
        if name=='None':
            new_user_nationality.delete(0,"end")
        else:
            pass

    def on_leave_p1(e):
        name=new_user_nationality.get()
        if name=='':
            new_user_nationality.insert(0,"None")
    
    new_user_Label2_1=Label(new_user_Label_frm_2,text="Nationality                             :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_1.place(x=20,y=20)
    new_user_nationality=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_nationality.place(x=230,y=25)
    new_user_nationality.insert(0,"None")
    new_user_nationality.bind("<FocusIn>",on_enter_p1)
    new_user_nationality.bind("<FocusOut>",on_leave_p1)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=47)#That line under the entry

    def on_enter_p2(e):
        name=new_user_state.get()
        if name=='None':
            new_user_state.delete(0,"end")
        else:
            pass

    def on_leave_p2(e):
        name=new_user_state.get()
        if name=='':
            new_user_state.insert(0,"None")

    new_user_Label2_2=Label(new_user_Label_frm_2,text="State                                        :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_2.place(x=20,y=60)
    new_user_state=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_state.place(x=230,y=65)
    new_user_state.insert(0,"None")
    new_user_state.bind("<FocusIn>",on_enter_p2)
    new_user_state.bind("<FocusOut>",on_leave_p2)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=87)#That line under the entry

    def on_enter_p3(e):
        name=new_user_district.get()
        if name=='None':
            new_user_district.delete(0,"end")
        else:
            pass

    def on_leave_p3(e):
        name=new_user_district.get()
        if name=='':
            new_user_district.insert(0,"None")


    new_user_Label2_3=Label(new_user_Label_frm_2,text="District                                    :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_3.place(x=20,y=100)
    new_user_district=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_district.place(x=230,y=105)
    new_user_district.insert(0,"None")
    new_user_district.bind("<FocusIn>",on_enter_p3)
    new_user_district.bind("<FocusOut>",on_leave_p3)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=127)#That line under the entry

    def on_enter_p4(e):
        name=new_user_P_address_1.get()
        if name=='None':
            new_user_P_address_1.delete(0,"end")
        else:
            pass

    def on_leave_p4(e):
        name=new_user_P_address_1.get()
        if name=='':
            new_user_P_address_1.insert(0,"None")

    
    new_user_Label2_4=Label(new_user_Label_frm_2,text="Parmanent Address Line 1   :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_4.place(x=20,y=140)
    new_user_P_address_1=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_P_address_1.place(x=230,y=145)
    new_user_P_address_1.insert(0,"None")
    new_user_P_address_1.bind("<FocusIn>",on_enter_p4)
    new_user_P_address_1.bind("<FocusOut>",on_leave_p4)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=167)#That line under the entry

    def on_enter_p5(e):
        name=new_user_P_address_2.get()
        if name=='None':
            new_user_P_address_2.delete(0,"end")
        else:
            pass

    def on_leave_p5(e):
        name=new_user_P_address_2.get()
        if name=='':
            new_user_P_address_2.insert(0,"None")

    new_user_Label2_5=Label(new_user_Label_frm_2,text="Parmanent Address Line 2   :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_5.place(x=20,y=180)
    new_user_P_address_2=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_P_address_2.place(x=230,y=185)
    new_user_P_address_2.insert(0,"None")
    new_user_P_address_2.bind("<FocusIn>",on_enter_p5)
    new_user_P_address_2.bind("<FocusOut>",on_leave_p5)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=207)#That line under the entry

    def on_enter_p6(e):
        name=new_user_P_address_3.get()
        if name=='None':
            new_user_P_address_3.delete(0,"end")
        else:
            pass

    def on_leave_p6(e):
        name=new_user_P_address_3.get()
        if name=='':
            new_user_P_address_3.insert(0,"None")
          
    new_user_Label2_6=Label(new_user_Label_frm_2,text="Parmanent Address Line 3   :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_6.place(x=20,y=220)
    new_user_P_address_3=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_P_address_3.place(x=230,y=225)
    new_user_P_address_3.insert(0,"None")
    new_user_P_address_3.bind("<FocusIn>",on_enter_p6)
    new_user_P_address_3.bind("<FocusOut>",on_leave_p6)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=247)#That line under the entry

    def on_enter_p7(e):
        name=new_user_P_address_4.get()
        if name=='None':
            new_user_P_address_4.delete(0,"end")
        else:
            pass

    def on_leave_p7(e):
        name=new_user_P_address_4.get()
        if name=='':
            new_user_P_address_4.insert(0,"None")

    new_user_Label2_7=Label(new_user_Label_frm_2,text="Parmanent Address Pincode :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label2_7.place(x=20,y=260)
    new_user_P_address_4=Entry(new_user_Label_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_P_address_4.place(x=230,y=265)
    new_user_P_address_4.insert(0,"None")
    new_user_P_address_4.bind("<FocusIn>",on_enter_p7)
    new_user_P_address_4.bind("<FocusOut>",on_leave_p7)
    Frame(new_user_Label_frm_2,width=165,height=2,bg="black").place(x=230,y=287)#That line under the entry
    
    #Parmanent And Current Address CheckButton Frame---------->
    def check_button_confirmation():

        #Assigning global to every identifier so that these can be used outside the function
        global new_user_CA_1
        global new_user_CA_2
        global new_user_C_address_1
        global new_user_C_address_2
        global new_user_C_address_3
        global new_user_C_address_4
        global new_user_PACA_back_button
        global Confirm_button_click_check
        global Current_Address_Entry

        #This helps to find whether the person clicked the cnfirm button to confirm his address 
        Confirm_button_click_check=False
        
        def new_user_PACA_back():
            global Confirm_button_click_check
            
            
            Confirm_button_click_check=False
            Current_Address_Entry=False
            new_user_Label_frm_5.destroy()
            Check_Button_1()

        #Checking Which of the CheckButton is Clicked------->
        if Check_button_1.get()=="ON" and Check_button_2.get()=="OFF":
            Confirm_button_click_check=True
            Current_Address_Entry=False
            messagebox.showinfo('MESSAGE','Selected\nParmanent Address SAME as Current Address')
        elif Check_button_1.get()=="OFF" and Check_button_2.get()=="ON":
            Confirm_button_click_check=True
            Current_Address_Entry=True
            new_user_Label_frm_3.destroy()
            new_user_Label_frm_5=LabelFrame(new_user_frm,text="Current Address",font=("dubai","14","bold"),fg="black",bg="white")
            new_user_Label_frm_5.place(x=600,y=425,width=450,height=265)

            def on_enter_c1(e):
                name=new_user_CA_1.get()
                if name=='None':
                    new_user_CA_1.delete(0,"end")
                else:
                    pass

            def on_leave_c1(e):
                name=new_user_CA_1.get()
                if name=='':
                    new_user_CA_1.insert(0,"None")

            new_user_C_1=Label(new_user_Label_frm_5,text="State                                        :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_1.place(x=20,y=30)
            new_user_CA_1=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_CA_1.place(x=230,y=35)
            new_user_CA_1.insert(0,"None")
            new_user_CA_1.bind("<FocusIn>",on_enter_c1)
            new_user_CA_1.bind("<FocusOut>",on_leave_c1)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=57)#That line under the entry

            def on_enter_c2(e):
                name=new_user_CA_2.get()
                if name=='None':
                    new_user_CA_2.delete(0,"end")
                else:
                    pass

            def on_leave_c2(e):
                name=new_user_CA_2.get()
                if name=='':
                    new_user_CA_2.insert(0,"None")


            new_user_C_2=Label(new_user_Label_frm_5,text="District                                     :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_2.place(x=20,y=60)
            new_user_CA_2=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_CA_2.place(x=230,y=65)
            new_user_CA_2.insert(0,"None")
            new_user_CA_2.bind("<FocusIn>",on_enter_c2)
            new_user_CA_2.bind("<FocusOut>",on_leave_c2)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=87)#That line under the entry

            def on_enter_c3(e):
                name=new_user_C_address_1.get()
                if name=='None':
                    new_user_C_address_1.delete(0,"end")
                else:
                    pass

            def on_leave_c3(e):
                name=new_user_C_address_1.get()
                if name=='':
                    new_user_C_address_1.insert(0,"None")

            
            new_user_C_3=Label(new_user_Label_frm_5,text="Current Address Line 1         :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_3.place(x=20,y=90)
            new_user_C_address_1=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_C_address_1.place(x=230,y=95)
            new_user_C_address_1.insert(0,"None")
            new_user_C_address_1.bind("<FocusIn>",on_enter_c3)
            new_user_C_address_1.bind("<FocusOut>",on_leave_c3)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=117)#That line under the entry

            def on_enter_c4(e):
                name=new_user_C_address_2.get()
                if name=='None':
                    new_user_C_address_2.delete(0,"end")
                else:
                    pass

            def on_leave_c4(e):
                name=new_user_C_address_2.get()
                if name=='':
                    new_user_C_address_2.insert(0,"None")

            new_user_C_4=Label(new_user_Label_frm_5,text="Current Address Line 2         :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_4.place(x=20,y=120)
            new_user_C_address_2=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_C_address_2.place(x=230,y=125)
            new_user_C_address_2.insert(0,"None")
            new_user_C_address_2.bind("<FocusIn>",on_enter_c4)
            new_user_C_address_2.bind("<FocusOut>",on_leave_c4)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=147)#That line under the entry

            def on_enter_c5(e):
                name=new_user_C_address_3.get()
                if name=='None':
                    new_user_C_address_3.delete(0,"end")
                else:
                    pass

            def on_leave_c5(e):
                name=new_user_C_address_3.get()
                if name=='':
                    new_user_C_address_3.insert(0,"None")
                    
            new_user_C_5=Label(new_user_Label_frm_5,text="Current Address Line 3         :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_5.place(x=20,y=150)
            new_user_C_address_3=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_C_address_3.place(x=230,y=155)
            new_user_C_address_3.insert(0,"None")
            new_user_C_address_3.bind("<FocusIn>",on_enter_c5)
            new_user_C_address_3.bind("<FocusOut>",on_leave_c5)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=177)#That line under the entry

            def on_enter_c6(e):
                name=new_user_C_address_4.get()
                if name=='None':
                    new_user_C_address_4.delete(0,"end")
                else:
                    pass

            def on_leave_c6(e):
                name=new_user_C_address_4.get()
                if name=='':
                    new_user_C_address_4.insert(0,"None")

            new_user_C_5=Label(new_user_Label_frm_5,text="Current Address Pincode      :",font=("dubai","12"),fg="black",bg="white")
            new_user_C_5.place(x=20,y=180)
            new_user_C_address_4=Entry(new_user_Label_frm_5,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
            new_user_C_address_4.place(x=230,y=185)
            new_user_C_address_4.insert(0,"None")
            new_user_C_address_4.bind("<FocusIn>",on_enter_c6)
            new_user_C_address_4.bind("<FocusOut>",on_leave_c6)
            Frame(new_user_Label_frm_5,width=165,height=2,bg="black").place(x=230,y=207)#That line under the entry

            #Back Button Current Address box to Check box
            new_user_PACA_back_button=Button(new_user_Label_frm_5,text="back",bg="black",relief="ridge",bd=0,font=("castellar","7","bold"),command=new_user_PACA_back)
            new_user_PACA_back_button.place(x=400,y=5)
            
            
        elif Check_button_1.get()=="OFF" and Check_button_2.get()=="OFF":
            Confirm_button_click_check=False
            Current_Address_Entry=False
            messagebox.showerror('ERROR','Select any one of the Ckeckbuttons...!')

        elif Check_button_1.get()=="ON" and Check_button_2.get()=="ON":
            Confirm_button_click_check=False
            Current_Address_Entry=False
            new_user_checkbutton_1.deselect()
            new_user_checkbutton_2.deselect()           
            messagebox.showerror('ERROR','Only one needs to be selected...!')
            
        else:
            pass
        
    def Check_Button_1():

        #Assigning global to every identifier so that these can be used outside the function
        global Check_button_1
        global Check_button_2
        global new_user_checkbutton_1
        global new_user_checkbutton_2
        global new_user_Label_frm_3
        global new_user_PACA_button
        
        new_user_Label_frm_3=LabelFrame(new_user_frm,text="Current Address",font=("dubai","14","bold"),fg="black",bg="white")
        new_user_Label_frm_3.place(x=600,y=425,width=450,height=135)

        Check_button_1=StringVar()
        new_user_checkbutton_1=Checkbutton(new_user_Label_frm_3,bg="white",text="Current Address Same As Parmanent Address !",variable=Check_button_1,onvalue="ON",offvalue="OFF")
        new_user_checkbutton_1.place(x=20,y=20)
        new_user_checkbutton_1.deselect()

        Check_button_2=StringVar()
        new_user_checkbutton_2=Checkbutton(new_user_Label_frm_3,bg="white",text="Current Address NOT Same As Parmanent Address !",variable=Check_button_2,onvalue="ON",offvalue="OFF")
        new_user_checkbutton_2.place(x=20,y=50)
        new_user_checkbutton_2.deselect()

        #check Button Parmanent Address Current Address Check box
        new_user_PACA_button=Button(new_user_Label_frm_3,text="CONFIRM",bg="black",relief="ridge",bd=0,font=("castellar","8","bold"),command=check_button_confirmation)
        new_user_PACA_button.place(x=350,y=80)
    Check_Button_1()

    #UserName Password Entry Frame---------------------------------->
    new_user_Label_frm_4=LabelFrame(new_user_frm,text="Username Password",font=("dubai","14","bold"),fg="black",bg="white")
    new_user_Label_frm_4.place(x=90,y=580,width=470,height=130)

    def on_enter_up1(e):
        name=new_user_username.get()
        if name=='None':
            new_user_username.delete(0,"end")
        else:
            pass

    def on_leave_up1(e):
        name=new_user_username.get()
        if name=='':
            new_user_username.insert(0,"None")

    new_user_Label3_2=Label(new_user_Label_frm_4,text="Prefferred UserName :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label3_2.place(x=20,y=5)
    new_user_username=Entry(new_user_Label_frm_4,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_username.place(x=190,y=10)
    new_user_username.insert(0,"None")
    new_user_username.bind("<FocusIn>",on_enter_up1)
    new_user_username.bind("<FocusOut>",on_leave_up1)
    Frame(new_user_Label_frm_4,width=165,height=2,bg="black").place(x=190,y=32)#That line under the entry

    def on_enter_up2(e):
        name=new_user_password.get()
        if name=='None':
            new_user_password.delete(0,"end")
        else:
            pass

    def on_leave_up2(e):
        name=new_user_password.get()
        if name=='':
            new_user_password.insert(0,"None")
    

    new_user_Label3_3=Label(new_user_Label_frm_4,text="Preferred Password  :",font=("dubai","12"),fg="black",bg="white")
    new_user_Label3_3.place(x=20,y=45)
    new_user_password=Entry(new_user_Label_frm_4,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    new_user_password.place(x=190,y=50)
    new_user_password.insert(0,"None")
    new_user_password.bind("<FocusIn>",on_enter_up2)
    new_user_password.bind("<FocusOut>",on_leave_up2)
    Frame(new_user_Label_frm_4,width=165,height=2,bg="black").place(x=190,y=72)#That line under the entry

    def new_username_check():
        
        global username_check_button
        username_check_button=False

        #New user name password minimum requirements Errors
        def errorcode_3():
            
            if (len(new_user_username.get())==0 or new_user_username.get()=="None") and (len(new_user_password.get())==0 or new_user_password.get()=="None"):
                #Null input
                messagebox.showerror('ERROR','Input Required')

            elif (len(new_user_username.get())<4 or len(new_user_username.get())>15) and (len(new_user_password.get())==0 or new_user_password.get()=="None"):
                #wrong username and Null password -----> 2
                messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters\n Password required')

            elif (len(new_user_username.get())<4 or len(new_user_username.get())>15) and len(new_user_password.get())<8:
                #wrong username and password less 8 charecters -----> 3
                messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters')
                messagebox.showerror('ERROR','Password should be more than 8 charecters')

            elif (len(new_user_username.get())<4 or len(new_user_username.get())>15) and len(new_user_password.get())>8:
                #wrong username and password more than 8 charecters -----> 4
                messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters')

            elif len(new_user_password.get())<8:
                #correct username and password less 8 charecters -----> 5
                messagebox.showerror('ERROR','Password should be more than 8 charecters')

            elif new_user_username.get()=="None":
                #Null Username and password more than 8 charecters -----> 6
                messagebox.showerror('ERROR','Username Required')
                
            else:
                #correct username and password more than 8 charecters but doest fullfill the conditions -----> 7
                messagebox.showerror('ERROR','Your input has ERROR\nPassword must contain:----->\nAtleast 1 Capital Letter, 1 Small Letter\n1 Spcl Charecter, 1 Number ')



        #Assigning global to every identifier so that these can be used outside the function
        global new_username_password_eligibility_check

        #checking the new_user_name and new_password meets the minimum requirements for creating username and password---------------------->
        a1=new_user_username.get()
        b1=new_user_password.get()
        new_username_password_eligibility_check=l1.crt_1(a1,b1)

        if new_username_password_eligibility_check==True:

            #Checking the availability of the new username in database---------------------->
            cursor.execute("use user_account")
            cursor.execute("Select User_Name from Personal_details")
            user_name_fetch=new_user_username.get()
            user_count=0
            for usernames in cursor:
                #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                for x in usernames:
                    if user_name_fetch==x:
                        user_count=user_count+1  
                    else:
                        pass

            #Checking the availability of the new username in Request database---------------------->
            cursor.execute("use new_user_account")
            cursor.execute("Select New_User_Name from New_User_Details")
            user_name_fetch_1=new_user_username.get()
            new_user_count=0
            for usernames_1 in cursor:
                #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                for x_1 in usernames_1:
                    if user_name_fetch_1==x_1:
                        new_user_count=new_user_count+1  
                    else:
                        pass

            if user_count==0 and new_user_count==0:
                messagebox.showinfo('Message','Username Available And Password Meets the Requirements')

                #Confirming the check button of newuser pass section is clicked and checked                    
                username_check_button=True
                
            elif user_count!=0 or new_user_count!=0:
                username_check_button=False
                messagebox.showerror('ERROR','UserName already Taken\nChange a new UserName')
                
            else:
                pass
        else:
            username_check_button=False
            errorcode_3()

    #Checking the Availability for the UserName in the database ---------->
    new_Username_check_button=Button(new_user_Label_frm_4,text="Check",font=("nirmala ui","8","bold"),bg="black",relief="ridge",bd=0,command=new_username_check)
    new_Username_check_button.place(x=390,y=60)
    
    #New User Frame to User Frame 1
    new_User_Back=Button(new_user_frm,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_2)
    new_User_Back.place(x=15,y=15)

    #New User Details Request Button
    new_user_submit=Button(new_user_frm,text="Request",bg="black",relief="ridge",bd=0,font=("castellar","13","bold"),command=new_user_request)
    new_user_submit.place(x=1150,y=655)





def User_Page_1():

    #Assigning global to every identifier so that these can be used outside the function
    global user_frm1
    global User_Back_1
    global User_Name
    global Password_1
    global new_user_button
    global User_login_button

    #Creating A New Frame For User to Login...

    def back_1():
        user_frm1.destroy()

    #Username's and Password's entry Error's messageboxes -----> 1
    def errorcode_1():
        if (len(User_Name.get())==0 or User_Name.get()=="UserName") and (len(Password_1.get())==0 or Password_1.get()=="Password"):
            #Null input
            messagebox.showerror('ERROR','Input Required')

        elif (len(User_Name.get())<4 or len(User_Name.get())>15) and (len(Password_1.get())==0 or Password_1.get()=="Password"):
            #wrong username and Null password -----> 2
            messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters\n Password required')

        elif (len(User_Name.get())<4 or len(User_Name.get())>15) and len(Password_1.get())<8:
            #wrong username and password less 8 charecters -----> 3
            messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters')
            messagebox.showerror('ERROR','Password should be more than 8 charecters')

        elif (len(User_Name.get())<4 or len(User_Name.get())>15) and len(Password_1.get())>8:
            #wrong username and password more than 8 charecters -----> 4
            messagebox.showerror('ERROR','Your input has ERROR\n Give Username between 4 to 15 charecters')

        elif len(Password_1.get())<8:
            #correct username and password less 8 charecters -----> 5
            messagebox.showerror('ERROR','Password should be more than 8 charecters')

        elif User_Name.get()=="UserName":
            #Null Username and password more than 8 charecters -----> 6
            messagebox.showerror('ERROR','Username Required')

        elif Password_1.get()=="Password":
            #Username Meets the requirement But Null Password -----> 7
            messagebox.showerror('ERROR','Password Required')
            
        else:
            #correct username and password more than 8 charecters but doest fullfill the conditions -----> 8
            messagebox.showerror('ERROR','Your input has ERROR\nPassword must contain:----->\nAtleast 1 Capital Letter, 1 Small Letter\n1 Spcl Charecter, 1 Number ')

    #Username's and Password's entry check
    def login_1():
        global user_frm_2
        global user_frm_2_Button_1
        global user_frm_2_Button_2
        global user_count_1
        global user_name_fetch

        a=User_Name.get()
        b=Password_1.get()
        user_pass_check=l1.crt_1(a,b)

        #User's Page View Balence
        def user_Balence():    
            user_name_fetch_1=f"'{user_name_fetch}'"
            View_User_Balence=f"select Bank_Balence from Account_Details where User_Name={user_name_fetch_1}"
            cursor.execute("use user_account")
            cursor.execute(View_User_Balence)
            for Bal in cursor:
                for Balence in Bal:
                    messagebox.showinfo('MESSAGE',f'Balence : Rs.{Balence}')

        def User_Transaction():

            #Withdrawal Page------------------------>
            def User_Withdrawal():
                def back_9():
                    user_frm_4.destroy()

                user_frm_4=Frame(user_frm_3,width=1509,height=942,bg="white")
                user_frm_4.place(x=0,y=0)

                User_Withdrawal_Label_frm=LabelFrame(user_frm_4,text="Withdrawal",font=("dubai","14","bold"),fg="black",bg="white")
                User_Withdrawal_Label_frm.place(x=90,y=70,width=450,height=130)

                user_frm_4_label_1=Label(User_Withdrawal_Label_frm,text="How Much Money Needs\n             To Be Withdrawn",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_4_label_1.place(x=15,y=39)

                user_frm_4_label_2=Label(User_Withdrawal_Label_frm,text=":",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_4_label_2.place(x=208,y=46)

                def on_enter_User_Withdraw(e):
                    name=User_Withdraw_Entry.get()
                    if name=="None":
                        User_Withdraw_Entry.delete(0,"end")

                def on_leave_User_Withdraw(e):
                    name=User_Withdraw_Entry.get()
                    if name=='':
                        User_Withdraw_Entry.insert(0,"Admin UserName")
             
                User_Withdraw_Entry=Entry(User_Withdrawal_Label_frm,width=11,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                User_Withdraw_Entry.place(x=223,y=45)
                User_Withdraw_Entry.insert(0,"None")
                User_Withdraw_Entry.bind("<FocusIn>",on_enter_User_Withdraw)
                User_Withdraw_Entry.bind("<FocusOut>",on_leave_User_Withdraw)
                
                Frame(User_Withdrawal_Label_frm,width=80,height=2,bg="black").place(x=223,y=67)#That line under the entry

                def User_Withdrawl_Code_Generation():

                    user_name_fetch_1=f"'{user_name_fetch}'"
                    View_User_Balence=f"select Bank_Balence from Account_Details where User_Name={user_name_fetch_1}"
                    cursor.execute("use user_account")
                    cursor.execute(View_User_Balence)
                    for Bal in cursor:
                        for Balence in Bal:
                            User_Balence_1=float(Balence)
                            
                    if User_Withdraw_Entry.get()!="None" and User_Withdraw_Entry.get()!="":
                        if User_Withdraw_Entry.get().isdigit():
                            User_Withdraw_Entry_1=float(User_Withdraw_Entry.get())
                            if User_Balence_1>=User_Withdraw_Entry_1:

                                def Code_Generation_1():

                                    global Random_Key_To_Withdrawal
                                    
                                    Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                    Lower="abcdefghijklmnopqrstuvwxyz"
                                    Numbers="0123456789"
                                    Symbols="!@#$%&*"

                                    string_1= Upper + Lower + Numbers + Symbols
                                    length_1=18

                                    Random_Key_To_Withdrawal="".join(sample(string_1,length_1))

                                Code_Generation_1()

                                #Checking For Duplicates Codes In The Database To Avoid Multiple Persons Having Same Codes
                                cursor.execute("use user_account")
                                cursor.execute("select Codes from Withdrawal_Codes")
                                Code_Duplicate_Count=0
                                for Codess in cursor:
                                    for Code in Codess:
                                        if Code==Random_Key_To_Withdrawal:
                                            Code_Duplicate_Count=Code_Duplicate_Count+1
                                        else:
                                            pass
                                        
                                if Code_Duplicate_Count==0:

                                    Final_Withdrawl_code=f"'{Random_Key_To_Withdrawal}'"
                                    Code_Add_To_Data_Base=f"Insert into Withdrawal_Codes VALUES ({Final_Withdrawl_code})"

                                    cursor.execute("use user_account")
                                    cursor.execute(Code_Add_To_Data_Base)
                                    my_DB.commit()

                                    messagebox.showinfo('MESSAGE','Important...!')
                                    messagebox.showinfo('MESSAGE','You Will Get A 18 Digit Withdrawl Code\nEnter It In Either an ATM\nOR Give IT In The Bank And Withdraw Your Money')
                                    messagebox.showinfo('MESSAGE',"Don't Cut Next Message Sooner...!")
                                    messagebox.showinfo('MESSAGE',f'{Random_Key_To_Withdrawal}')
                                    messagebox.showinfo('MESSAGE',f"{Random_Key_To_Withdrawal}\nIt Won't Be Shown Again Be Carefull And Note Down Carefully")
                                    user_frm_4.destroy()
                                    user_frm_3.destroy()
                                    
                                else:
                                    Code_Generation_1()
                                
                            else:
                                messagebox.showerror('ERROR','Insufficient Balence...!')

                        else:
                            messagebox.showerror('ERROR','Give Only Numbers...!')

                    else:
                        messagebox.showerror('ERROR','Input Required...!')
                    

                #Withdraw Submit Button
                User_Withdrawal_Submit=Button(User_Withdrawal_Label_frm,text="Submit",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Withdrawl_Code_Generation)
                User_Withdrawal_Submit.place(x=350,y=50)

                #Back Button Withdrawal Page to Transaction Page ---------->
                User_Back_4=Button(user_frm_4,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_9)
                User_Back_4.place(x=15,y=15)
                

            #Fund Transfer Page--------------------------->
            def user_Fund_Transfer():

                global user_frm_5
                global User_Fund_Transfer_Label_frm
                global user_frm_5_entry_1
                global user_frm_5_entry_2
                global user_frm_5_entry_3
                global user_frm_5_entry_4
                global View_Reciever_Balence
                global Final_Reciever_Balence
                global Acc_Num_Exixtance_Check
                global Acc_Holder_Name_Exixtance_Check
                global Update_Reciever_Balence
                global Update_Sender_Balence
                global Transfer_Fund_Bal
                global Reciever_User_Name
                
                def back_10():
                    user_frm_5.destroy()

                def User_Fund_Transfer_Check_Credintials():
                    
                    if user_frm_5_entry_1.get()!='' and user_frm_5_entry_1.get()!='None' and user_frm_5_entry_2.get()!='' and user_frm_5_entry_2.get()!='None' and user_frm_5_entry_3.get()!='' and user_frm_5_entry_3.get()!='None' and user_frm_5_entry_4.get()!='' and user_frm_5_entry_4.get()!='None':

                        if user_frm_5_entry_1.get().isdigit() and user_frm_5_entry_2.get().isdigit():

                            if user_frm_5_entry_1.get()==user_frm_5_entry_2.get():

                                cursor.execute("use user_account")
                                cursor.execute("select Account_Number from Account_Details")
                                Acc_Num_Exixtance_Check=0
                                for Acc_Nums in cursor:
                                    for Account_Number_1 in Acc_Nums:
                                        if Account_Number_1==user_frm_5_entry_1.get():
                                            Acc_Num_Exixtance_Check=Acc_Num_Exixtance_Check+1
                                        else:
                                            pass

                                if Acc_Num_Exixtance_Check==1:

                                    Acc_Num_1=user_frm_5_entry_1.get()
                                    Acc_Num_2=f"'{Acc_Num_1}'"
                                    Fund_Transfer_Acc_Name_Check=f"select Account_Holder_Name from Account_Details where Account_Number={Acc_Num_2}"
                                    cursor.execute("use user_account")
                                    cursor.execute(Fund_Transfer_Acc_Name_Check)
                                    Acc_Holder_Name_Exixtance_Check=0
                                    for Acc_Names in cursor:
                                        for Acc_Names_1 in Acc_Names:
                                            if Acc_Names_1==user_frm_5_entry_3.get():
                                                Acc_Holder_Name_Exixtance_Check=Acc_Holder_Name_Exixtance_Check+1
                                            else:
                                                pass

                                    if Acc_Holder_Name_Exixtance_Check==1:
                                        
                                        user_name_fetch_1=f"'{user_name_fetch}'"
                                        View_User_Balence=f"select Bank_Balence from Account_Details where User_Name={user_name_fetch_1}"
                                        cursor.execute("use user_account")
                                        cursor.execute(View_User_Balence)
                                        for Bal in cursor:
                                            for Balence in Bal:
                                                Transfer_Fund_Bal=float(Balence)

                                        #Finding The UserName For The Given Account Number
                                        X0A0=user_frm_5_entry_1.get()
                                        Reciever_UserName=f"select User_Name from Account_Details where Account_Number = '{X0A0}'"
                                        cursor.execute("use user_account")
                                        cursor.execute(Reciever_UserName)
                                        for User__1 in cursor:
                                            for UserNames_1 in User__1:
                                                Reciever_User_Name=str(UserNames_1)

                                        X1A1=user_frm_5_entry_1.get()
                                        user_Reciever_fetch_1=f"'{X1A1}'"
                                        View_Reciever_Balence=f"select Bank_Balence from Account_Details where Account_Number = {user_Reciever_fetch_1}"
                                        cursor.execute("use user_account")
                                        cursor.execute(View_Reciever_Balence)
                                        for Bal__1 in cursor:
                                            for Reciever_Balence in Bal__1:
                                                global Reciever_Initial_Bal
                                                Reciever_Initial_Bal=float(Reciever_Balence)
                                                
                                        if user_frm_5_entry_4.get().isdigit():
                                            
                                            if Transfer_Fund_Bal>=float(user_frm_5_entry_4.get()):

                                                Money_Transfer_Confirmation=messagebox.askquestion("Confirm...?",f"Do You Want To Transfer Rs.{user_frm_5_entry_4.get()}\nTo {user_frm_5_entry_3.get()}")
                                                if Money_Transfer_Confirmation == 'yes':
                                                
                                                    X2A2=float(user_frm_5_entry_4.get())
                                                    Final_Sender_Balence=Transfer_Fund_Bal-X2A2

                                                    Update_Sender_Balence=f"UPDATE `user_account`.`Account_Details` SET `Bank_Balence` = '{Final_Sender_Balence}' WHERE (`User_Name` = {user_name_fetch_1});"
                                                    cursor.execute("use user_account")
                                                    cursor.execute(Update_Sender_Balence)
                                                    my_DB.commit()

                                                    Final_Reciever_Balence=Reciever_Initial_Bal+X2A2                                                        
                                                    Update_Reciever_Balence=f"UPDATE `user_account`.`Account_Details` SET `Bank_Balence` = '{Final_Reciever_Balence}' WHERE (`User_Name` = '{Reciever_User_Name}');"
                                                    cursor.execute("use user_account")
                                                    cursor.execute(Update_Reciever_Balence)
                                                    my_DB.commit()

                                                    messagebox.showinfo('MESSAGE','Transaction Sucessfull')
                                                    messagebox.showinfo('MESSAGE',f" Your Current Balence : '{Final_Sender_Balence}'")
                                                    user_frm_5.destroy()
                                                    user_frm_3.destroy()
                                                    
                                                else:
                                                    pass
                                            
                                            else:
                                                messagebox.showerror('ERROR','Insufficient Balence...!')
                                                
                                        else:
                                            messagebox.showerror('ERROR','Enter The Money To Be Transfered In Numbers')
                                            
                                    else:
                                        messagebox.showerror('ERROR',"Incorrect Account Holder's Name")
                                                
                                else:
                                    messagebox.showerror('ERROR','Incorrect Account Number')

                            else:
                                messagebox.showerror('ERROR','Both Account Numbers Must Be Same')                         

                        else:
                            messagebox.showerror('ERROR','Account Numbers Must Only Be In Numbers')

                    else:
                        messagebox.showerror('ERROR','Input Required...!\nFill Everything')

                user_frm_5=Frame(user_frm_3,width=1509,height=942,bg="white")
                user_frm_5.place(x=0,y=0)

                User_Fund_Transfer_Label_frm=LabelFrame(user_frm_5,text="Fund Transfer",font=("dubai","14","bold"),fg="black",bg="white")
                User_Fund_Transfer_Label_frm.place(x=90,y=70,width=450,height=280)

                def on_enter_Fund_T_1(e):
                    name=user_frm_5_entry_1.get()
                    if name=='None':
                        user_frm_5_entry_1.delete(0,"end")
                    else:
                        pass

                def on_leave_Fund_T_1(e):
                    name=user_frm_5_entry_1.get()
                    if name=='':
                        user_frm_5_entry_1.insert(0,"None")
                
                user_frm_5_label_1=Label(User_Fund_Transfer_Label_frm,text="Account Number                 :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_5_label_1.place(x=20,y=39)
                user_frm_5_entry_1=Entry(User_Fund_Transfer_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                user_frm_5_entry_1.place(x=240,y=44)
                user_frm_5_entry_1.insert(0,"None")
                user_frm_5_entry_1.bind("<FocusIn>",on_enter_Fund_T_1)
                user_frm_5_entry_1.bind("<FocusOut>",on_leave_Fund_T_1)
                Frame(User_Fund_Transfer_Label_frm,width=165,height=2,bg="black").place(x=240,y=66)#That line under the entry

                def on_enter_Fund_T_2(e):
                    name=user_frm_5_entry_2.get()
                    if name=='None':
                        user_frm_5_entry_2.delete(0,"end")
                    else:
                        pass

                def on_leave_Fund_T_2(e):
                    name=user_frm_5_entry_2.get()
                    if name=='':
                        user_frm_5_entry_2.insert(0,"None")

                
                user_frm_5_label_2=Label(User_Fund_Transfer_Label_frm,text="Confirm Account Number  :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_5_label_2.place(x=18,y=79)
                user_frm_5_entry_2=Entry(User_Fund_Transfer_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                user_frm_5_entry_2.place(x=240,y=84)
                user_frm_5_entry_2.insert(0,"None")
                user_frm_5_entry_2.bind("<FocusIn>",on_enter_Fund_T_2)
                user_frm_5_entry_2.bind("<FocusOut>",on_leave_Fund_T_2)
                Frame(User_Fund_Transfer_Label_frm,width=165,height=2,bg="black").place(x=240,y=106)#That line under the entry

                def on_enter_Fund_T_3(e):
                    name=user_frm_5_entry_3.get()
                    if name=='None':
                        user_frm_5_entry_3.delete(0,"end")
                    else:
                        pass

                def on_leave_Fund_T_3(e):
                    name=user_frm_5_entry_3.get()
                    if name=='':
                        user_frm_5_entry_3.insert(0,"None")

                user_frm_5_label_3=Label(User_Fund_Transfer_Label_frm,text="Account Holder Name        :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_5_label_3.place(x=20,y=119)
                user_frm_5_entry_3=Entry(User_Fund_Transfer_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                user_frm_5_entry_3.place(x=240,y=124)
                user_frm_5_entry_3.insert(0,"None")
                user_frm_5_entry_3.bind("<FocusIn>",on_enter_Fund_T_3)
                user_frm_5_entry_3.bind("<FocusOut>",on_leave_Fund_T_3)
                Frame(User_Fund_Transfer_Label_frm,width=165,height=2,bg="black").place(x=240,y=146)#That line under the entry
    
                def on_enter_Fund_T_4(e):
                    name=user_frm_5_entry_4.get()
                    if name=='None':
                        user_frm_5_entry_4.delete(0,"end")
                    else:
                        pass

                def on_leave_Fund_T_4(e):
                    name=user_frm_5_entry_4.get()
                    if name=='':
                        user_frm_5_entry_4.insert(0,"None")

                user_frm_5_label_4=Label(User_Fund_Transfer_Label_frm,text="Amount To Be Transfered :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                user_frm_5_label_4.place(x=20,y=159)
                user_frm_5_entry_4=Entry(User_Fund_Transfer_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                user_frm_5_entry_4.place(x=240,y=164)
                user_frm_5_entry_4.insert(0,"None")
                user_frm_5_entry_4.bind("<FocusIn>",on_enter_Fund_T_4)
                user_frm_5_entry_4.bind("<FocusOut>",on_leave_Fund_T_4)
                Frame(User_Fund_Transfer_Label_frm,width=165,height=2,bg="black").place(x=240,y=186)#That line under the entry

                #Back Button Fund Transfer Page To Transaction Page---------->
                User_Back_5=Button(user_frm_5,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_10)
                User_Back_5.place(x=15,y=15)

                #Fund Transfer Submit Button
                User_Fund_Transfer_Submit=Button(User_Fund_Transfer_Label_frm,text="Submit",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Fund_Transfer_Check_Credintials)
                User_Fund_Transfer_Submit.place(x=350,y=210)

            
            #User Frame 3------------------------------->

            def back_8():
                user_frm_3.destroy()

            user_frm_3=Frame(user_frm_2,width=1509,height=942,bg="white")
            user_frm_3.place(x=0,y=0)

            user_frm_3_label_1=Label(user_frm_3,text="What's Your Need",font=("dubai","40","bold"),fg="BLACK",bg="white")
            user_frm_3_label_1.place(x=440,y=200)
            
            user_frm_3_Button_2=Button(user_frm_3,width=28,text="Withdrawal",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=User_Withdrawal)
            user_frm_3_Button_2.place(x=520,y=330)

            user_frm_3_Button_3=Button(user_frm_3,width=28,text="Fund Transfer",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=user_Fund_Transfer)
            user_frm_3_Button_3.place(x=520,y=390)

            user_frm_3_label_2=Label(user_frm_3,text="For Deposits to Your Own Account\n You Have To Reach The Bank In Person",font=("dubai","20","bold"),fg="BLACK",bg="white")
            user_frm_3_label_2.place(x=440,y=660)          

            #Back Button Transaction Page to User Page 2 ---------->
            User_Back_3=Button(user_frm_3,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_8)
            User_Back_3.place(x=15,y=15)


        #User Frame 4------------------------------>
        def Account_Details_Changes():

            cursor.execute("use user_account")
            cursor.execute("Select User_Name from User_Changes")
            Previous_details_changes_request_count=0

            for usernames_in_Request in cursor:
                for usernames_in_Request_1 in usernames_in_Request:
                    if usernames_in_Request_1==User_Name.get():
                        Previous_details_changes_request_count=Previous_details_changes_request_count+1
                    else:
                        pass

            if Previous_details_changes_request_count==0:
            
                def back_11():
                    user_frm_6.destroy()

                user_frm_6=Frame(user_frm_2,width=1509,height=942,bg="white")
                user_frm_6.place(x=0,y=0)

                User_Details_Changes_Label_frm=LabelFrame(user_frm_6,text="Account Details Changes",font=("dubai","14","bold"),fg="black",bg="white")
                User_Details_Changes_Label_frm.place(x=90,y=70,width=520,height=170)

                def Account_Changes_Entry():

                    Changes_selection_Check_count=0
                    Changes_selection_Check_count_1=0

                    if USER_Changes_COMBOBOX.get()=="--Select--":
                        Changes_selection_Check_count_1=Changes_selection_Check_count_1+1
                    elif USER_Changes_COMBOBOX.get() not in Changes_List_Options:
                        Changes_selection_Check_count=Changes_selection_Check_count+1
                    else:
                        pass
                    
                    if Changes_selection_Check_count==0:
                        
                        if Changes_selection_Check_count_1==0:
                            
                            #Back Button New User Details Page to New Request Page
                            def back_12():
                                user_frm_7.destroy()
                                USER_Changes_COMBOBOX.current(0)
                            
                            user_frm_7=Frame(user_frm_6,width=1509,height=942,bg="white")
                            user_frm_7.place(x=0,y=0)

                            def User_Single_Detail_change_Submit():

                                if User_Single_change_Entry.get()!="None" and User_Single_change_Entry.get()!="":
                                
                                    if USER_Changes_COMBOBOX.get()=="User Name":
                                        
                                        cursor.execute("use user_account")
                                        cursor.execute("Select User_Name from Personal_Details")
                                        Changeing_user_name_fetch=User_Single_change_Entry.get()
                                        Existing_user_count_1=0
                                        for existingusernames in cursor:
                                            #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                                            for xA1 in existingusernames:
                                                if Changeing_user_name_fetch==xA1:
                                                    Existing_user_count_1=Existing_user_count_1+1  
                                                else:
                                                    pass
                                        if Existing_user_count_1==0:
                                            
                                            if len(User_Single_change_Entry.get())>=4 and len(User_Single_change_Entry.get())<=15:
                                                
                                                Single_Detail_Change_Confirm=messagebox.askquestion("Confirm...?","Do You Want To Raise Request ?")
                                                if Single_Detail_Change_Confirm == 'yes':
                                                
                                                    cursor.execute("use user_account")
                                                    USERNAME_CHANGES_INSERT=f"INSERT INTO User_Changes Values('{User_Name.get()}','User Name','{User_Single_change_Entry.get()}')"
                                                    cursor.execute(USERNAME_CHANGES_INSERT)
                                                    my_DB.commit()

                                                    messagebox.showinfo('MESSAGE','Request Raised Sucessfully')
                                                    messagebox.showinfo('NOTE...','Only One Request Can Be Made At an Instanse\nOnce the changes is Updated You Can Raise Another')
                                                    user_frm_7.destroy()
                                                    user_frm_6.destroy()

                                                else:
                                                    pass
                                                
                                        else:
                                            messagebox.showerror('ERROR','UserName Already Taken\nTry Something else ...')

                                    elif USER_Changes_COMBOBOX.get()=="Mobile Number":

                                        if User_Single_change_Entry.get().isdigit():

                                            if len(User_Single_change_Entry.get())==10:

                                                Single_Detail_Change_Confirm_1=messagebox.askquestion("Confirm...?","Do You Want To Raise Request ?")
                                                if Single_Detail_Change_Confirm_1 == 'yes':

                                                    cursor.execute("use user_account")
                                                    USERNAME_CHANGES_INSERT_1=f"INSERT INTO User_Changes Values('{User_Name.get()}','Mobile Number','{User_Single_change_Entry.get()}')"
                                                    cursor.execute(USERNAME_CHANGES_INSERT_1)
                                                    my_DB.commit()

                                                    messagebox.showinfo('MESSAGE','Request Raised Sucessfully')
                                                    messagebox.showinfo('NOTE...','Only One Request Can Be Made At an Instanse\nOnce the changes is Updated You Can Raise Another')
                                                    user_frm_7.destroy()
                                                    user_frm_6.destroy()

                                                else:
                                                    pass
                                                
                                            else:
                                                messagebox.showerror('ERROR','Mobile Number Should Only Be In 10 Digits')

                                        else:
                                            messagebox.showerror('ERROR','Mobile Number Should Only Be In Numbers')

                                    elif USER_Changes_COMBOBOX.get()=="Email Id":

                                        Single_Detail_Change_Confirm_2=messagebox.askquestion("Confirm...?","Do You Want To Raise Request ?")
                                        if Single_Detail_Change_Confirm_2 == 'yes':

                                            cursor.execute("use user_account")
                                            USERNAME_CHANGES_INSERT_1=f"INSERT INTO User_Changes Values('{User_Name.get()}','Email Id','{User_Single_change_Entry.get()}')"
                                            cursor.execute(USERNAME_CHANGES_INSERT_1)
                                            my_DB.commit()

                                            messagebox.showinfo('MESSAGE','Request Raised Sucessfully')
                                            messagebox.showinfo('NOTE...','Only One Request Can Be Made At an Instanse\nOnce the changes is Updated You Can Raise Another')
                                            user_frm_7.destroy()
                                            user_frm_6.destroy()

                                        else:
                                            pass
                                        
                                    else:
                                        messagebox.showerror('ERROR',"Go Back And Start The Process Again\nDon't Type Anything Without Clicking The Entries")

                                else:
                                    messagebox.showerror('ERROR','Input Required')
                                    

                            def User_Password_change_Submit():

                                if USER_Changes_COMBOBOX.get()=="Password":
                                
                                    User_Password_Changes_Eligibility_Check=0
                                                                        
                                    if User_Password_change_Entry_1.get()==Password_1.get():

                                        if User_Password_change_Entry_2.get()==User_Password_change_Entry_3.get():

                                            if len(User_Password_change_Entry_2.get())>=8:
                                                User_Password_Changes_Eligibility_Check=User_Password_Changes_Eligibility_Check+1
                                            else:
                                                pass

                                            spcl_1=[".",",","!","@","#","$","%","^","&","*","(",")","-","=","_","+","?","<",">","/","{","[","]","}","|",";",":"]

                                            User_Password_Changes_Entry_Fetch=str(User_Password_change_Entry_2.get())

                                            for single_Letter_1 in User_Password_Changes_Entry_Fetch:
                                                if single_Letter_1.isupper():
                                                    User_Password_Changes_Eligibility_Check=User_Password_Changes_Eligibility_Check+1
                                                    break

                                            for single_Letter_2 in User_Password_Changes_Entry_Fetch:
                                                if single_Letter_2.islower():
                                                    User_Password_Changes_Eligibility_Check=User_Password_Changes_Eligibility_Check+1
                                                    break

                                            for single_Letter_3 in User_Password_Changes_Entry_Fetch:
                                                if single_Letter_3 in spcl_1:
                                                    User_Password_Changes_Eligibility_Check=User_Password_Changes_Eligibility_Check+1
                                                    break

                                            for single_Letter_4 in User_Password_Changes_Entry_Fetch:
                                                if single_Letter_4.isdigit():
                                                    User_Password_Changes_Eligibility_Check=User_Password_Changes_Eligibility_Check+1
                                                    break

                                            if User_Password_Changes_Eligibility_Check==5:

                                                Single_Detail_Change_Confirm_3=messagebox.askquestion("Confirm...?","Do You Want To Raise Request ?")
                                                if Single_Detail_Change_Confirm_3 == 'yes':

                                                    cursor.execute("use user_account")
                                                    USERNAME_CHANGES_INSERT_2=f"INSERT INTO User_Changes Values('{User_Name.get()}','Password','{User_Password_change_Entry_2.get()}')"
                                                    cursor.execute(USERNAME_CHANGES_INSERT_2)
                                                    my_DB.commit()

                                                    messagebox.showinfo('MESSAGE','Request Raised Sucessfully')
                                                    messagebox.showinfo('NOTE...','Only One Request Can Be Made At an Instanse\nOnce the changes is Updated You Can Raise Another')
                                                    user_frm_7.destroy()
                                                    user_frm_6.destroy()

                                                else:
                                                    pass

                                            else:

                                                if len(User_Password_change_Entry_2.get())<8:
                                                    
                                                    messagebox.showerror('ERROR','Minimum Length Of a Password is 8 Charecters')

                                                else:

                                                    messagebox.showerror('ERROR','Your input has ERROR\nPassword must contain:----->\nAtleast 1 Capital Letter, 1 Small Letter\n1 Spcl Charecter, 1 Number ')
                                                    
                                        else:
                                            messagebox.showerror('ERROR',"New Passwords Doesn't Match\nBoth New Password entry and Confirm Password Entry Must Be Same")

                                    else:
                                        messagebox.showerror('ERROR','Incorrect Current Password')

                                else:
                                    messagebox.showerror('ERROR',"Go Back And Start The Process Again\nDon't Type Anything Without Clicking The Entries")

                            def User_Adderss_change_Submit():

                                if USER_Changes_COMBOBOX.get()=="Parmanent Address" or USER_Changes_COMBOBOX.get()=="Current Address":

                                    if User_Address_Change_Entry_1.get()!="None" and User_Address_Change_Entry_2.get()!="None" and User_Address_Change_Entry_3.get()!="None" and User_Address_Change_Entry_4.get()!="None" and User_Address_Change_Entry_5.get()!="None" and User_Address_Change_Entry_6.get()!="None":

                                        if User_Address_Change_Entry_1.get()!="" and User_Address_Change_Entry_2.get()!="" and User_Address_Change_Entry_3.get()!="" and User_Address_Change_Entry_4.get()!="" and User_Address_Change_Entry_5.get()!="" and User_Address_Change_Entry_6.get()!="":

                                            if User_Address_Change_Entry_6.get().isdigit():

                                                if len(User_Address_Change_Entry_6.get())==6:

                                                    Single_Detail_Change_Confirm_4=messagebox.askquestion("Confirm...?","Do You Want To Raise Request ?")
                                                    if Single_Detail_Change_Confirm_4 == 'yes':

                                                        cursor.execute("use user_account")
                                                        USERNAME_CHANGES_INSERT_3=f"INSERT INTO User_Changes Values('{User_Name.get()}','{USER_Changes_COMBOBOX.get()}','{User_Address_Change_Entry_3.get()},\n{User_Address_Change_Entry_4.get()},\n{User_Address_Change_Entry_1.get()},{User_Address_Change_Entry_5.get()},\n{User_Address_Change_Entry_6.get()}')"
                                                        cursor.execute(USERNAME_CHANGES_INSERT_3)
                                                        my_DB.commit()

                                                        messagebox.showinfo('MESSAGE','Request Raised Sucessfully')
                                                        messagebox.showinfo('NOTE...','Only One Request Can Be Made At an Instanse\nOnce the changes is Updated You Can Raise Another')
                                                        user_frm_7.destroy()
                                                        user_frm_6.destroy()

                                                    else:
                                                        pass

                                                else:
                                                    messagebox.showerror('ERROR','Pincode Must Have Only 6 digits')

                                            else:
                                                messagebox.showerror('ERROR','Pincode Must Only Be In Numbers')

                                        else:
                                            messagebox.showerror('ERROR','Input Required')

                                    else:
                                        messagebox.showerror('ERROR','Input Required...!')

                                else:
                                    messagebox.showerror('ERROR',"Go Back And Start The Process Again\nDon't Type Anything Without Clicking The Entries")
                                    
                                
                            if USER_Changes_COMBOBOX.get()=="User Name" or USER_Changes_COMBOBOX.get()=="Mobile Number" or USER_Changes_COMBOBOX.get()=="Email Id":

                                User_Single_Parameter_Changes_Label_frm=LabelFrame(user_frm_7,text=f"{USER_Changes_COMBOBOX.get()} Changes",font=("dubai","14","bold"),fg="black",bg="white")
                                User_Single_Parameter_Changes_Label_frm.place(x=90,y=70,width=520,height=170)

                                User_Single_Parameter_Changes_Label_1=Label(User_Single_Parameter_Changes_Label_frm,text=f"{USER_Changes_COMBOBOX.get()}",font=("dubai","12","bold"),fg="BLACK",bg="white")
                                User_Single_Parameter_Changes_Label_1.place(x=15,y=39)

                                User_Single_Parameter_Changes_Label_2=Label(User_Single_Parameter_Changes_Label_frm,text=":",font=("dubai","12","bold"),fg="BLACK",bg="white")
                                User_Single_Parameter_Changes_Label_2.place(x=178,y=40)

                                def on_enter_User_Changes_1(e):
                                    name=User_Single_change_Entry.get()
                                    if name=="None":
                                        User_Single_change_Entry.delete(0,"end")

                                def on_leave_User_Changes_1(e):
                                    name=User_Single_change_Entry.get()
                                    if name=='':
                                        User_Single_change_Entry.insert(0,"Admin UserName")
                             
                                User_Single_change_Entry=Entry(User_Single_Parameter_Changes_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Single_change_Entry.place(x=203,y=45)
                                User_Single_change_Entry.insert(0,"None")
                                User_Single_change_Entry.bind("<FocusIn>",on_enter_User_Changes_1)
                                User_Single_change_Entry.bind("<FocusOut>",on_leave_User_Changes_1)
                                
                                Frame(User_Single_Parameter_Changes_Label_frm,width=163,height=2,bg="black").place(x=203,y=67)#That line under the entry

                                #Changes Submit Button
                                User_Single_Parameter_Change_Submit=Button(User_Single_Parameter_Changes_Label_frm,text="Submit",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Single_Detail_change_Submit)
                                User_Single_Parameter_Change_Submit.place(x=430,y=90)

                            elif USER_Changes_COMBOBOX.get()=="Password":

                                User_Password_Changes_Label_frm=LabelFrame(user_frm_7,text="Password Changes",font=("dubai","14","bold"),fg="black",bg="white")
                                User_Password_Changes_Label_frm.place(x=90,y=70,width=520,height=200)

                                def on_enter_User_Changes_2(e):
                                    name=User_Password_change_Entry_1.get()
                                    if name=="None":
                                        User_Password_change_Entry_1.delete(0,"end")

                                def on_leave_User_Changes_2(e):
                                    name=User_Password_change_Entry_1.get()
                                    if name=='':
                                        User_Password_change_Entry_1.insert(0,"Admin UserName")
                             
                                User_Password_Changes_Label_1=Label(User_Password_Changes_Label_frm,text="Current Password       :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                                User_Password_Changes_Label_1.place(x=15,y=39)
                                User_Password_change_Entry_1=Entry(User_Password_Changes_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Password_change_Entry_1.place(x=203,y=43)
                                User_Password_change_Entry_1.insert(0,"None")
                                User_Password_change_Entry_1.bind("<FocusIn>",on_enter_User_Changes_2)
                                User_Password_change_Entry_1.bind("<FocusOut>",on_leave_User_Changes_2)
                                
                                Frame(User_Password_Changes_Label_frm,width=163,height=2,bg="black").place(x=203,y=65)#That line under the entry

                                def on_enter_User_Changes_3(e):
                                    name=User_Password_change_Entry_2.get()
                                    if name=="None":
                                        User_Password_change_Entry_2.delete(0,"end")

                                def on_leave_User_Changes_3(e):
                                    name=User_Password_change_Entry_2.get()
                                    if name=='':
                                        User_Password_change_Entry_2.insert(0,"Admin UserName")
                             

                                User_Password_Changes_Label_2=Label(User_Password_Changes_Label_frm,text="New Password              :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                                User_Password_Changes_Label_2.place(x=15,y=79)
                                User_Password_change_Entry_2=Entry(User_Password_Changes_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Password_change_Entry_2.place(x=203,y=83)
                                User_Password_change_Entry_2.insert(0,"None")
                                User_Password_change_Entry_2.bind("<FocusIn>",on_enter_User_Changes_3)
                                User_Password_change_Entry_2.bind("<FocusOut>",on_leave_User_Changes_3)
                                
                                Frame(User_Password_Changes_Label_frm,width=163,height=2,bg="black").place(x=203,y=105)#That line under the entry


                                def on_enter_User_Changes_4(e):
                                    name=User_Password_change_Entry_3.get()
                                    if name=="None":
                                        User_Password_change_Entry_3.delete(0,"end")

                                def on_leave_User_Changes_4(e):
                                    name=User_Password_change_Entry_3.get()
                                    if name=='':
                                        User_Password_change_Entry_3.insert(0,"Admin UserName")
                             

                                User_Password_Changes_Label_3=Label(User_Password_Changes_Label_frm,text="Confirm Password       :",font=("dubai","12","bold"),fg="BLACK",bg="white")
                                User_Password_Changes_Label_3.place(x=15,y=119)
                                User_Password_change_Entry_3=Entry(User_Password_Changes_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Password_change_Entry_3.place(x=203,y=123)
                                User_Password_change_Entry_3.insert(0,"None")
                                User_Password_change_Entry_3.bind("<FocusIn>",on_enter_User_Changes_4)
                                User_Password_change_Entry_3.bind("<FocusOut>",on_leave_User_Changes_4)
                                
                                Frame(User_Password_Changes_Label_frm,width=163,height=2,bg="black").place(x=203,y=145)#That line under the entry


                                #Password Changes Submit Button
                                User_Single_Parameter_Change_Submit=Button(User_Password_Changes_Label_frm,text="Submit",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Password_change_Submit)
                                User_Single_Parameter_Change_Submit.place(x=440,y=130)

                            elif USER_Changes_COMBOBOX.get()=="Parmanent Address" or USER_Changes_COMBOBOX.get()=="Current Address":
                                
                                #Address Entry Frame--------------------------------------->
                                User_Adress_Change_Label_frm=LabelFrame(user_frm_7,text=f"{USER_Changes_COMBOBOX.get()}",font=("dubai","14","bold"),fg="black",bg="white")
                                User_Adress_Change_Label_frm.place(x=90,y=70,width=450,height=295)

                                def on_enter_User_Changes_5(e):
                                    name=User_Address_Change_Entry_1.get()
                                    if name=='None':
                                        User_Address_Change_Entry_1.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_5(e):
                                    name=User_Address_Change_Entry_1.get()
                                    if name=='':
                                        User_Address_Change_Entry_1.insert(0,"None")

                                User_Address_Change_Label_1=Label(User_Adress_Change_Label_frm,text="State                                        :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_1.place(x=20,y=30)
                                User_Address_Change_Entry_1=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_1.place(x=230,y=35)
                                User_Address_Change_Entry_1.insert(0,"None")
                                User_Address_Change_Entry_1.bind("<FocusIn>",on_enter_User_Changes_5)
                                User_Address_Change_Entry_1.bind("<FocusOut>",on_leave_User_Changes_5)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=57)#That line under the entry

                                def on_enter_User_Changes_6(e):
                                    name=User_Address_Change_Entry_2.get()
                                    if name=='None':
                                        User_Address_Change_Entry_2.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_6(e):
                                    name=User_Address_Change_Entry_2.get()
                                    if name=='':
                                        User_Address_Change_Entry_2.insert(0,"None")


                                User_Address_Change_Label_2=Label(User_Adress_Change_Label_frm,text="District                                     :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_2.place(x=20,y=60)
                                User_Address_Change_Entry_2=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_2.place(x=230,y=65)
                                User_Address_Change_Entry_2.insert(0,"None")
                                User_Address_Change_Entry_2.bind("<FocusIn>",on_enter_User_Changes_6)
                                User_Address_Change_Entry_2.bind("<FocusOut>",on_leave_User_Changes_6)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=87)#That line under the entry

                                def on_enter_User_Changes_7(e):
                                    name=User_Address_Change_Entry_3.get()
                                    if name=='None':
                                        User_Address_Change_Entry_3.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_7(e):
                                    name=User_Address_Change_Entry_3.get()
                                    if name=='':
                                        User_Address_Change_Entry_3.insert(0,"None")

                                
                                User_Address_Change_Label_3=Label(User_Adress_Change_Label_frm,text="Current Address Line 1         :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_3.place(x=20,y=90)
                                User_Address_Change_Entry_3=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_3.place(x=230,y=95)
                                User_Address_Change_Entry_3.insert(0,"None")
                                User_Address_Change_Entry_3.bind("<FocusIn>",on_enter_User_Changes_7)
                                User_Address_Change_Entry_3.bind("<FocusOut>",on_leave_User_Changes_7)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=117)#That line under the entry

                                def on_enter_User_Changes_8(e):
                                    name=User_Address_Change_Entry_4.get()
                                    if name=='None':
                                        User_Address_Change_Entry_4.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_8(e):
                                    name=User_Address_Change_Entry_4.get()
                                    if name=='':
                                        User_Address_Change_Entry_4.insert(0,"None")

                                User_Address_Change_Label_4=Label(User_Adress_Change_Label_frm,text="Current Address Line 2         :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_4.place(x=20,y=120)
                                User_Address_Change_Entry_4=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_4.place(x=230,y=125)
                                User_Address_Change_Entry_4.insert(0,"None")
                                User_Address_Change_Entry_4.bind("<FocusIn>",on_enter_User_Changes_8)
                                User_Address_Change_Entry_4.bind("<FocusOut>",on_leave_User_Changes_8)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=147)#That line under the entry

                                def on_enter_User_Changes_9(e):
                                    name=User_Address_Change_Entry_5.get()
                                    if name=='None':
                                        User_Address_Change_Entry_5.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_9(e):
                                    name=User_Address_Change_Entry_5.get()
                                    if name=='':
                                        User_Address_Change_Entry_5.insert(0,"None")
                                        
                                User_Address_Change_Label_5=Label(User_Adress_Change_Label_frm,text="Current Address Line 3         :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_5.place(x=20,y=150)
                                User_Address_Change_Entry_5=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_5.place(x=230,y=155)
                                User_Address_Change_Entry_5.insert(0,"None")
                                User_Address_Change_Entry_5.bind("<FocusIn>",on_enter_User_Changes_9)
                                User_Address_Change_Entry_5.bind("<FocusOut>",on_leave_User_Changes_9)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=177)#That line under the entry

                                def on_enter_User_Changes_10(e):
                                    name=User_Address_Change_Entry_6.get()
                                    if name=='None':
                                        User_Address_Change_Entry_6.delete(0,"end")
                                    else:
                                        pass

                                def on_leave_User_Changes_10(e):
                                    name=User_Address_Change_Entry_6.get()
                                    if name=='':
                                        User_Address_Change_Entry_6.insert(0,"None")

                                User_Address_Change_Label_6=Label(User_Adress_Change_Label_frm,text="Current Address Pincode      :",font=("dubai","12"),fg="black",bg="white")
                                User_Address_Change_Label_6.place(x=20,y=180)
                                User_Address_Change_Entry_6=Entry(User_Adress_Change_Label_frm,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                                User_Address_Change_Entry_6.place(x=230,y=185)
                                User_Address_Change_Entry_6.insert(0,"None")
                                User_Address_Change_Entry_6.bind("<FocusIn>",on_enter_User_Changes_10)
                                User_Address_Change_Entry_6.bind("<FocusOut>",on_leave_User_Changes_10)
                                Frame(User_Adress_Change_Label_frm,width=165,height=2,bg="black").place(x=230,y=207)#That line under the entry

                                #Address Changes Submit Button
                                User_Address_Change_Submit=Button(User_Adress_Change_Label_frm,text="Submit",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Adderss_change_Submit)
                                User_Address_Change_Submit.place(x=380,y=230)

                            
                            else:
                                messagebox.showerror('ERROR','Unknown Error In Choosing Parameter')


                            #Back Button Details Changes Page to User Page 2 ---------->
                            User_Back_7=Button(user_frm_7,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_12)
                            User_Back_7.place(x=15,y=15)
                        
                        else:
                            messagebox.showerror('ERROR','Select a Parameter From the list to Change their Details')
                            
                    else:
                        messagebox.showerror('ERROR','Choose Only the Parameter Displayed in the List')


                #ComboBox For Choosing the New User   
                def Account_Details_Changes_combo(event_1):
                    
                    global USER_Changes_COMBOBOX
                    pass

                global Changes_List_Options
                Changes_List_Options=["--Select--",
                                      "User Name",
                                      "Password",
                                      "Mobile Number",
                                      "Email Id",
                                      "Parmanent Address",
                                      "Current Address"]

                Changes_Options_Label=Label(User_Details_Changes_Label_frm,text="Options       :",font=("dubai","12"),fg="black",bg="white")
                Changes_Options_Label.place(x=20,y=39)
                    
                USER_Changes_COMBOBOX=ttk.Combobox(User_Details_Changes_Label_frm,width=35,values=Changes_List_Options,justify="center")
                USER_Changes_COMBOBOX.current(0)
                USER_Changes_COMBOBOX.bind("<<ComboboxSelected>>",Account_Details_Changes_combo)
                USER_Changes_COMBOBOX.place(x=170,y=44)

                User_details_Changes_Button=Button(User_Details_Changes_Label_frm,text="Proceed",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=Account_Changes_Entry)
                User_details_Changes_Button.place(x=230,y=80)

                #Back Button Details Changes Page to User Page 2 ---------->
                User_Back_6=Button(user_frm_6,text="Back",font=("nirmala ui","12","bold"),fg="white",bg="black",relief="ridge",bd=5,command=back_11)
                User_Back_6.place(x=15,y=15)
                
            else:
                messagebox.showerror('ERROR','You Already Have A Pending Request To Change Details\n You Can Raise Another Once THe Pending One Is Complete')
             
        
        if user_pass_check==True:
            
            cursor.execute("use user_account")
            cursor.execute("Select User_Name from Personal_Details")
            user_name_fetch=User_Name.get()
            user_count_1=0
            for usernames in cursor:
                #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                for x in usernames:
                    if user_name_fetch==x:
                        user_count_1=user_count_1+1  
                    else:
                        pass

            user_Password_Check_1=False
            
            User_Username_Login_check_Password=f"'{user_name_fetch}'"
            user_Password_fetch=Password_1.get()
            User_Login_Pass_check=f"Select User_Password from Personal_Details where User_Name={User_Username_Login_check_Password}"
            cursor.execute("use user_account")
            cursor.execute(User_Login_Pass_check)
            
            for Passwords in cursor:
                #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                for x1 in Passwords:
                    if user_Password_fetch==x1:
                        user_Password_Check_1=True
                    else:
                        user_Password_Check_1=False

            if user_count_1==1:
                if user_Password_Check_1==True:
                    messagebox.showinfo('MESSAGE','Login Sucessfull')
                    
                    #User Frame 2--------------->

                    def back_7():
                        user_frm_2.destroy()
                        User_Name.delete(0,"end")
                        User_Name.insert(0,"UserName")
                        Password_1.delete(0,"end")
                        Password_1.insert(0,"Password")
                        
                    user_frm_2=Frame(user_frm1,width=1509,height=942,bg="white")
                    user_frm_2.place(x=0,y=0)

                    user_frm_2_label_1=Label(user_frm_2,text="What's Your Need",font=("dubai","40","bold"),fg="BLACK",bg="white")
                    user_frm_2_label_1.place(x=440,y=200)
                    
                    user_frm_2_Button_2=Button(user_frm_2,width=28,text="Transaction",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=User_Transaction)
                    user_frm_2_Button_2.place(x=520,y=310)

                    user_frm_2_Button_3=Button(user_frm_2,width=28,text="View Balence",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=user_Balence)
                    user_frm_2_Button_3.place(x=520,y=370)

                    user_frm_2_Button_4=Button(user_frm_2,width=28,text="Request Changes In Account Details",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=Account_Details_Changes)          
                    user_frm_2_Button_4.place(x=520,y=430)

                    #Back Button User Page 2 to User Page 1 ---------->
                    User_Back_2=Button(user_frm_2,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_7)
                    User_Back_2.place(x=15,y=15)
                else:
                    messagebox.showerror('ERROR','Incorrect Password')

            else:
                messagebox.showerror('ERROR','Incorrect UserName')
                
        else:
            errorcode_1()


    #User frame 1 ---------->
    user_frm1=Frame(root,width=1509,height=942,bg="white")
    user_frm1.place(x=0,y=0)
    user_image1=Image.open("//Users//thillaim//Desktop//Python//Project images//User1.jpg")
    test1=ImageTk.PhotoImage(user_image1)
    user_image_label1=Label(user_frm1,image=test1,bg="white")
    user_image_label1.image=test1
    user_image_label1.place(x=200,y=200)

    #Back Button User Page 1 to 1st Page ---------->
    User_Back_1=Button(user_frm1,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_1)
    User_Back_1.place(x=15,y=15)

    #Username Entry ---------->

    '''
    default "Username" word will be shown in the entry box once we click the cursor it will dissappeare and we can give a fresh entry
    '''
    def on_enter(e):
        name=User_Name.get()
        if name=="UserName":
            User_Name.delete(0,"end")

    def on_leave(e):
        name=User_Name.get()
        if name=='':
            User_Name.insert(0,"UserName")      
    
    user_frame1_Label1=Label(user_frm1,text="Login",font=("Microsoft yahei ui light","26","bold"),fg="#57a1f8",bg="white").place(x=700,y=180)
    User_Name=Entry(user_frm1,width=25,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    User_Name.place(x=650,y=290)
    User_Name.insert(0,"UserName")
    User_Name.bind("<FocusIn>",on_enter)
    User_Name.bind("<FocusOut>",on_leave)
    

    Frame(user_frm1,width=295,height=2,bg="black").place(x=650,y=310)#That line under the entry

    #Password Entry ---------->

    '''
    default "password" word will be shown in the entry box once we click the cursor it will dissappeare and we can give a fresh entry
    '''
    
    def on_enter(e):
        name=Password_1.get()
        if name=="Password":
            Password_1.delete(0,"end")
    def on_leave(e):
        name=Password_1.get()
        if name=='':
            Password_1.insert(0,"Password")

    Password_1=Entry(user_frm1,width=25,border=0,fg="black",font=("Microsoft yahei ui light","10"))
    Password_1.place(x=650,y=360)
    Password_1.insert(0,"Password")
    Password_1.bind("<FocusIn>",on_enter)
    Password_1.bind("<FocusOut>",on_leave)

    Frame(user_frm1,width=295,height=2,bg="black").place(x=650,y=380)#That line under the entry

    #New User Button... ---------->
    new_user_button=Button(user_frm1,text="Don't have an Account ?",bd=0,relief="flat",font=("Microsoft yahei ui light","9","bold"),fg="#619bcc",bg="white",command=New_User_Page)
    new_user_button.place(x=650,y=385)

    #LOGIN Button... ---------->
    User_login_button=Button(user_frm1,width=21,text="LOGIN...",bg="sky blue",relief="ridge",bd=0,font=("castellar","13","bold"),command=login_1)
    User_login_button.place(x=648,y=425)

#------------------------------------------------------------------------------------------------------------------------------------------------------->
#Admin Frame

#
def User_Details_Changs_Admin_Work():

    #Back From New Request Page to Admin Page 1
    def back_13():
        Admin_Frame_5.destroy()

    #Admin Frame 4--------------->
    Admin_Frame_5=Frame(Admin_Frame_2,width=1509,height=942,bg="white")
    Admin_Frame_5.place(x=0,y=0)

    Admin_Frame_5_Label_frm_1=LabelFrame(Admin_Frame_5,text="Account Details Changes",font=("dubai","14","bold"),fg="black",bg="white")
    Admin_Frame_5_Label_frm_1.place(x=90,y=70,width=520,height=170)

    #Back Button Account Details Changes Page to Admin Page 1 ---------->
    Admin_Back_5=Button(Admin_Frame_5,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_13)
    Admin_Back_5.place(x=15,y=15)

    #ComboBox For Choosing the New User   
    def User_Changes_Admin_Selected_Username(event_1):
        pass

    global User_Details_Changes_Request_Usernames
    User_Details_Changes_Request_Usernames=["--Select--"]

    cursor.execute("use user_account")
    cursor.execute("Select User_Name from User_Changes")

    for usernames_1 in cursor:
        for individuals_1 in usernames_1:
            User_Details_Changes_Request_Usernames.append(individuals_1)

    
    User_Details_Changes_request_Label_1=Label(Admin_Frame_5_Label_frm_1,text="USERNAMES       :",font=("dubai","12"),fg="black",bg="white")
    User_Details_Changes_request_Label_1.place(x=20,y=39)

    global USER_Details_Changes_COMBOBOX        
    USER_Details_Changes_COMBOBOX=ttk.Combobox(Admin_Frame_5_Label_frm_1,width=35,values=User_Details_Changes_Request_Usernames,justify="center")
    USER_Details_Changes_COMBOBOX.current(0)
    USER_Details_Changes_COMBOBOX.bind("<<ComboboxSelected>>",User_Changes_Admin_Selected_Username)
    USER_Details_Changes_COMBOBOX.place(x=170,y=44)


    def User_Account_Details_Changes_Admin_Page():

        selection_Check_count_1_1=0
        selection_Check_count_1_2=0

        if USER_Details_Changes_COMBOBOX.get()=="--Select--":
            selection_Check_count_1_1=selection_Check_count_1_1+1
        elif USER_Details_Changes_COMBOBOX.get() not in User_Details_Changes_Request_Usernames:
            selection_Check_count_1_2=selection_Check_count_1_2+1
        else:
            pass
        
        if selection_Check_count_1_1==0:
        
            if selection_Check_count_1_2==0:

                #Back Button New User Details Page to New Request Page
                def back_14():
                    Admin_Frame_6.destroy()
                    USER_Details_Changes_COMBOBOX.current(0)
                
                Admin_Frame_6=Frame(Admin_Frame_5,width=1509,height=942,bg="white")
                Admin_Frame_6.place(x=0,y=0)
                
                #Back Button New User Details Page to New Request Page ---------->
                Admin_Back_6=Button(Admin_Frame_6,text="Back",font=("nirmala ui","12","bold"),fg="white",bg="black",relief="ridge",bd=5,command=back_14)
                Admin_Back_6.place(x=15,y=15)
                
                Admin_Selected_User_Change=USER_Details_Changes_COMBOBOX.get()
                cursor.execute("use user_account")
                Fetching_selected_User_Changing_details=f"select * from User_Changes where User_Name='{Admin_Selected_User_Change}'"
                cursor.execute(Fetching_selected_User_Changing_details)

                user_Changes_Details_List=[]
                user_Changes_Details_List_1=[]

                #Fetching The Selected user's Data From Request Database
                for Datas_1 in cursor:
                    for individual_Data_1 in Datas_1:
                        user_Changes_Details_List.append(individual_Data_1)
                        user_Changes_Details_List_1.append(individual_Data_1)

                if user_Changes_Details_List[1]=="User Name" or user_Changes_Details_List[1]=="Password" or user_Changes_Details_List[1]=="Mobile Number" or user_Changes_Details_List[1]=="Email Id":

                    #Showing The Details of User Changes in Label Format
                    Admin_User_Info_Chances_Details_Labelfrm=LabelFrame(Admin_Frame_6,text=f"{user_Changes_Details_List[1]} Changes",font=("dubai","14","bold"),fg="black",bg="white")
                    Admin_User_Info_Chances_Details_Labelfrm.place(x=90,y=70,width=450,height=130)

                    Admin_User_Details_Changes_Label_1=Label(Admin_User_Info_Chances_Details_Labelfrm,text=f"{user_Changes_Details_List[1]}",font=("dubai","12","bold"),fg="BLACK",bg="white")
                    Admin_User_Details_Changes_Label_1.place(x=15,y=39)

                    Admin_User_Details_Changes_Label_2=Label(Admin_User_Info_Chances_Details_Labelfrm,text=":",font=("dubai","12","bold"),fg="BLACK",bg="white")
                    Admin_User_Details_Changes_Label_2.place(x=208,y=46)
                 
                    Admin_User_Details_Changes_Label_3=Label(Admin_User_Info_Chances_Details_Labelfrm,text=f"{user_Changes_Details_List[2]}",font=("nirmala ui","12"),fg="BLACK",bg="white")
                    Admin_User_Details_Changes_Label_3.place(x=223,y=45)

                    #Accepting User Changes Request
                    def Admin_User_changes_Accept_Changes():

                        if user_Changes_Details_List[1]=="User Name":
                            changing_Parameter="User_Name"
                        elif user_Changes_Details_List[1]=="Password":
                            changing_Parameter="User_Password"
                        elif user_Changes_Details_List[1]=="Mobile Number":
                            changing_Parameter="Mobile_Number"
                        elif user_Changes_Details_List[1]=="Email Id":
                            changing_Parameter="Email_ID"
                        else:
                            pass

                        cursor.execute("use user_account")
                        Processing_User_details_Changes=f"UPDATE `user_account`.`Personal_Details` SET `{changing_Parameter}` = '{user_Changes_Details_List[2]}' WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Processing_User_details_Changes)
                        my_DB.commit()

                        cursor.execute("use user_account")
                        Deleting_User_details_Changes_Data_From_Initial_Table=f"DELETE FROM `user_account`.`User_Changes` WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Deleting_User_details_Changes_Data_From_Initial_Table)
                        my_DB.commit()

                        messagebox.showinfo('MESSAGE','Changes Suceccfully Updated')
                        Admin_Frame_6.destroy()
                        Admin_Frame_5.destroy()
                        User_Details_Changs_Admin_Work()

                    def Admin_User_changes_Reject_Changes():

                        cursor.execute("use user_account")
                        Deleting_User_details_Changes_Data_From_Initial_Table_1=f"DELETE FROM `user_account`.`User_Changes` WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Deleting_User_details_Changes_Data_From_Initial_Table_1)
                        my_DB.commit()

                        messagebox.showinfo('MESSAGE','Request Deleted')
                        Admin_Frame_6.destroy()
                        Admin_Frame_5.destroy()
                        User_Details_Changs_Admin_Work()
                        

                    Admin_User_changes_Accept_button=Button(Admin_Frame_6,text="Preceed Changes",font=("nirmala ui","10","bold"),bg="black",relief="ridge",bd=0,command=Admin_User_changes_Accept_Changes)
                    Admin_User_changes_Accept_button.place(x=415,y=230)

                    Admin_User_changes_Accept_button=Button(Admin_Frame_6,text="Reject Request",font=("nirmala ui","10","bold"),bg="black",relief="ridge",bd=0,command=Admin_User_changes_Reject_Changes)
                    Admin_User_changes_Accept_button.place(x=90,y=230)

                elif user_Changes_Details_List[1]=="Parmanent Address" or user_Changes_Details_List[1]=="Current Address":

                    #Showing The Details of User Changes in Label Format
                    Admin_User_Adress_Change_Label_frm=LabelFrame(Admin_Frame_6,text=f"{user_Changes_Details_List[1]} Changes",font=("dubai","14","bold"),fg="black",bg="white")
                    Admin_User_Adress_Change_Label_frm.place(x=90,y=70,width=450,height=175)

                    Admin_User_Address_Details_Changes_Label_1=Label(Admin_User_Adress_Change_Label_frm,text=f"{user_Changes_Details_List[1]}",font=("dubai","12","bold"),fg="BLACK",bg="white")
                    Admin_User_Address_Details_Changes_Label_1.place(x=15,y=39)

                    Admin_User_Address_Details_Changes_Label_2=Label(Admin_User_Adress_Change_Label_frm,text=":",font=("dubai","12","bold"),fg="BLACK",bg="white")
                    Admin_User_Address_Details_Changes_Label_2.place(x=208,y=43)
                 
                    Admin_User_Address_Details_Changes_Label_3=Label(Admin_User_Adress_Change_Label_frm,text=f"{user_Changes_Details_List[2]}",font=("nirmala ui","12"),fg="BLACK",bg="white",justify="left")
                    Admin_User_Address_Details_Changes_Label_3.place(x=223,y=42)

                    def Admin_User_Adress_Change_Accept_Changes():

                        if user_Changes_Details_List[1]=="Parmanent Address":
                            changing_Parameter="Parmanent_Address"
                        elif user_Changes_Details_List[1]=="Current Address":
                            changing_Parameter="Current_Address"
                        else:
                            pass

                        cursor.execute("use user_account")
                        Processing_User_details_Changes_1=f"UPDATE `user_account`.`Personal_Details` SET `{changing_Parameter}` = '{user_Changes_Details_List[2]}' WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Processing_User_details_Changes_1)
                        my_DB.commit()

                        cursor.execute("use user_account")
                        Deleting_User_details_Changes_Data_From_Initial_Table_2=f"DELETE FROM `user_account`.`User_Changes` WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Deleting_User_details_Changes_Data_From_Initial_Table_2)
                        my_DB.commit()

                        messagebox.showinfo('MESSAGE','Changes Suceccfully Updated')
                        Admin_Frame_6.destroy()
                        Admin_Frame_5.destroy()
                        User_Details_Changs_Admin_Work()

                    def Admin_User_Adress_Change_Reject_Changes():

                        cursor.execute("use user_account")
                        Deleting_User_details_Changes_Data_From_Initial_Table_3=f"DELETE FROM `user_account`.`User_Changes` WHERE (`User_Name` = '{user_Changes_Details_List[0]}');"
                        cursor.execute(Deleting_User_details_Changes_Data_From_Initial_Table_3)
                        my_DB.commit()

                        messagebox.showinfo('MESSAGE','Request Deleted')
                        Admin_Frame_6.destroy()
                        Admin_Frame_5.destroy()
                        User_Details_Changs_Admin_Work()
                        

                    Admin_User_Address_changes_Accept_button=Button(Admin_Frame_6,text="Preceed Changes",font=("nirmala ui","10","bold"),bg="black",relief="ridge",bd=0,command=Admin_User_Adress_Change_Accept_Changes)
                    Admin_User_Address_changes_Accept_button.place(x=415,y=260)

                    Admin_User_Address_changes_Accept_button=Button(Admin_Frame_6,text="Reject Request",font=("nirmala ui","10","bold"),bg="black",relief="ridge",bd=0,command=Admin_User_Adress_Change_Reject_Changes)
                    Admin_User_Address_changes_Accept_button.place(x=90,y=260)
                    

            else:
                messagebox.showerror('ERROR','Choose Only the Usernames Displayed in the List')

        else:
            messagebox.showerror('ERROR','Select a Username From the list to Display their Details')
            
    #User Details Changes to be Showmn when Clicking this button
    Admin_user_Changes_details_Button=Button(Admin_Frame_5_Label_frm_1,text="Show Details",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=User_Account_Details_Changes_Admin_Page)
    Admin_user_Changes_details_Button.place(x=230,y=80)
           

#New User Requests Admin's Action----------------------------------------------------------->
def New_User_Request_Admin():

    #Back From New Request Page to Admin Page 1
    def back_5():
        Admin_Frame_3.destroy()

    #Admin Frame 3--------------->
    Admin_Frame_3=Frame(Admin_Frame_2,width=1509,height=942,bg="white")
    Admin_Frame_3.place(x=0,y=0)

    Admin_Label_frm_1=LabelFrame(Admin_Frame_3,text="New Requests",font=("dubai","14","bold"),fg="black",bg="white")
    Admin_Label_frm_1.place(x=90,y=70,width=520,height=170)

    #Back Button New Reqyest Page to Admin Page 1 ---------->
    Admin_Back_3=Button(Admin_Frame_3,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_5)
    Admin_Back_3.place(x=15,y=15)

    #ComboBox For Choosing the New User   
    def New_Request_combo(event_1):
        global Admin_Select_New_username
        Admin_Select_New_username=NEW_USER_COMBOBOX.get()

    global New_User_Request_Usernames
    New_User_Request_Usernames=["--Select--"]

    cursor.execute("use new_user_account")
    cursor.execute("Select New_User_Name from New_User_Details")

    for usernames in cursor:
        for individuals in usernames:
            New_User_Request_Usernames.append(individuals)

    
    new_user_request_Label_Usernames=Label(Admin_Label_frm_1,text="USERNAMES       :",font=("dubai","12"),fg="black",bg="white")
    new_user_request_Label_Usernames.place(x=20,y=39)
        
    NEW_USER_COMBOBOX=ttk.Combobox(Admin_Label_frm_1,width=35,values=New_User_Request_Usernames,justify="center")
    NEW_USER_COMBOBOX.current(0)
    NEW_USER_COMBOBOX.bind("<<ComboboxSelected>>",New_Request_combo)
    NEW_USER_COMBOBOX.place(x=170,y=44)


    def New_User_Details_Page():

        selection_Check_count=0
        selection_Check_count_1=0

        if NEW_USER_COMBOBOX.get()=="--Select--":
            selection_Check_count_1=selection_Check_count_1+1
        elif NEW_USER_COMBOBOX.get() not in New_User_Request_Usernames:
            selection_Check_count=selection_Check_count+1
        else:
            pass
        if selection_Check_count_1==0:
            if selection_Check_count==0:

                #Back Button New User Details Page to New Request Page
                def back_6():
                    Admin_Frame_4.destroy()
                
                Admin_Frame_4=Frame(Admin_Frame_3,width=1509,height=942,bg="white")
                Admin_Frame_4.place(x=0,y=0)
                
                #Back Button New User Details Page to New Request Page ---------->
                Admin_Back_4=Button(Admin_Frame_4,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_6)
                Admin_Back_4.place(x=15,y=15)

                Admin_Selected_New_User=NEW_USER_COMBOBOX.get()
                cursor.execute("use new_user_account")
                Fetching_selected_newuser_details=f"select * from New_User_Details where New_User_Name='{Admin_Selected_New_User}'"
                cursor.execute(Fetching_selected_newuser_details)

                New_user_Details_List=[]
                New_user_Details_List_1=[]

                #Fetching The Selected user's Data From Request Database
                for Datas in cursor:
                    for individual_Data in Datas:
                        New_user_Details_List.append(individual_Data)
                        New_user_Details_List_1.append(individual_Data)
                        

                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)

                #Showing The Details of New User in Label Format
                Admin_Request_Label_frm_newuser_1=LabelFrame(Admin_Frame_4,text="Personal Details",font=("dubai","14","bold"),fg="black",bg="white")
                Admin_Request_Label_frm_newuser_1.place(x=90,y=70,width=470,height=500)

                Admin_new_user_request_Label_1=Label(Admin_Request_Label_frm_newuser_1,text="Account Holder's Name :",font=("dubai","11"),fg="black",bg="white")
                Admin_new_user_request_Label_1.place(x=19,y=13)
                Admin_new_user_request_entry_1=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_1.place(x=190,y=15)
                Admin_new_user_request_entry_1.delete(0,END)
                Admin_new_user_request_entry_1.insert(END,New_user_Details_List[0])
                
                Admin_new_user_request_Label_2=Label(Admin_Request_Label_frm_newuser_1,text="SEX                               :",font=("dubai","11"),fg="black",bg="white")
                Admin_new_user_request_Label_2.place(x=20,y=49)
                Admin_new_user_request_entry_2=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_2.place(x=190,y=54)
                Admin_new_user_request_entry_2.delete(0,END)
                Admin_new_user_request_entry_2.insert(END,New_user_Details_List[1])
            
                Admin_new_user_request_Label_3=Label(Admin_Request_Label_frm_newuser_1,text="Father's Name              :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_3.place(x=20,y=90)
                Admin_new_user_request_entry_3=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_3.place(x=190,y=95)
                Admin_new_user_request_entry_3.delete(0,END)
                Admin_new_user_request_entry_3.insert(END,New_user_Details_List[2])

                Admin_new_user_request_Label_4=Label(Admin_Request_Label_frm_newuser_1,text="Mother's Name             :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_4.place(x=20,y=135)
                Admin_new_user_request_entry_4=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_4.place(x=190,y=140)
                Admin_new_user_request_entry_4.delete(0,END)
                Admin_new_user_request_entry_4.insert(END,New_user_Details_List[3])

                Admin_new_user_request_Label_5=Label(Admin_Request_Label_frm_newuser_1,text="Date Of Birth                 :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_5.place(x=20,y=180)
                Admin_new_user_request_Label_6=Label(Admin_Request_Label_frm_newuser_1,text="(YYYYMMDD)",font=("dubai","8"),fg="black",bg="white")
                Admin_new_user_request_Label_6.place(x=20,y=202)
                Admin_new_user_request_entry_5=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_5.place(x=190,y=185)
                Admin_new_user_request_entry_5.delete(0,END)
                Admin_new_user_request_entry_5.insert(END,New_user_Details_List[4])
                
                Admin_new_user_request_Label_7=Label(Admin_Request_Label_frm_newuser_1,text="AGE                               :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_7.place(x=20,y=235)
                Admin_new_user_request_entry_6=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_6.place(x=190,y=240)
                Admin_new_user_request_entry_6.delete(0,END)
                Admin_new_user_request_entry_6.insert(END,New_user_Details_List[5])
                
                Admin_new_user_request_Label_8=Label(Admin_Request_Label_frm_newuser_1,text="Aadar Number              :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_8.place(x=20,y=281)
                Admin_new_user_request_entry_7=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_7.place(x=190,y=284)
                Admin_new_user_request_entry_7.delete(0,END)
                Admin_new_user_request_entry_7.insert(END,New_user_Details_List[6])

                Admin_new_user_request_Label_9=Label(Admin_Request_Label_frm_newuser_1,text="Mobile Number             :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_9.place(x=20,y=330)
                Admin_new_user_request_entry_8=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_8.place(x=190,y=334)
                Admin_new_user_request_entry_8.delete(0,END)
                Admin_new_user_request_entry_8.insert(END,New_user_Details_List[7])
                
                Admin_new_user_request_Label_10=Label(Admin_Request_Label_frm_newuser_1,text="Email ID                        :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_10.place(x=20,y=381)
                Admin_new_user_request_entry_9=Entry(Admin_Request_Label_frm_newuser_1,width=35,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_9.place(x=190,y=385)
                Admin_new_user_request_entry_9.delete(0,END)
                Admin_new_user_request_entry_9.insert(END,New_user_Details_List[8])

                Admin_new_user_request_Label_11=Label(Admin_Request_Label_frm_newuser_1,text="Education Qualification :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_11.place(x=19,y=425)
                Admin_new_user_request_entry_10=Entry(Admin_Request_Label_frm_newuser_1,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_10.place(x=192,y=430)
                Admin_new_user_request_entry_10.delete(0,END)
                Admin_new_user_request_entry_10.insert(END,New_user_Details_List[9])
                
                #Parmanent Address Frame--------------------------------------->
                Admin_Request_Label_frm_newuser_2=LabelFrame(Admin_Frame_4,text="Parmanent Address",font=("dubai","14","bold"),fg="black",bg="white")
                Admin_Request_Label_frm_newuser_2.place(x=600,y=70,width=450,height=300)
                
                Admin_new_user_request_Label_12=Label(Admin_Request_Label_frm_newuser_2,text="Nationality                             :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_12.place(x=20,y=20)
                Admin_new_user_request_entry_11=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_11.place(x=230,y=25)
                Admin_new_user_request_entry_11.delete(0,END)
                Admin_new_user_request_entry_11.insert(END,New_user_Details_List[10])

                #Poping the Datas till Nationality so that that wont get in the way of separating address lines
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)
                New_user_Details_List.pop(0)

                #from the modified Data list Address are separated line by line
                NEW_P_Address_Data=New_user_Details_List[0]
                New_User_P_Address_Details=NEW_P_Address_Data.split("\n")
                NEW_USER_REQUEST_STATE_DISTRICE=New_User_P_Address_Details[2]
                New_User_P_Address_Details_State_District=NEW_USER_REQUEST_STATE_DISTRICE.split(",")
                

                Admin_new_user_request_Label_13=Label(Admin_Request_Label_frm_newuser_2,text="State                                        :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_13.place(x=20,y=60)
                Admin_new_user_request_entry_12=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_12.place(x=230,y=65)
                Admin_new_user_request_entry_12.delete(0,END)
                Admin_new_user_request_entry_12.insert(END,New_User_P_Address_Details_State_District[0])

                Admin_new_user_request_Label_14=Label(Admin_Request_Label_frm_newuser_2,text="Parmanent Address Line 1   :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_14.place(x=20,y=100)
                Admin_new_user_request_entry_13=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_13.place(x=230,y=105)
                Admin_new_user_request_entry_13.delete(0,END)
                Admin_new_user_request_entry_13.insert(END,New_User_P_Address_Details[0])
               
                Admin_new_user_request_Label_15=Label(Admin_Request_Label_frm_newuser_2,text="Parmanent Address Line 2   :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_15.place(x=20,y=140)
                Admin_new_user_request_entry_14=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_14.place(x=230,y=145)
                Admin_new_user_request_entry_14.delete(0,END)
                Admin_new_user_request_entry_14.insert(END,New_User_P_Address_Details[1])
                
                Admin_new_user_request_Label_16=Label(Admin_Request_Label_frm_newuser_2,text="Parmanent Address Line 3   :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_16.place(x=20,y=190)
                Admin_new_user_request_entry_15=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_15.place(x=230,y=195)
                Admin_new_user_request_entry_15.delete(0,END)
                Admin_new_user_request_entry_15.insert(END,New_User_P_Address_Details_State_District[1])
                
                Admin_new_user_request_Label_17=Label(Admin_Request_Label_frm_newuser_2,text="Parmanent Address Pincode :",font=("dubai","12"),fg="black",bg="white")
                Admin_new_user_request_Label_17.place(x=20,y=240)
                Admin_new_user_request_entry_16=Entry(Admin_Request_Label_frm_newuser_2,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                Admin_new_user_request_entry_16.place(x=232,y=245)
                Admin_new_user_request_entry_16.delete(0,END)
                Admin_new_user_request_entry_16.insert(END,New_User_P_Address_Details[3])

                #Poping the P Address so we can easily acces the C Address Section
                New_user_Details_List.pop(0)
                NEW_USER_REQUEST_C_A=New_user_Details_List[0]
                
                if NEW_USER_REQUEST_C_A=="SAME AS PARMANENT ADDRESS":
                    
                    Admin_Request_Label_frm_newuser_3=LabelFrame(Admin_Frame_4,text="Current Address",font=("dubai","14","bold"),fg="black",bg="white")
                    Admin_Request_Label_frm_newuser_3.place(x=600,y=380,width=450,height=105)

                    Admin_new_user_request_Label_18=Label(Admin_Request_Label_frm_newuser_3,text="SAME AS PARMANENT ADDRESS",font=("dubai","15"),fg="black",bg="white")
                    Admin_new_user_request_Label_18.place(x=55,y=20)
                    
                else:

                    New_User_C_Address_Details=NEW_USER_REQUEST_C_A.split("\n")
                    NEW_USER_REQUEST_C_STATE_DISTRICE=New_User_C_Address_Details[2]
                    New_User_C_Address_Details_State_District=NEW_USER_REQUEST_C_STATE_DISTRICE.split(",")
                        
                    Admin_Request_Label_frm_newuser_3=LabelFrame(Admin_Frame_4,text="Current Address",font=("dubai","14","bold"),fg="black",bg="white")
                    Admin_Request_Label_frm_newuser_3.place(x=600,y=380,width=450,height=190)

                    Admin_new_user_request_Label_19=Label(Admin_Request_Label_frm_newuser_3,text="State                                        :",font=("dubai","12"),fg="black",bg="white")
                    Admin_new_user_request_Label_19.place(x=20,y=10)
                    Admin_new_user_request_entry_17=Entry(Admin_Request_Label_frm_newuser_3,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                    Admin_new_user_request_entry_17.place(x=230,y=15)
                    Admin_new_user_request_entry_17.delete(0,END)
                    Admin_new_user_request_entry_17.insert(END,New_User_C_Address_Details_State_District[0])
                    
                    Admin_new_user_request_Label_20=Label(Admin_Request_Label_frm_newuser_3,text="Current Address Line 1         :",font=("dubai","12"),fg="black",bg="white")
                    Admin_new_user_request_Label_20.place(x=20,y=40)
                    Admin_new_user_request_entry_18=Entry(Admin_Request_Label_frm_newuser_3,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                    Admin_new_user_request_entry_18.place(x=230,y=45)
                    Admin_new_user_request_entry_18.delete(0,END)
                    Admin_new_user_request_entry_18.insert(END,New_User_C_Address_Details[0])
                    
                    Admin_new_user_request_Label_21=Label(Admin_Request_Label_frm_newuser_3,text="Current Address Line 2         :",font=("dubai","12"),fg="black",bg="white")
                    Admin_new_user_request_Label_21.place(x=20,y=70)
                    Admin_new_user_request_entry_19=Entry(Admin_Request_Label_frm_newuser_3,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                    Admin_new_user_request_entry_19.place(x=230,y=75)
                    Admin_new_user_request_entry_19.delete(0,END)
                    Admin_new_user_request_entry_19.insert(END,New_User_C_Address_Details[1])
                            
                    Admin_new_user_request_Label_22=Label(Admin_Request_Label_frm_newuser_3,text="Current Address Line 3         :",font=("dubai","12"),fg="black",bg="white")
                    Admin_new_user_request_Label_22.place(x=20,y=100)
                    Admin_new_user_request_entry_20=Entry(Admin_Request_Label_frm_newuser_3,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                    Admin_new_user_request_entry_20.place(x=230,y=105)
                    Admin_new_user_request_entry_20.delete(0,END)
                    Admin_new_user_request_entry_20.insert(END,New_User_C_Address_Details_State_District[1])
                   
                    Admin_new_user_request_Label_23=Label(Admin_Request_Label_frm_newuser_3,text="Current Address Pincode      :",font=("dubai","12"),fg="black",bg="white")
                    Admin_new_user_request_Label_23.place(x=20,y=130)
                    Admin_new_user_request_entry_21=Entry(Admin_Request_Label_frm_newuser_3,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"))
                    Admin_new_user_request_entry_21.place(x=230,y=135)
                    Admin_new_user_request_entry_21.delete(0,END)
                    Admin_new_user_request_entry_21.insert(END,New_User_C_Address_Details[3])

                #Disclaimer To Admin that No Chances can be done by him here
                Admin_new_user_request_Label_24=Label(Admin_Frame_4,text="NO Changes Can Be Made Here",font=("dubai","15","bold"),fg="black",bg="white")
                Admin_new_user_request_Label_24.place(x=460,y=590)

                Admin_new_user_request_Label_25=Label(Admin_Frame_4,text="Any Changes Made Here Won't Reflect in The Database",font=("dubai","15","bold"),fg="black",bg="white")
                Admin_new_user_request_Label_25.place(x=350,y=625)

                Admin_new_user_request_Label_26=Label(Admin_Frame_4,text="If Anything Changed Unknowingly Just Go Back And Come Back Again",font=("dubai","15","bold"),fg="black",bg="white")
                Admin_new_user_request_Label_26.place(x=285,y=665)

                def New_User_Accept():

                    #Generating Account Number to New User For Transaction
                    Account_Number_count=0
                    Account_Number_count_1=[]

                    while Account_Number_count<1:
                        Generated_Acc_Num=randint(10000000000,9999999999999999)
                        Generated_Acc_Num_Str=str(Generated_Acc_Num)
                        cursor.execute("use user_account")
                        cursor.execute("Select Account_Number from Account_Details")
                        Acc_Num_Availability=0
                        for Account_Numbers in cursor:
                            #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                            for Acc_Nums in Account_Numbers:
                                if Generated_Acc_Num_Str==Acc_Nums:
                                    Acc_Num_Availability=Acc_Num_Availability+1  
                                else:
                                    pass
                                
                        if Acc_Num_Availability==0:
                            Account_Number_count_1.append(Generated_Acc_Num_Str)
                            Account_Number_count=Account_Number_count+1
                            break
                        else:
                            pass

                    #Back Button Admin Wrk Pass Page to New Request Details Page
                    def back_Mini_1():
                        Admin_Frame_4_mini_frm_1.destroy()

                    #Admin Work Pass Check --------------------->
                    def Admin_work_Pass_Check():
                        
                        def Adding_New_User():
                            #Adding The New User's Details To the Main Database
                            New_User_Add=f"Insert into Personal_Details VALUES ('{New_user_Details_List_1[0]}','{New_user_Details_List_1[1]}','{New_user_Details_List_1[2]}','{New_user_Details_List_1[3]}','{New_user_Details_List_1[4]}','{New_user_Details_List_1[5]}','{New_user_Details_List_1[6]}','{New_user_Details_List_1[7]}','{New_user_Details_List_1[8]}','{New_user_Details_List_1[9]}','{New_user_Details_List_1[10]}','{New_user_Details_List_1[11]}','{New_user_Details_List_1[12]}','{New_user_Details_List_1[13]}','{New_user_Details_List_1[14]}')"
                            cursor.execute("use user_account")
                            cursor.execute(New_User_Add)
         

                            #Addind New User's Account Number And Minimum Balance to the Main Database
                            New_User_Add_Balence=f"Insert into Account_Details VALUES ('{New_user_Details_List_1[0]}','{New_user_Details_List_1[2]}','{Account_Number_count_1[0]}','5000')"
                            cursor.execute("use user_account")
                            cursor.execute(New_User_Add_Balence)
                            

                            #Removing New User Details from New User Database to Avoid Multiple users of same details in the MAin Database
                            New_User_Remove=f"DELETE FROM `new_user_account`.`New_User_Details` WHERE `New_User_Name` = '{New_user_Details_List_1[0]}'"
                            cursor.execute("use new_user_account")
                            cursor.execute(New_User_Remove)
                            my_DB.commit()

                            messagebox.showinfo('MESSAGE',"New User's Details Added To The Main Database")

                            #Deleting the frames to Avoid furthur errors and Calling The previous frame now
                            Admin_Frame_4.destroy()

                            Admin_Frame_3.destroy()

                            New_User_Request_Admin()

                        cursor.execute("use Admins")
                        Fetching_Admin_Work_Pass=f"select Admin_Pass_for_Work from Admin_Details where Admin_User_Name='{Admin_User_Name.get()}'"
                        cursor.execute(Fetching_Admin_Work_Pass)

                        for Admin_Pass in cursor:
                            for Admin_Work_Pass in Admin_Pass:
                                Admin_Stored_Work_Pass=Admin_Work_Pass
                                
                        if Admin_Stored_Work_Pass==Admin_Work_Pass_Entry.get():
                            
                            Adding_New_User()
                            
                        else:
                            messagebox.showerror('ERROR','Wrong Work Pass')
                                

                    Admin_Frame_4_mini_frm_1=Frame(Admin_Frame_4,width=300,height=300,bg="light Grey")
                    Admin_Frame_4_mini_frm_1.place(x=420,y=280)

                    #Back Button Admin Work Pass Frame To New User Details Page ---------->
                    Admin_Frame_4_mini_frm_1_Back=Button(Admin_Frame_4_mini_frm_1,width=3,text="X",font=("nirmala ui","9","bold"),bg="#FF0000",bd=0,command=back_Mini_1)
                    Admin_Frame_4_mini_frm_1_Back.place(x=275,y=1)

                    Admin_Work_Pass_Label=Label(Admin_Frame_4_mini_frm_1,text="Enter Your Work Password\nTo Make The Action",font=("dubai","10","bold"),fg="black",bg="light Grey")
                    Admin_Work_Pass_Label.place(x=55,y=105)

                    def on_enter_Admin_Wrk_Pass(e):
                        name=Admin_Work_Pass_Entry.get()
                        if name=='None':
                            Admin_Work_Pass_Entry.delete(0,"end")
                        else:
                            pass

                    def on_leave_Admin_Wrk_Pass(e):
                        name=Admin_Work_Pass_Entry.get()
                        if name=='':
                            Admin_Work_Pass_Entry.insert(0,"None")
                            
                    Admin_Work_Pass_Entry=Entry(Admin_Frame_4_mini_frm_1,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"),bg="light Grey")
                    Admin_Work_Pass_Entry.place(x=65,y=155)
                    Admin_Work_Pass_Entry.insert(0,"None")
                    Admin_Work_Pass_Entry.bind("<FocusIn>",on_enter_Admin_Wrk_Pass)
                    Admin_Work_Pass_Entry.bind("<FocusOut>",on_leave_Admin_Wrk_Pass)
                    Frame(Admin_Frame_4_mini_frm_1,width=165,height=2,bg="black").place(x=65,y=178)#That line under the entry

                    #Admin Work Password To Process The Action ---------->
                    Admin_Frame_4_mini_frm_1_Confirm=Button(Admin_Frame_4_mini_frm_1,text="Confirm",font=("nirmala ui","9","bold"),bg="Blue",bd=0,command=Admin_work_Pass_Check)
                    Admin_Frame_4_mini_frm_1_Confirm.place(x=200,y=200)                                          

                def New_User_Reject():

                    def Rejecting_New_User():
                        
                        #Removing New User Details from New User Database
                        New_User_Reject=f"DELETE FROM `new_user_account`.`New_User_Details` WHERE `New_User_Name` = '{New_user_Details_List_1[0]}'"
                        cursor.execute("use new_user_account")
                        cursor.execute(New_User_Reject)
                        my_DB.commit()

                        messagebox.showinfo('MESSAGE',"New User Rejected\nDetails Removed From The Database")

                        #Deleting the frames to Avoid furthur errors and Calling The previous frame now
                        Admin_Frame_4.destroy()

                        Admin_Frame_3.destroy()

                        New_User_Request_Admin()

                    #Back Button Admin Wrk Pass Page to New Request Details Page
                    def back_Mini_2():
                        Admin_Frame_4_mini_frm_2.destroy()

                    def Admin_work_Pass_Check_1():
                        cursor.execute("use Admins")
                        Fetching_Admin_Work_Pass_1=f"select Admin_Pass_for_Work from Admin_Details where Admin_User_Name='{Admin_User_Name.get()}'"
                        cursor.execute(Fetching_Admin_Work_Pass_1)

                        for Admin_Pass_1 in cursor:
                            for Admin_Work_Pass_1 in Admin_Pass_1:
                                Admin_Stored_Work_Pass_1=Admin_Work_Pass_1
                                
                        if Admin_Stored_Work_Pass_1==Admin_Work_Pass_Entry_1.get():
                            
                            Rejecting_New_User()
                            
                        else:
                            messagebox.showerror('ERROR','Wrong Work Pass')

                    Admin_Frame_4_mini_frm_2=Frame(Admin_Frame_4,width=300,height=300,bg="light Grey")
                    Admin_Frame_4_mini_frm_2.place(x=420,y=280)

                    #Back Button Admin Work Pass Frame To New User Details Page ---------->
                    Admin_Frame_4_mini_frm_2_Back=Button(Admin_Frame_4_mini_frm_2,width=3,text="X",font=("nirmala ui","9","bold"),bg="#FF0000",bd=0,command=back_Mini_2)
                    Admin_Frame_4_mini_frm_2_Back.place(x=275,y=1)

                    Admin_Work_Pass_Label_1=Label(Admin_Frame_4_mini_frm_2,text="Enter Your Work Password\nTo Make The Action",font=("dubai","10","bold"),fg="black",bg="light Grey")
                    Admin_Work_Pass_Label_1.place(x=55,y=105)

                    def on_enter_Admin_Wrk_Pass_1(e):
                        name=Admin_Work_Pass_Entry_1.get()
                        if name=='None':
                            Admin_Work_Pass_Entry_1.delete(0,"end")
                        else:
                            pass

                    def on_leave_Admin_Wrk_Pass_1(e):
                        name=Admin_Work_Pass_Entry_1.get()
                        if name=='':
                            Admin_Work_Pass_Entry_1.insert(0,"None")
                            
                    Admin_Work_Pass_Entry_1=Entry(Admin_Frame_4_mini_frm_2,width=23,border=0,fg="black",font=("Microsoft yahei ui light","10"),bg="light Grey")
                    Admin_Work_Pass_Entry_1.place(x=65,y=155)
                    Admin_Work_Pass_Entry_1.insert(0,"None")
                    Admin_Work_Pass_Entry_1.bind("<FocusIn>",on_enter_Admin_Wrk_Pass_1)
                    Admin_Work_Pass_Entry_1.bind("<FocusOut>",on_leave_Admin_Wrk_Pass_1)
                    Frame(Admin_Frame_4_mini_frm_2,width=165,height=2,bg="black").place(x=65,y=178)#That line under the entry

                    #Admin Work Password To Process The Action ---------->
                    Admin_Frame_4_mini_frm_2_Confirm=Button(Admin_Frame_4_mini_frm_2,text="Confirm",font=("nirmala ui","9","bold"),bg="Blue",bd=0,command=Admin_work_Pass_Check_1)
                    Admin_Frame_4_mini_frm_2_Confirm.place(x=200,y=200)                                          



                #New User Accept Button
                new_user_Accept=Button(Admin_Frame_4,text="Accept Request",bg="black",relief="ridge",bd=0,font=("nirmala ui","13","bold"),command=New_User_Accept)
                new_user_Accept.place(x=1150,y=695)

                #New User Reject Button
                new_user_Reject=Button(Admin_Frame_4,text="Reject Request",bg="black",relief="ridge",bd=0,font=("nirmala ui","13","bold"),command=New_User_Reject)
                new_user_Reject.place(x=40,y=695)
                    
            else:
                messagebox.showerror('ERROR','Choose Only the Usernames Displayed in the List')

        else:
            messagebox.showerror('ERROR','Select a Username From the list to Display their Details')


    Admin_newuser_details_Button=Button(Admin_Label_frm_1,text="Show Details",font=("nirmala ui","9","bold"),bg="black",relief="ridge",bd=0,command=New_User_Details_Page)
    Admin_newuser_details_Button.place(x=230,y=80)

    
def Admin_Page_1():

    global Admin_User_Name
    global Admin_Password_1

    #Back From Admin Frame To Cover Page
    def back_3():
        admin_frm1.destroy()

    #Admin Username password Check and Login 
    def Admin_login():

        global Admin_Frame_2
        global Admin_username
        global Admin_username_1

        #Here the Admin's Username is been checked with the Database
        cursor.execute("use Admins")
        cursor.execute("Select Admin_User_Name from Admin_details")
        Admin_user_name_fetch=Admin_User_Name.get()
        Admin_user_count_1=0
        for admin_usernames in cursor:
            #The cursor will give the names in separate separate tuple in single list so we need to itrate it
            for x1 in admin_usernames:
                if Admin_user_name_fetch==x1:
                    Admin_user_count_1=Admin_user_count_1+1
                else:
                    pass
        
        if Admin_User_Name.get()!="Admin UserName" and Admin_Password_1.get()!="Admin Password":
            
            #If the Admin's username is stored in the database it will move forward
            if Admin_user_count_1==1:

                #Here the Admin's Password is been checked with the Database with its username
                Admin_username=Admin_User_Name.get()
                Admin_Password_fetch=Admin_Password_1.get()
                Admin_username_1=f"'{Admin_username}'"
                f=f"select Admin_Password from Admin_details where Admin_User_Name={Admin_username_1}"
                cursor.execute(f)
                admin_Pass_1=False
                for Admin_pass in cursor:
                    for Admin_Password in Admin_pass:
                        if Admin_Password==Admin_Password_fetch:
                            admin_Pass_1=True
                        else:
                            admin_Pass_1=False

                #If the password matches Admin's Frame will appeare                   
                if admin_Pass_1==True:

                    #Getting The Admin's Details in a List To USe It In the Future
                    cursor.execute("use Admins")
                    admin_Details_Get=f"Select * from Admin_details where Admin_User_Name='{Admin_User_Name.get()}'"
                    cursor.execute(admin_Details_Get)
                    global Admin_Details_fetch
                    Admin_Details_fetch=[]
                    for admin_Details_1 in cursor:
                        #The cursor will give the names in separate separate tuple in single list so we need to itrate it
                        for Separate_Details in admin_Details_1:
                            Admin_Details_fetch.append(Separate_Details)
                    
                    messagebox.showinfo('MESSAGE','Login Sucessfull')

                    def back_4():
                        back=messagebox.askquestion("Confirm...?","Do You Want To Leave")
                        if back == 'yes':
                            Admin_Frame_2.destroy()
                            Admin_User_Name.delete(0,"end")
                            Admin_User_Name.insert(0,"Admin UserName")
                            Admin_Password_1.delete(0,"end")
                            Admin_Password_1.insert(0,"Admin Password")
                            
                        else:
                            pass
                    
                    #Admin Frame 2--------------->
                    Admin_Frame_2=Frame(admin_frm1,width=1509,height=942,bg="white")
                    Admin_Frame_2.place(x=0,y=0)
                    Admin_image_2=ImageTk.PhotoImage(file="//Users//thillaim//Desktop//Python//Project images//Admin2.jpg")
                    admin_frm_2_label1=Label(Admin_Frame_2,image=Admin_image_2,bg="white")
                    admin_frm_2_label1.image=Admin_image_2
                    admin_frm_2_label1.place(x=0,y=0)                    
                    
                    admin_frm_2_Button_1=Button(Admin_Frame_2,text="New User Requestes",font=("nirmala ui","13","bold"),bg="black",relief="ridge",bd=0,command=New_User_Request_Admin)
                    admin_frm_2_Button_1.place(x=695,y=485)

                    admin_frm_2_Button_2=Button(Admin_Frame_2,text="Any Changes\n In the\nAccount Details",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=User_Details_Changs_Admin_Work)          
                    admin_frm_2_Button_2.place(x=1117,y=513)

                    #Back Button Admin Page 2 to Admin Page 1 ---------->
                    Admin_Back_2=Button(Admin_Frame_2,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_4)
                    Admin_Back_2.place(x=15,y=15)
                    
                else:
                    messagebox.showerror('ERROR',"Password Doesn't Match")

            else:
                messagebox.showerror('ERROR','Incorrect UserName')
                
        elif Admin_User_Name.get()=="Admin UserName" and Admin_Password_1.get()!="Admin Password":
            messagebox.showerror('ERROR','UserName Required')
            
        elif Admin_User_Name.get()!="Admin UserName" and Admin_Password_1.get()=="Admin Password":
            messagebox.showerror('ERROR','Password Required')

        else:
            messagebox.showerror('ERROR','Input Required')   
    
    #Admin frame 1 ---------->
    admin_frm1=Frame(root,width=1511,height=952,bg="white")
    admin_frm1.place(x=0,y=0)
    admin_image_1=Image.open("//Users//thillaim//Desktop//Python//Project images//Admin1.jpg")
    admin_test_1=ImageTk.PhotoImage(admin_image_1)
    admin_frm_1_label1=Label(admin_frm1,image=admin_test_1,bg="white")
    admin_frm_1_label1.image=admin_test_1
    admin_frm_1_label1.place(x=200,y=200)

    #Back Button Admin Page 1 to Cover Page ---------->
    Admin_Back_1=Button(admin_frm1,text="Back",font=("nirmala ui","12","bold"),bg="black",relief="ridge",bd=0,command=back_3)
    Admin_Back_1.place(x=15,y=15)

    #Username Entry ---------->

    '''
    default "Admin Username" word will be shown in the entry box once we click the cursor it will dissappeare and we can give a fresh entry
    '''
    
    def on_enter__1(e):
        name=Admin_User_Name.get()
        if name=="Admin UserName":
            Admin_User_Name.delete(0,"end")

    def on_leave__1(e):
        name=Admin_User_Name.get()
        if name=='':
            Admin_User_Name.insert(0,"Admin UserName")
 
    user_frame1_Label1=Label(admin_frm1,text="Login",font=("Microsoft yahei ui light","26","bold"),fg="#57a1f8",bg="white").place(x=700,y=180)
    Admin_User_Name=Entry(admin_frm1,width=25,border=0,font=("Microsoft yahei ui light","10"),bg="white")
    Admin_User_Name.place(x=650,y=290)
    Admin_User_Name.insert(0,"Admin UserName")
    Admin_User_Name.bind("<FocusIn>",on_enter__1)
    Admin_User_Name.bind("<FocusOut>",on_leave__1)
    
    Frame(admin_frm1,width=295,height=2,bg="black").place(x=650,y=310)

    #Password Entry ---------->

    '''
    default "Login password" word will be shown in the entry box once we click the cursor it will dissappeare and we can give a fresh entry
    '''
    
    def on_enter(e):
        name=Admin_Password_1.get()
        if name=="Admin Password":
            Admin_Password_1.delete(0,"end")
            
    def on_leave(e):
        name=Admin_Password_1.get()
        if name=='':
            Admin_Password_1.insert(0,"Admin Password")

    Admin_Password_1=Entry(admin_frm1,width=25,border=0,font=("Microsoft yahei ui light","10"),bg="white")
    Admin_Password_1.place(x=650,y=360)
    Admin_Password_1.insert(0,"Admin Password")
    Admin_Password_1.bind("<FocusIn>",on_enter)
    Admin_Password_1.bind("<FocusOut>",on_leave)

    Frame(admin_frm1,width=295,height=2,bg="black").place(x=650,y=380)

    #New User Button... ---------->
    #new_user_button=Button(user_frm1,text="Don't have an Account ?",bd=0,relief="flat",font=("Microsoft yahei ui light","9","bold"),fg="#619bcc",bg="white",command=New_User_Page)
    #new_user_button.place(x=650,y=385)

    #LOGIN Button... ---------->
    User_login_button=Button(admin_frm1,width=21,text="LOGIN...",bg="sky blue",relief="ridge",bd=0,font=("castellar","13","bold"),command=Admin_login)
    User_login_button.place(x=648,y=425)

#------------------------------------------------------------------------------------------------------------------------------------------------------->
#First Frame(Cover Page)
root=Tk()
root.title('Bank Management')
root.wm_attributes("-fullscreen",True)
bankimage=ImageTk.PhotoImage(file="//Users//thillaim//Desktop//Python//Project images//bk2.jpg")
canvas=Canvas(root)
canvas.create_image(-320,-190,image=bankimage,anchor=NW)
canvas.create_text(690,45,text="Bank Management System",fill="White",font=("dubai","35","bold"))
canvas.pack(fill="both",expand=True)

Login_User_Button=Button(root,text="Login As User",font=("nirmala ui","22","bold"),bg="black",relief="ridge",bd=0,command=User_Page_1)
Login_User_Button.place(x=550,y=440)
Login_Admin_Button=Button(root,text="Login As Admin",font=("nirmala ui","22","bold"),bg="black",relief="ridge",bd=0,command=Admin_Page_1)
Login_Admin_Button.place(x=975,y=625)

#Exit Button ---------->
def EXIT():
    root.destroy()
    
Exit_Button=Button(root,text="Exit",font=("nirmala ui","12","bold"),bg="white",relief="ridge",bd=0,command=EXIT)
Exit_Button.place(x=15,y=15)

root.mainloop()
