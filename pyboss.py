import os
import csv
# Import Date Time module
import datetime

# Open the Input File
csvpath = os.path.join('Resources','boss.csv')

# Dictionary for storing the State abbreviation 
states = {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota',
'MO': 'Missouri','MP': 'Northern Mariana Islands','MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina','ND': 'North Dakota',
'NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio', 'OK': 'Oklahoma',
'OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas',
'UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}

# Reading the CSV file in 'r' mode
f = open(csvpath,'r')
content = f.read()

# Lists to store data
emp_id = []
name = []
fname = []
lname = []
DOB = []
ssn = []
state_abb = []
abb = []


with open (csvpath,newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading every row of CSV file
    for row in csvreader:

        # Checks for the Employee data other than the label(Emp ID)
        if row[0] != "Emp ID":

            #Add Emp Id
            emp_id.append(row[0])
            emp_num = len(emp_id)-1

        # Checks for the Employee Name data
        if row[1] != "Name":  

            # Employee name is splitted using spli function  
            name = row[1].split()

            # Add First and Last Name
            fname.append(name[0])
            lname.append(name[-1])

        # Checks for the Employee Date of Birth data
        if row[2] != "DOB":

            # strptime function is for date conversion
            d = datetime.datetime.strptime(row[2], '%Y-%m-%d')

            # strftime function is to format the date (dd/mm/yy)
            db = d.strftime('%d/%m/%Y')
            DOB.append(db)
            print(DOB)

        # Checks for the Employee SSN data
        if row[3] != "SSN":

            ssn_hidden = row[3]

            # Replace first five digits as '*'
            hide = ssn_hidden.replace(ssn_hidden[0:6],"***-**")
            ssn.append(hide)

        # Checks for the State 
        if row[4] != "State":

            abb = row[4]

            # Looping for finding the key state from the dictionary
            for key,value in states.items():
                if abb in value:
                    state_abb.append(key) 
           
# Zip lists together
merge = zip(emp_id,fname,lname,DOB,ssn,state_abb)

# Set variable for output file
output_file = os.path.join("webfinal.csv")

#  Open the output file
with open(output_file, "w", newline="", encoding='utf-8') as datafile:
    writer = csv.writer(datafile)
    
    # Write the header row
    writer.writerow(["EMP ID","FIRST NAME","LAST NAME","DOB","SSN","STATE"])

    # Write in zipped rows
    writer.writerows(merge)
    







        
        

            

                
            








