import os
def take_data(series_names):
    Series = open(series_names,"r",encoding="utf-8")
    for i in Series:
        i= i.replace("\n","")
        point= input("{} ".format(i))
        Series_Points.append([i,point,"\n"])    
    Series.close() 
def ordered_file(list_name):
    Series_Point= open(list_name,"w",encoding="utf-8")
    for i in Ordered_Series:

        string='    '.join([str(item) for item in i])
        string.join("\n")

        Series_Point.write(string)
    Series_Point.close()
def started():
    print("Welcome To Universal Movie Rankings...")
    first=1
    global list_name
    while (first==1):
        first=2
        start= input("Did you use our app (Yes i have a list/ No,create a list ):")
        if(start=="Yes"or start=="Yes i have a list"):
            global third
            third=1
            while (third==1):
                third=2
                list_name = input("Can you write your list name: ")
                if os.path.exists(list_name):
                    second_action(list_name)
                elif(list_name=="0"):
                    break
                elif(list_name=="come back"):
                    third=2
                    first=1
                else:
                    print("List Not Found")
                    third=1                 
        elif(start=="No"or start=="No,create a list"):
            nineth=1
            while(nineth==1):
                series_names = input("Please enter the name of the list where your series are written.")
                if os.path.exists(series_names):
                    Series_Point =open("Series_Point.txt","w",encoding="utf-8")
                    Series_Point.close()
                    list_name="Series_Point.txt"
                    take_data(series_names)
                    second_action(list_name)
                elif(series_names=="come back"):
                    first=1
                    print("Going Back...\n")
                elif(series_names=="0"):
                    print("App Is Closing...")
                    break
                else:
                    print("Please enter a valid file name...\n")
                    nineth=1

        elif(start=="0"):
            print("Closing App")
            break
        else:
            print("Please choose a true operation...\n")
            first=1          
def second_action(list_name):    
    update(list_name)
    Series_Point = open(list_name,"a",encoding="utf-8")
    global fourth
    fourth=1
    while(fourth==1):
        fourth=2
        print("\nWhat Will You Do\n")
        print("I will add new series >>> 1")   
        print("I will change point >>> 2")
        action= input("Choose an operation: ")
        if(action=="1"):
            add_series = input("What is the name of series: ")
            if(add_series=="come back"):
                print("Going Back...\n")
                fourth=1
            eighth=1
            while(eighth==1):
                    eighth==2
                    add_point = input("What is your rating for the series(0<x<=5): ")
                    if(add_point>"0" and add_point<="5"):  
                        Series_Points.append([add_series,add_point,"\n"])
                        Series = open("Series.txt","a",encoding="utf-8")
                        Series.write(add_series)
                        print("Added Your List... \n")
                        continuee()
                    elif(add_point=="come back"):
                        fourth=1
                        print("Going Back...\n")
                    else:
                        eighth=1
                        print("Please enter a 0<x<=5 number")
        elif(action=="2"):
            fifth=1
            while(fifth==1):
                fifth=2
                change_series = input("What is the name of series: ")
                control1=1
                z=0
                for i in Series_Points:
                    z+=1
                    if(i[0]==change_series ):
                        control1=5
                        sixth=1
                        while(sixth==1):
                            sixth=2
                            new_rate= float(input("What is the new rate for series: "))
                            if (new_rate>0 and new_rate<=5):
                                rated =str(new_rate)
                                i[1]=rated
                                continuee()
                            else:
                                print("Please give a 0<x<=5 number")
                                sixth=1
                    elif(change_series=="0"):  
                        break
                    elif(change_series=="come back"):
                        fifth=2
                        fourth=1
                    elif((len(Series_Points))==z and control1!=5):
                        print("Please enter a series in your list")
                        fifth=1
        elif(action=="0"):
            print("App Is Closing...")
            break
        elif(action=="come back"):
            print("Going Back...\n")
            fourth=2
            global third
            third=1
        else:
            print("Please choose a valid operation...\n")
            fourth=1
def update(list_name):
    Series_Point = open(list_name,"r",encoding="utf-8")
    for i in Series_Point:
        splitted = i.split()
        first_part = " ".join(splitted[:-1])  
        second_part = splitted[-1] 
        Series_Points.append([first_part,second_part,"\n"])
def order():
    global Ordered_Series
    Ordered_Series = sorted(Series_Points, key=lambda x: x[1])
    Ordered_Series.reverse()
    ordered_file(list_name)
def continuee():
    seventh=1
    while(seventh==1):
        seventh=2
        continuee= input("Do you want continue: (yes/no)")
        if(continuee=="yes"):
            global fourth
            fourth=1
        elif (continuee=="no"or continuee=="0"):
            print("Take Care...")
            break
        else:
            seventh=1
            print("Please choose valid operation")

list_name=""
Series_Points=[]
started()
order()