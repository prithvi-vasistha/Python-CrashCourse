def get_formatted_name(fname, lname, mname =''):
    if mname:
        return (f"{fname.title()} {mname.title()} {lname.title()}")
    else:    
        return (f"{fname.title()} {lname.title()}")
def format_first_name(fname): 
    return (f"{fname.title()}") 
