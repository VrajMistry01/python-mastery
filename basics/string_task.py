def username_generator(fullname : str) -> str:    
    #clean the fnaeme
    clean_name = fullname.strip().lower()
    #replace the spaces with underscores
    username = clean_name.replace(" ","_")
    username = username+'_'+str(len(clean_name))
    return username
test_list= ["  Vraj Mistry  ", "  John Doe  ", "  Jane Smith  ","Alice","   ","  John  Doe  "]
for name in test_list:
    print(username_generator(name))