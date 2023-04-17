# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20200515_w1870557_18705573
 
# Date: Wednesday 08 December 


#create and define variables
i_pass=0
i_defer=0
i_fail=0
total=0
m_loop=True #main loop

#count of progression outcome 
progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0

#lists
tem_log=[]
progress_list=[]
progress_trailer_list=[]
module_retriever_list=[]
excluded_list=[]


#functions
#founction for input
def input_validation(credit_name):
    while True:
        try: #Filtering int inputs only
            user_input=int(input("Please enter your credits at "+credit_name+": "))
            if 0<=user_input<=120 and user_input%20==0: #Flitering only range numbers
                break
            print ("Out of range")
        except ValueError:
            print("Integer required")
    return(user_input)


#founction for list append
def list_append(list_name):#reference(https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python/20196202#:~:text=%3E%3E%3E%20lst.extend(%5B5%2C%206%2C%207%5D)%0A%3E%3E%3E%20lst.extend((8%2C%209%2C%2010))%0A%3E%3E%3E%20lst%0A%5B1%2C%202%2C%203%2C%204%2C%205%2C%206%2C%207%2C%208%2C%209%2C%2010%5D)
    tem_log.extend([i_pass,i_defer,i_fail])
    list_name.append(tem_log)

#print lists
def print_list(log_list,type_list):
    for m_ele in log_list:
        print(type_list,end="")
        print(*m_ele, sep=", ")

#upload to logbook(text file)
def log_fun(list_type):
    log_book.write(str(list_type)+" - "+f'{str(i_pass):>3}'+","+f'{str(i_defer):>2}'+","+f'{str(i_fail):>2}'+"\n")


print("choose your option")
print("\t[1] Student Version")
print("\t[2] Staff Version")
print("\t[3] Staff Version with Vertical Histogram")
print("\t[4] Staff Version with summery")
print("\t[5] Staff Version with Text file")
print()

#getting user input for options
while True:
    con_user=input("Continue with - ")
    if  con_user=="1" or con_user=="2" or con_user=="3" or con_user=="4" or con_user=="5":
        break
    else:
        print("Invalid answer")


#0pen the log book file
log_book=open("Log_book_all.txt","a+")
print()

while m_loop:#Main loop
    tem_log=[]
    while True:#All input loop
        #Input part
        i_pass=input_validation("pass")
        i_defer=input_validation("defer")

        total=i_pass+i_defer
        if total>120: #Checking total
            print("Total incorrect")
            continue

        i_fail=input_validation("fail")

        total=i_pass+i_defer+i_fail
        if total==120:
            break
        else:
            print("Total incorrect")
            print()

    #Process part(Choosing Progression Outcome)
    if i_pass==120:
        list_append(progress_list)#calling function of list append
        log_fun("Progress")#calling funtion of log upload
        print("Progress")
        progress_count+=1
    
    elif i_pass==100:
        list_append(progress_trailer_list)
        log_fun("Progress (module trailer)")
        print("Progress (module trailer) ")
        trailer_count+=1
    
    elif 80<=i_fail<=120:
        list_append(excluded_list)
        log_fun("Exclude")
        print("Exclude")
        excluded_count+=1
    
    else:
        list_append(module_retriever_list)
        log_fun("Module retriever")
        print("Do not progress – module retriever")
        retriever_count+=1

    #student version
    if con_user=="1":
        break

    print()

    print("Would you like to enter another set of data?")
    while True:# Again looping part
        again_loop=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if again_loop=="yes" or again_loop=="y":
            break
        elif again_loop=="quit" or again_loop=="q":
            m_loop=False
            break
        else:
            print("Invalid answer")
    print()

