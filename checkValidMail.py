import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def checkValidMail(email):   
  
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
      
    email = "sahasoham01@gmail.com"  
    checkValidMail(email)   
  
    email = "sahasoham01@gmail"  
    checkValidMail(email)   
