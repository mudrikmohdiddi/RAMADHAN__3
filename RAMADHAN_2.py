from tkinter import *
from tkinter.ttk import *
from time import strftime
def masiku():
    siku=["Jumatatu","Jumanne","Jumatano","Alhamis","Ijumaa","Jumamosi","Jumapili"]
    from calendar import day_name
    from time import strftime
    for a in range(7):
        if(day_name[a]==strftime("%A")):
            return siku[a]
def saa():
    swala=""
    if(int(strftime("%H"))>=20):
        swala=f"""
Kwasasa: Ishaa na Tarawehe   %H:%M:%S %p
Baadae :{23-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Kiamu laily"""
    elif(int(strftime("%H"))>=19):
        swala=f"""
Kwasasa: Makharib   %H:%M:%S %p
Baadae :00:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Ishaa na Tarawehe"""
    elif(int(strftime("%H"))>=16):
        swala=f"""
Kwasasa: Lasir   %H:%M:%S %p
Baadae :{18-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Makharib"""
    elif(int(strftime("%H"))>=13):
        swala=f"""
Kwasasa: Dhuhur   %H:%M:%S %p
Baadae :{15-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Lasir"""
    elif(int(strftime("%H"))>=7):
        swala=f"""
Kwasasa: Dhuhaa   %H:%M:%S %p
Baadae :{12-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Dhuhur"""
    elif(int(strftime("%H"))>=5):
        swala=f"""
Kwasasa: Al-fagir   %H:%M:%S %p
Baadae :{6-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Dhuhaa"""
    else:
        swala=f"""
Kwasasa: Kiamu laily   %H:%M:%S %p
Baadae :{4-int(strftime("%H"))}:{59-int(strftime("%M"))}:{59-int(strftime("%S"))} Al-fagir"""
    fu=""
    if(int(strftime("%H"))>=18):
        if(int(strftime("%M"))>=47):
            fu="Muda wakufuturu "
        elif(int(strftime("%H"))>=19):
            fu="Muda wakufuturu "
        else:
            fu="Muda wakufunga"
    elif(int(strftime("%H"))>=4):
        if(int(strftime("%M"))>=52):
            fu="Muda wakufunga"
        elif(int(strftime("%H"))>=5):
            fu="Muda wakufunga"
        else:
            fu="Muda wakula daku"
    else:
        fu="Muda wakula daku"
    ram=""
    if(int(strftime("%H"))>=18 and int(strftime("%m"))==3):
        if(int(strftime("%M"))>=47):
            ram=f"Ramadhan ya {int(strftime("%d"))-10}"
        elif(int(strftime("%H"))>=19):
            ram=f"Ramadhan ya {int(strftime("%d"))-10}"
        else:
            ram=f"Ramadhan ya {int(strftime("%d"))-11}"
    elif(int(strftime("%H"))>=0 and int(strftime("%m"))==3):
        ram=f"Ramadhan ya {int(strftime("%d"))-11}"
    elif(int(strftime("%H"))>=18 and int(strftime("%m"))==4):
        if(int(strftime("%M"))>=47):
            ram=f"Ramadhan ya {int(strftime("%d"))+21}"
        elif(int(strftime("%H"))>=19):
            ram=f"Ramadhan ya {int(strftime("%d"))+21}"
        else:
            ram=f"Ramadhan ya {int(strftime("%d"))+20}"
    elif(int(strftime("%H"))>=0 and int(strftime("%m"))==4):
        ram=f"Ramadhan ya {int(strftime("%d"))+20}"

    mud.config(text=strftime(f"""
    %H:%M:%S %p
    {masiku()} %B-20%y
_____________________________________________________________________________________
          \n{"NYAKATI ZA SWALA".lower()}
    {swala}
______________________________________________________________________________________
        {fu} saivi  %H:%M:%S %p
_____________________________________________________________________________________
    Leo {ram}   
_____________________________________________________________________________________
BY MUDRIK
"""))
    mud.after(1000,saa)
mud=Label(font=("digital",30),background="green",foreground="cyan")
mud.pack(anchor="ne")
saa()
