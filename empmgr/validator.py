#Validate
def parse_salary(text): 
    try: 
        salary = float(text) 
        if salary < 0:
            return None
        return salary
    except ValueError: 
        return None 
    
def check_email(email):
    email = email.strip()
    if ("@" in email and "." in email):
        if (not ' ' in email) and len(email)>10 and email.count("@") == 1 and email.endswith("@gmail.com"):
            if email.count(".") == 1:
                return True
            else:
                if(email.index('.') != 0):
                    if email.index('.') - email.index('@') > 1:
                        return True
    return False