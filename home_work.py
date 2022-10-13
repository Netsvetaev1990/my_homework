a = ["adffjl","bnnj","cmn", 15, 12, 33]
str_list = []
int_list = []
with open("work.txt", "w") as f:
    for i in a:
        if type(i) == str:
           str_list.append(i)
        elif type(i) == int:
            int_list.append(i)





