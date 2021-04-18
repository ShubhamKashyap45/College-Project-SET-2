from tkinter import *

root = Tk()
root.geometry("800x700")
# root.maxsize(412, 717)
# root.minsize(412, 717)
root.title("Job Application")

def getvalue():
    print("\n")
    print("Personal Information")
    print("\n")

    print("Name:", name1_entry.get())
    print("Email:", email_entry.get())
    print("Education:", education_entry.get())
    print("Resume:", resume_entry.get())
    print("Address1:", Add1_entry.get())
    print("Address2:", Add2_entry.get())
    print("Country:", country_entry.get())
    print("City:", city_entry.get())
    print("State:", state_entry.get())
    print("Zip Code:", zipcode_entry.get())
    print("Phone Number:", number_entry.get())
    print("What are your hobbies?:", hobbies_entry.get())
    print("\n")
    print("Previous/Current Employmnet Details")
    print("\n")
    print("Company Name:", company_entry.get())
    print("Job Title:", Job_entry.get())
    print("How long were you here?:", HLWYH_entry.get())
    print("\n")
    print("Reference Name1:", r_name1_entry.get())
    print("Reference Phone1:", r_phone1_entry.get())
    print("\n")
    print("Reference Name2:", r_name2_entry.get())
    print("Reference Phone2:", r_phone2_entry.get())


    # Taking Job Application input from user in txt file

    with open("Job Application", "a") as f:
        f.write("\n")
        f.write("Personal Information")
        f.write("\n")

        f.write("\n")

        f.write("Name:\t")
        f.write(name1_entry.get())
        f.write("\n")

        f.write("Email:\t")
        f.write(email_entry.get())
        f.write("\n")

        f.write("Education:\t")
        f.write(education_entry.get())
        f.write("\n")

        f.write("Resume:\t")
        f.write(resume_entry.get())
        f.write("\n")

        f.write("Address 1:\t")
        f.write(Add1_entry.get())
        f.write("\n")

        f.write("Address 2:\t")
        f.write(Add2_entry.get())
        f.write("\n")

        f.write("Country:\t")
        f.write(country_entry.get())
        f.write("\n")

        f.write("City:\t")
        f.write(city_entry.get())
        f.write("\n")

        f.write("State:\t")
        f.write(state_entry.get())
        f.write("\n")

        f.write("Zip Code:\t")
        f.write(zipcode_entry.get())
        f.write("\n")

        f.write("What are your hobbies?:\t")
        f.write(hobbies_entry.get())
        f.write("\n")

        f.write("\n")

        f.write("Previous/Current Employment Details")
        f.write("\n")

        f.write("\n")

        f.write("Company Name:\t")
        f.write(company_entry.get())
        f.write("\n")

        f.write("Job Title:\t")
        f.write(Job_entry.get())
        f.write("\n")

        f.write("How long were you here?:\t")
        f.write(HLWYH_entry.get())
        f.write("\n")

        f.write("\n")

        f.write("Reference #1")
        f.write("\n")

        f.write("Name:\t")
        f.write(r_name1_entry.get())
        f.write("\n")

        f.write("Phone:\t")
        f.write(r_phone1_entry.get())
        f.write("\n")

        f.write("\n")

        f.write("Reference #2")
        f.write("\n")

        f.write("Name:\t")
        f.write(r_name2_entry.get())
        f.write("\n")

        f.write("Phone:\t")
        f.write(r_phone2_entry.get())
        f.write("\n")

        f.close()


# frame
frame = Frame(root)
frame.grid(row=16, column=0, sticky="ew", columnspan=4)


# Creating title
title_heading = Label(root,text="Job Application", font="lucida 15 bold")
title_heading.grid(row=0, column=1)

# Personal Information Heading
personal_info = Label(root, text="Personal Information", fg="red", font="lucida 10 bold")
personal_info.grid(sticky="w", row=1, column=0)

# 1st part Labels
name = Label(root,text="Name").grid(sticky="w", row=2,column=0)
email = Label(root, text="Email").grid(sticky="w", row=3,column=0)
education = Label(root, text="Education").grid(sticky="w", row=4,column=0)
resume = Label(root, text="Resume").grid(sticky="w", row=5,column=0)
adress = Label(root, text="Address").grid(sticky="w", row=6,column=0)
adress1 = Label(root, text="Address 1", font=" lucida 7 bold").grid(row=7,column=1)
adress2 = Label(root, text="Address 2", font=" lucida 7 bold").grid(row=9,column=1)
country = Label(root, text="Country", font=" lucida 7 bold").grid(row=11,column=1)
city = Label(root, text="City", font=" lucida 7 bold").grid(row=13, column=1)
state = Label(root, text="State", font=" lucida 7 bold").grid(row=13, column=2)
zip = Label(root, text="Zip Code", font=" lucida 7 bold").grid(row=13, column=3)
phnumber = Label(root, text="Phone Number").grid(sticky="w", pady=5, row=14,column=0)
hobbies = Label(root, text="What are your Hobbies?").grid(sticky="w", pady=5, row=15,column=0)


