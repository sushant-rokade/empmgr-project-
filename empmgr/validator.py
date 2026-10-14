#Validate
def parse_salary(text): 
    try: 
        salary = float(text) 
        return salary
    except ValueError: 
        return None 