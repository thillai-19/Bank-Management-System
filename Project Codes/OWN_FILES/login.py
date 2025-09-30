def crt_1(a,b):

    def username1():
        if len(name)<=15 and len(name)>=4:
            return True
        else:
            return False

    ###
    def pass1():
        if len(password1)>=8:
            return True
        else:
            return False

    ###        
    def check_upper():
        for i in password1:
            if i.isupper():
                return True
            
    ###         
    def check_lower():
        for j in password1:
            if j.islower():
                return True
                        
    ###
    def check_spcl():
        for k in password1:
            if k in spcl:
                return True
                
    ###            
    def check_digit():
        for l in password1:
            if l.isdigit():
                return True
    ##################################################################################
            
    spcl=[".",",","!","@","#","$","%","^","&","*","(",")","-","=","_","+"
          ,"?","<",">","/","{","[","]","}","|",";",":"]

    ###

    name=a
    password1=b

    username1()
    pass1()

    ###
    check_upper()
    ###
    check_lower()
    ###
    check_spcl()
    ###
    check_digit()


    if name=="UserName":
        return False
    else:
        pass

    

    if username1()==True and pass1()==True and check_upper()==True and check_lower()==True and check_spcl()==True and check_digit()==True:
            return True
    else:
        return False