# 2nd part of the form

# Employment Details Heading
employment_details = Label(root, text="Previous/Current Employment Details", fg="red", font="lucida 10 bold")
employment_details.grid(sticky="w", pady=5, row=17, column=0)

# 2nd part Labels
company_name = Label(root,text="Company Name").grid(sticky="w", row=18,column=0)
job_title = Label(root,text="Job Title").grid(sticky="w", row=19,column=0)
HLWYH = Label(root,text="How long were you here?").grid(sticky="w", row=20,column=0)

# Reference #1
reference1 = Label(root, text="Reference #1", fg="red", font="lucida 10 bold")
reference1.grid(sticky="w", row=21, column=0)

r_name1 = Label(root,text="Name").grid(sticky="w", row=22,column=0)
r_phone1 = Label(root,text="Phone").grid(sticky="w", row=23,column=0)

# Reference #2
reference2 = Label(root, text="Reference #2", fg="red", font="lucida 10 bold")
reference2.grid(sticky="w", row=24, column=0)

r_name2 = Label(root,text="Name").grid(sticky="w", row=25,column=0)
r_phone2 = Label(root,text="Phone").grid(sticky="w", row=26,column=0)

# 1st part vars
name1_var = StringVar()
# name2_var = StringVar()
email_var = StringVar()
education_var = StringVar()
resume_var = StringVar()
Add1var = StringVar()
Add2var = StringVar()
country_var = StringVar()
city_var = StringVar()
state_var = StringVar()
zipcode_var = StringVar()
number_var = StringVar()
hobbies_var = StringVar()

# 2nd part vars
company_var = StringVar()
Job_var = StringVar()
HLWYH_var = StringVar()

r_name1_var = StringVar()
r_phone1_var = StringVar()

r_name2_var = StringVar()
r_phone2_var = StringVar()


# 1st part entry widgets
name1_entry = Entry(root, textvariable=name1_var)
name1_entry.grid(sticky="w", pady=2, row=2, column=1)
# name2_entry = Entry(root, textvariable=name2_var)
# name2_entry.grid(sticky="w", row=2, column=2)

email_entry = Entry(root, textvariable=email_var)
email_entry.grid(sticky="w", pady=2, row=3, column=1)

education_entry = Entry(root, textvariable=education_var)
education_entry.grid(sticky="w", pady=2, row=4, column=1)

resume_entry = Entry(root, textvariable=resume_var)
resume_entry.grid(sticky="w", pady=2, row=5, column=1)

Add1_entry = Entry(root, width=40, textvariable=Add1var)
Add1_entry.grid(sticky="w", pady=2, row=6, column=1)

Add2_entry = Entry(root, width=40, textvariable=Add2var)
Add2_entry.grid(sticky="w", pady=2, row=8, column=1)

country_entry = Entry(root, width=35, textvariable=country_var)
country_entry.grid(pady=2,sticky="w", row=10, column=1)

city_entry = Entry(root,width=35, textvariable=city_var)
city_entry.grid(pady=2, sticky="w", row=12, column=1)

state_entry = Entry(root, textvariable=state_var)
state_entry.grid(pady=2, row=12, column=2)

zipcode_entry = Entry(root, textvariable=zipcode_var)
zipcode_entry.grid(pady=2, padx=5, row=12, column=3)

number_entry = Entry(root, textvariable=number_var)
number_entry.grid(pady=2, sticky="w", row=14, column=1)

hobbies_entry = Entry(frame, width=130, textvariable=hobbies_var)
hobbies_entry.pack(side=LEFT)


# 2nd part entry widgets
company_entry = Entry(root, textvariable=company_var)
company_entry.grid(sticky="w", pady=2, row=18, column=1)

Job_entry = Entry(root, textvariable=Job_var)
Job_entry.grid(sticky="w", pady=2, row=19, column=1)

HLWYH_entry = Entry(root, textvariable=HLWYH_var)
HLWYH_entry.grid(sticky="w", pady=2, row=20, column=1)

r_name1_entry = Entry(root, textvariable=r_name1_var)
r_name1_entry.grid(sticky="w", pady=2, row=22, column=1)

r_phone1_entry = Entry(root, textvariable=r_phone1_var)
r_phone1_entry.grid(sticky="w", pady=2, row=23, column=1)

r_name2_entry = Entry(root, textvariable=r_name2_var)
r_name2_entry.grid(sticky="w", pady=2, row=25, column=1)

r_phone2_entry = Entry(root, textvariable=r_phone2_var)
r_phone2_entry.grid(sticky="w", pady=2, row=26, column=1)

apply_button = Button(root, text="Apply", padx=13, bg="black", fg="white", command=getvalue)
apply_button.grid(pady=15, row=27, column=1)


root.mainloop()