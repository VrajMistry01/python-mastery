def username_generator(fullname : str) -> str:    
    #clean the fnaeme
    clean_name = fullname.strip().lower()
    #replace the spaces with underscores
    split_name = clean_name.split() #split without arg will split at space and remove the leading spaces automatically
    if not split_name:
        return ("User name cannot be empty")
    username = "_".join(split_name)+'_'+str(len(clean_name))
    return username
test_list= ["  Vraj Mistry  ", "  John Doe  ", "  Jane Smith  ","Alice","   ","  John  Doe  "]
for name in test_list:
    print(username_generator(name))