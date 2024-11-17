import tkinter as tk
import random
from tkinter import ttk
import datetime

CurrentDate= datetime.datetime.now()

#DEFINE MC WINDOW
mc = tk.Tk()
mc.title("WATER BILL FORM")

#Title Grid
Title_Frame = tk.Frame(mc)
Title_Frame.pack(anchor = "center", padx=20, pady=10)
Form_title = tk.LabelFrame(Title_Frame, text = "WATER BILL ONLINE FORM")
Form_title.grid(row=0, column=0, padx=0, pady=0)
Form_title.config(font = ("Calibri", 16, "bold"))


#Displays WaterDistrict Address
WaterDistrict_Address = tk.Label(Title_Frame, text ="Corrales Ave. 27 Cagayan De Oro City NON-VAT REG. TIN 000-550-995-000")
WaterDistrict_Address.grid(row=0,column=0)
WaterDistrict_Address.config(font = ("Calibri", 6, "bold"))

Water_District = tk.Label(Form_title, text = "   Cagayan De Oro City Water District")
Water_District.grid(row=1, column=0, padx=19, pady=0)

#DEFINE FRAME IN WINDOW
frame = tk.Frame(mc) 
frame.pack(padx=10, pady=10)


#1st USER INFO GRID
user_info_frame = tk.LabelFrame(frame, text = "User Info")
user_info_frame.grid(row = 0, column = 0, padx = 5, pady = 0)
user_info_frame.config(font = ("Calibri", 14, "bold"))

#First name input
first_name = tk.Label(user_info_frame, text = "First Name")
first_name.grid(row = 0, column = 0)



#Last name input
last_name = tk.Label(user_info_frame, text = "Last Name")
last_name.grid(row = 0, column = 1)

#ENTRIES FOR USER INPUT
first_name_entry = tk.Entry(user_info_frame, width = 14)
last_name_entry = tk.Entry(user_info_frame, width = 15)

first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

#Contact Label
Contact_no = tk.Label(user_info_frame, text = "Contact #")
Contact_no.grid(row = 3, column = 0, columnspan = 2)
Contact_no = tk.Entry(user_info_frame, width = 13)
Contact_no.grid(row = 4, column = 0, columnspan = 2)


#1st Line
# Between_NamesAddress = tk.Canvas(user_info_frame, width=1, height=60, bd=0, highlightthickness=0)
# Between_NamesAddress.create_line(0, 0, 0, 60, fill = "black")
# Between_NamesAddress.grid(row = 0, column = 4, rowspan=5, padx=10, pady=5)

#2nd Line
# Between_NamesReading = tk.Canvas(user_info_frame, width=320, height=1, bd=0, highlightthickness=0)
# Between_NamesReading.create_line(320, 0, 0, 0, fill = "black")
# Between_NamesReading.grid(column=0, row=3, rowspan=5, padx=10, pady=5)
# Between_NamesReading.create_line(180, 0, 0, 0, fill = "black")
# Between_NamesReading.grid(row = 5, column = 0, rowspan=5, columnspan = 2, padx=10, pady=5)
#Age spinbox


#2nd ADDRESS GRID
Address_Frame = tk.LabelFrame(frame, text="Personal Address")
Address_Frame.grid(row=0, column=1, padx=5, pady=5)
Address_Frame.config(font = ("Calibri", 14, "bold"))

#Street
StreetAddress_Label = tk.Label(Address_Frame, text="Street")
StreetAddress_Label.grid(row=0, column=0)
StreetAddress_Entry = tk.Entry(Address_Frame, width= 15)
StreetAddress_Entry.grid(row=1, column=0)

#Barangay
BarangayAddress_Label = tk.Label(Address_Frame, text = "Barangay") 
BarangayAddress_Label.grid(row = 0, column = 1) 
BarangayAddress_Entry = tk.Entry(Address_Frame, width= 15)
BarangayAddress_Entry.grid(row = 1, column = 1)

#City
CityAddress_Label = tk.Label(Address_Frame, text = "City")
CityAddress_Label.grid(row = 0, column=2)
CityAddress_Entry = tk.Entry(Address_Frame, width= 15)
CityAddress_Entry.grid(row= 1, column = 2)

#Province
ProvinceAdress_Label = tk.Label(Address_Frame, text = "Province")
ProvinceAdress_Label.grid(row=2,column=0)
ProvinceAdress_Entry = tk.Entry(Address_Frame, width= 15)
ProvinceAdress_Entry.grid(row=3,column=0) 

#ZipCode
ZipAdress_Label = tk.Label(Address_Frame, text = "Zip Code #")
ZipAdress_Label.grid(row=2,column=1)
ZipAdress_Entry = tk.Entry(Address_Frame, width= 5)
ZipAdress_Entry.grid(row=3,column=1)

#3rd UTILITY REPORT GRID
Utility_Report_Frame = tk.LabelFrame(frame, text= "Utility Report")
Utility_Report_Frame.grid(row=1, column=0, columnspan=2, padx=40, pady=5)
Utility_Report_Frame.config(font = ("Calibri", 14, "bold"))


#Current Data
Date_Label = tk.Label(Utility_Report_Frame, text="Current Date")
Date_Label.grid(row=0, column=0)
Date_Label_Display = tk.Label(Utility_Report_Frame, text=CurrentDate.strftime('%b-%d-%Y'))
Date_Label_Display.config(font=("Calibri", 10, "bold"))
Date_Label_Display.grid(row=1, column=0)

DueDate_Label = tk.Label(Utility_Report_Frame, text="Due Date")
DueDate_Label.grid(row=2,column=0)

#Gives 7 day after current day as Due Date
time_change = datetime.timedelta(days=7)
new_time = CurrentDate + time_change
  
DueDate_Label_Display = tk.Label(Utility_Report_Frame, text=new_time.strftime('%b-%d-%Y'))
DueDate_Label_Display.config(font=("Calibri", 10, "bold"))
DueDate_Label_Display.grid(row=3, column=0)


#Previous and Present Meter Reading
Meter_Readings_Label = tk.Label(Utility_Report_Frame, text="Meter Readings")
Meter_Readings_Label.grid(row=0, column=1, columnspan=2)

#Previous Meter Reading (Randomized between 1000-1050)
PreviousValue = random.randint(1000,1050) #Randomized Previous
PreviousMeter_Label = tk.Label(Utility_Report_Frame, text="PREVIOUS")
PreviousMeter_Label.grid(row=1, column=1)
PreviousMeter_Display = tk.Label(Utility_Report_Frame, width=10, text = PreviousValue)
PreviousMeter_Display.config(font=("Calibri", 10, "bold"))
PreviousMeter_Display.grid(row =2, column=1)

#Present Meter Reading NOTE: INPUT RETURN/ELSE ERROR IF THE INPUT IS LESS THAN 'PreviousValue'
PresentMeter_Label = tk.Label(Utility_Report_Frame, text="PRESENT")
PresentMeter_Label.grid(row=1, column=2)
PresentMeter_Entry = tk.Entry(Utility_Report_Frame, width=10)
PresentMeter_Entry.grid(row=2, column=2)    
#NOTE: INPUT FUNCTION THAT DISPLAYS THE CUBIC METERS

CubicMeter_Label = tk.Label(Utility_Report_Frame, text = "Cubic Meter Consumed")
CubicMeter_Label.grid(row=1,column=3)
CubicMeter_Entry = tk.Label(Utility_Report_Frame, text = "ConsumedVar") #Variable for Waterbill consumption
CubicMeter_Entry.grid(row=2, column=3)


#NOTE: Use random for WIN number gneration




#WINDOW FUNCTION
mc.mainloop()