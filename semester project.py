from tkinter import *
from datetime import datetime
import random


window = Tk()
# making window
window.minsize(1600, 800)

entry1 = 0
entry2 = 0
entry3 = 0
seat = 0
I_seat = 0
entry_check = 0
admin_entry = 0


def admin_details():

    canvas = Canvas(width=1600, height=800, bg="#91D8E4")
    canvas.place(x=0, y=5)
    sby = Scrollbar(canvas)
    sby.place(x=1510, y=140)
    data_list = (Listbox(canvas, height=25, width=151, font="calibri 15", yscrollcommand=sby.set))
    data_list.place(x=0, y=140)
    sby.config(command=data_list.yview())

    f = open("flight user data.txt")
    f.seek(0)
    while 1:
        data = f.readline()
        data_list.insert(END, data + '\n')

        if not data:
            break
    f.close()
    canvas.create_text(250, 100, text="Passengers Record", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")

    main_page = Button(text="Esc", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=1300, y=80)


def admin_login():
    canvas = Canvas(width=500, height=400, bg="#F8EDE3")
    canvas.place(x=500, y=190)

    canvas.create_text(150, 60, text="Access to the platform:", font=(" Hermann Zapf's Optima", 18),
                       fill="black")

    canvas.create_text(70, 180, text="Password:1-8", font=(" Hermann Zapf's Optima", 12),
                       fill="black")

    def password_check():
        global admin_entry
        user_input = admin_entry.get()
        if user_input != "12345678":
            first_page()
        if user_input == "12345678":
            admin_details()

    global admin_entry
    admin_entry = Entry(window, width=30)
    admin_entry.place(x=650, y=355)

    details_button = Button(text="Login", font=("arial", 15), fg="white", bg="#3AB0FF", width=15,
                            command=password_check).place(x=650, y=480)

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)


##########################################################################################################################
# ************************************ MAIN CODE HERE

def first_page():
    # canvas Making
    canvas = Canvas(width=1600, height=800, bg="blue")
    canvas.place(x=0, y=5)

    # image on canvas
    desktop_image = PhotoImage(file="faded plane.png")
    canvas.create_image(800, 402, image=desktop_image)

    # welcome text
    canvas.create_text(250, 100, text="HAKUNA  MATATA", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")
    canvas.create_text(260, 145, text="AIRWAYS ௹", font=(" Hermann Zapf's Optima", 30, "bold"), fill="#282A3A")

    # asking for admin/user
    button1 = Button(text="   Administration  \n  Login  ", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF",
                     width=13, height=3, command=admin_login).place(x=1100, y=280)
    button2 = Button(text="   Passengers  \n  Booking  ", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF",
                     width=13, height=3, command=passenger_booking).place(x=1100, y=420)

    window.mainloop()


##########################################################################################################################
# **************************************  FAQ
def faq():
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)
    canvas1.create_text(780, 100, text="\"Frequently Asked Questions\"", font=(" Hermann Zapf's Optima", 40, "bold"),
                        fill="#EB455F")

    def que1():
        canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
        canvas1.place(x=0, y=5)
        data = open("q1.txt", "r")
        a = data.read()
        canvas1.create_text(600, 290, text=a, font=("Argent CF", 15), fill="white")
        data.close()
        back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                           command=faq
                           ).place(x=50, y=670)

    def que2():
        canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
        canvas1.place(x=0, y=5)
        data = open("q2.txt", "r")
        a = data.read()
        canvas1.create_text(600, 290, text=a, font=("Argent CF", 15), fill="white")
        data.close()
        back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                           command=faq
                           ).place(x=50, y=670)

    def que3():
        canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
        canvas1.place(x=0, y=5)
        data = open("q3.txt", "r")
        a = data.read()
        canvas1.create_text(600, 290, text=a, font=("Argent CF", 15), fill="white")
        data.close()
        back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                           command=faq
                           ).place(x=50, y=670)

    def que4():
        canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
        canvas1.place(x=0, y=5)
        data = open("q4.txt", "r")
        a = data.read()
        canvas1.create_text(600, 290, text=a, font=("Argent CF", 15), fill="white")
        data.close()
        back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                           command=faq
                           ).place(x=50, y=670)

    def que5():
        canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
        canvas1.place(x=0, y=5)
        data = open("q5.txt", "r")
        a = data.read()
        canvas1.create_text(600, 290, text=a, font=("Argent CF", 15), fill="white")
        data.close()
        back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                           command=faq
                           ).place(x=50, y=670)

    q1 = "Am I eligible to purchase and travel on an Extra Legroom seat?"
    q2 = "What is mobile boarding pass and how do i use it."
    q3 = "How can i obtain proof that my flight was cancelled."
    q4 = "What is online check-in? When and where can I use it?"
    q5 = "Can I Change my seat after i have paid for it."
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       ).place(x=50, y=670)
    question1 = Button(text=q1, font=("arial", 20, "bold"), fg="white", bg="#069A8E", width=70, height=1,
                       command=que1).place(x=210, y=190)

    question2 = Button(text=q2, font=("arial", 20, "bold"), fg="white", bg="#069A8E", width=70, height=1,
                       command=que2).place(x=210, y=290)

    question3 = Button(text=q3, font=("arial", 20, "bold"), fg="white", bg="#069A8E", width=70, height=1,
                       command=que3).place(x=210, y=390)

    question4 = Button(text=q4, font=("arial", 20, "bold"), fg="white", bg="#069A8E", width=70, height=1,
                       command=que4).place(x=210, y=490)

    question5 = Button(text=q5, font=("arial", 20, "bold"), fg="white", bg="#069A8E", width=70, height=1,
                       command=que5).place(x=210, y=590)

    back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=passenger_booking).place(
        x=1300, y=670)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)


########################################################################################################################

# **************************************About Us
def about_details():
    # canvas Making
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)
    # canvas1.create_text(700, 100, text="\n\n\t\tEmirates connects the world to, and through, our global hub\n in Dubai. We operate modern, efficient and comfortable\n aircraft, and our culturally diverse workforce delivers award-\nwinning services to our customers across six continents\n every day.", font=(" Hermann Zapf's Optima", 20, "bold"), fill="#9C254D")
    file = open("About Us.txt", "r")
    # print(file.read())
    a = file.read()
    canvas1.create_text(450, 250, text=a, font=("Argent CF", 30), fill="white")
    file.close()
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)
    back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=passenger_booking).place(
        x=50, y=600)


#######################################################################################################################

#**************************************  Flight Cancellation

def replace_line(file_name, line_num):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = "Cancelled - "+lines[line_num]
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def line_num_for_phrase_in_file(phrase="", filename='flight user data.txt'):
    global entry2
    phrase1 =str(entry2.get())
    print(phrase1)
    phrase=str(phrase1)
    print("response0: ", phrase)
    if phrase == "":
        return -1
    phrase += ", CNIC"
    lines = []
    flag = True
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if phrase in line:
                print("found at line: ",i)
                if (line[0:9] != "Cancelled"):
                    flag = False
                    print("replace: ",i)
                    replace_line(filename,i)
                    lines.append(line)

    if flag:
        return -1
    else:
        return lines


def flight_cancellation():
    # canvas Making
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)
    # main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
    #                    command=first_page).place(
    #     x=50, y=670)
    print("this is logging")
    response = line_num_for_phrase_in_file()
    print("response: ", response)
    if (response==-1):
        canvas1.create_text(700, 100, text="\n\n\t\tYou dont have any bookings to cancel.", font=(" Hermann Zapf's Optima", 20, "bold"), fill="#9C254D")
    else:
        text = "Bookings Cancelled: \n"
        for line in response:
            text += line + "\n"
        canvas1.create_text(700, 100, text=text, font=(" Hermann Zapf's Optima", 10, "bold"), fill="#9C254D")


def flight_cancel_screen():
    # canvas Making
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)

    canvas = Canvas(width=500, height=400, bg="#F8EDE3")
    canvas.place(x=500, y=190)

    canvas.create_text(150, 60, text="Access to the platform:", font=(" Hermann Zapf's Optima", 18),
                       fill="black")

    canvas.create_text(70, 180, text="Passport No:", font=(" Hermann Zapf's Optima", 12),
                       fill="black")
    global entry2
    entry2 = Entry(window, width=30)
    entry2.place(x=650, y=355)

    details_button = Button(text="Check Details", font=("arial", 15), fg="white", bg="#3AB0FF", width=15,
                            command=flight_cancellation).place(x=650, y=480)


#######################################################################################################################
def flight_deatils_reciept():
    global entry_check
    entry = entry_check.get()
    with open('flight user data.txt') as file:
        for line in file:
            b = line
            passport = b
            start = passport.find('Passport') + 9
            end = passport.find('CNIC', start) - 2
            r_passport = passport[start:end]
            if (entry == r_passport):
                data = r_passport
                a = b
        file.close()
    print(a)
    plane = a
    start = plane.find('Plane') + 6
    end = plane.find('Flight') - 2
    r_plane = plane[start:end]
    print(r_plane)
    if (r_plane == "Private Jet"):
        name = a
        start = name.find('Name') + 5
        end = name.find('Passport', start) - 2
        r_name = name[start:end]

        passport = a
        start = passport.find('Passport') + 9
        end = passport.find('CNIC', start) - 2
        r_passport = passport[start:end]

        cnic = a
        start = cnic.find('CNIC') + 5
        end = cnic.find('Plane') - 2
        r_cnic = cnic[start:end]

        plane = a
        start = plane.find('Plane') + 6
        end = plane.find('Flight') - 2
        r_plane = plane[start:end]

        flight = a
        start = flight.find('Flight') + 7
        end = flight.find('Departure') - 2
        r_flight = flight[start:end]

        departure = a
        start = departure.find('Departure') + 10
        end = departure.find('Arrival') - 2
        r_departure = departure[start:end]

        arrival = a
        start = arrival.find('Arrival') + 8
        end = arrival.find('Date') - 2
        r_arrival = arrival[start:end]

        date = a
        start = date.find('Date') + 5
        end = date.find('/20') + 5
        r_date = date[start:end]

        canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
        canvas1.place(x=0, y=5)
        canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"),
                            fill="#9C254D")
        canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
        canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
        canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
        canvas1.create_text(200, 335, text=(f"Plane: {r_plane}"), font=("Neue ", 18))
        canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
        canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
        canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
        canvas1.create_text(720, 470, text=(f"Category: Bizliners"), font=("Neue ", 18))
        canvas1.create_text(1170, 470, text=(f"Price: 2,000,000/-Rs"), font=("Neue ", 18))
        canvas1.create_text(720, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
        canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                            fill="#FF9F29")
    if (r_plane == " AirBus"):
        name = a
        start = name.find('Name') + 5
        end = name.find('Passport', start) - 2
        r_name = name[start:end]

        passport = a
        start = passport.find('Passport') + 9
        end = passport.find('CNIC', start) - 2
        r_passport = passport[start:end]

        cnic = a
        start = cnic.find('CNIC') + 5
        end = cnic.find('Plane') - 2
        r_cnic = cnic[start:end]

        plane = a
        start = plane.find('Plane') + 6
        end = plane.find('Flight') - 2
        r_palne = plane[start:end]

        flight = a
        start = flight.find('Flight') + 7
        end = flight.find('Departure') - 2
        r_flight = flight[start:end]

        departure = a
        start = departure.find('Departure') + 10
        end = departure.find('Arrival') - 2
        r_departure = departure[start:end]

        arrival = a
        start = arrival.find('Arrival') + 8
        end = arrival.find('Category') - 2
        r_arrival = arrival[start:end]

        category = a
        start = category.find('Category') + 9
        end = category.find('Seat') - 2
        r_category = category[start:end]

        seat_num = a
        start = seat_num.find('Seat') + 8
        end = seat_num.find('Date') - 2
        r_seat_num = seat_num[start:end]

        date = a
        start = date.find('Date') + 5
        end = date.find('/20') + 5
        r_date = date[start:end]

        canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
        canvas1.place(x=0, y=5)
        canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"),
                            fill="#9C254D")
        canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
        canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
        canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
        canvas1.create_text(200, 335, text=(f"Plane: {r_palne}"), font=("Neue ", 18))
        canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
        canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
        canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
        canvas1.create_text(720, 470, text=(f"Category: {r_category}"), font=("Neue ", 18))
        canvas1.create_text(1170, 470, text=(f"Seat no:{r_seat_num}"), font=("Neue ", 18))
        canvas1.create_text(400, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
        canvas1.create_text(980, 580, text=(f"Price: 20,000/-Rs"), font=("Neue ", 18))
        canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                            fill="#FF9F29")

    if (r_plane == "Cargo"):
        name = a
        start = name.find('Name') + 5
        end = name.find('Passport', start) - 2
        r_name = name[start:end]

        passport = a
        start = passport.find('Passport') + 9
        end = passport.find('CNIC', start) - 2
        r_passport = passport[start:end]

        cnic = a
        start = cnic.find('CNIC') + 5
        end = cnic.find('Plane') - 2
        r_cnic = cnic[start:end]

        plane = a
        start = plane.find('Plane') + 6
        end = plane.find('Flight') - 2
        r_palne = plane[start:end]

        flight = a
        start = flight.find('Flight') + 7
        end = flight.find('Departure') - 2
        r_flight = flight[start:end]

        departure = a
        start = departure.find('Departure') + 10
        end = departure.find('Arrival') - 2
        r_departure = departure[start:end]

        arrival = a
        start = arrival.find('Arrival') + 8
        end = arrival.find('Date') - 2
        r_arrival = arrival[start:end]

        date = a
        start = date.find('Date') + 5
        end = date.find('/20') + 5
        r_date = date[start:end]

        canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
        canvas1.place(x=0, y=5)
        canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"),
                            fill="#9C254D")
        canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
        canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
        canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
        canvas1.create_text(200, 335, text=(f"Plane: {r_palne}"), font=("Neue ", 18))
        canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
        canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
        canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
        canvas1.create_text(720, 470, text=(f"Category: Beoing 737"), font=("Neue ", 18))
        canvas1.create_text(1170, 470, text=(f"Ticket Price:150,000/-Rs"), font=("Neue ", 18))
        canvas1.create_text(720, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
        canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                            fill="#FF9F29")
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(x=50, y=670)


# **************************************  Flight Details
def flight_details():
    # canvas Making
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)

    canvas = Canvas(width=500, height=400, bg="#F8EDE3")
    canvas.place(x=500, y=190)

    canvas.create_text(150, 60, text="Access to the platform:", font=(" Hermann Zapf's Optima", 18),
                       fill="black")

    canvas.create_text(70, 180, text="Passport No:", font=(" Hermann Zapf's Optima", 12),
                       fill="black")
    global entry_check
    entry_check = Entry(window, width=30)
    entry_check.place(x=650, y=355)

    details_button = Button(text="Check Details", font=("arial", 15), fg="white", bg="#3AB0FF", width=15,
                            command=flight_deatils_reciept).place(x=650, y=480)

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)

    back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=passenger_booking).place(
        x=50, y=600)


##########################################################################################################################
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Private Plane %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# *********************************** Private Jet RECIEPT GENERATION *********************************************
def private_jet_reciept():
    with open('flight user data.txt') as f:
        for line in f:
            pass
        last_line = line
        f.close()
    a = last_line
    print(a)

    name = a
    start = name.find('Name') + 5
    end = name.find('Passport', start) - 2
    r_name = name[start:end]

    passport = a
    start = passport.find('Passport') + 9
    end = passport.find('CNIC', start) - 2
    r_passport = passport[start:end]

    cnic = a
    start = cnic.find('CNIC') + 5
    end = cnic.find('Plane') - 2
    r_cnic = cnic[start:end]

    plane = a
    start = plane.find('Plane') + 6
    end = plane.find('Flight') - 2
    r_plane = plane[start:end]

    flight = a
    start = flight.find('Flight') + 7
    end = flight.find('Departure') - 2
    r_flight = flight[start:end]

    departure = a
    start = departure.find('Departure') + 10
    end = departure.find('Arrival') - 2
    r_departure = departure[start:end]

    arrival = a
    start = arrival.find('Arrival') + 8
    end = arrival.find('Date') - 2
    r_arrival = arrival[start:end]

    # category=a
    # start=category.find('Category')+9
    # end=category.find('Seat')-2
    # r_category=category[start:end]

    # seat_num=a
    # start=seat_num.find('Seat')+8
    # end=seat_num.find('Date')-2
    # r_seat_num=seat_num[start:end]

    date = a
    start = date.find('Date') + 5
    end = date.find('/20') + 5
    r_date = date[start:end]

    canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
    canvas1.place(x=0, y=5)
    canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")
    canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
    canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
    canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
    canvas1.create_text(200, 335, text=(f"Plane: {r_plane}"), font=("Neue ", 18))
    canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
    canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
    canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
    canvas1.create_text(720, 470, text=(f"Category: Bizliners"), font=("Neue ", 18))
    canvas1.create_text(1170, 470, text=(f"Price: 2,000,000/-Rs"), font=("Neue ", 18))
    canvas1.create_text(720, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
    canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                        fill="#FF9F29")
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)
    full_data = (f"{r_name},{r_passport},{r_cnic},{r_plane},{r_flight},{r_departure},{r_arrival},N/A,N/A,{r_date}\n")
    with open("all data.csv", "a") as data:
        data.write(full_data)


# ********************************** Private International Time Slot Selection *************************************
def private_international_date_time():
    current_time = datetime.now()
    year = current_time.year
    date = current_time.day
    month = current_time.month

    date1 = date
    date2 = date + 2
    date3 = date + 5
    month1 = month
    month2 = month
    month3 = month
    year1 = year
    year2 = year
    year3 = year

    if date1 > 31 and month1 == 12:
        year1 += 1
    if date2 > 31 and month2 == 12:
        year2 += 1
    if date3 > 31 and month3 == 12:
        year3 += 1

    if month in (1, 3, 5, 7, 8, 10):
        if date1 > 31: month1 = month + 1
        if date2 > 31: month2 = month + 1
        if date3 > 31: month3 = month + 1
    if month == 2:
        if date1 > 28: month1 = month + 1
        if date2 > 28: month2 = month + 1
        if date3 > 28: month3 = month + 1
    if month in (4, 6, 9, 11):
        if date1 > 30: month1 = month + 1
        if date2 > 30: month2 = month + 1
        if date3 > 30: month3 = month + 1
    if month == 12:
        if date1 > 31: month1 = 1
        if date2 > 31: month2 = 1
        if date3 > 31: month3 = 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (date1 > 31): date1 = date1 - 31
        if (date2 > 31): date2 = date2 - 31
        if (date3 > 31): date3 = date3 - 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        if (date1 > 30): date1 = date1 - 30
        if (date2 > 30): date2 = date2 - 30
        if (date3 > 30): date3 = date3 - 30
    if month == 2:
        if (date1 > 28): date1 = date1 - 28
        if (date2 > 28): date2 = date2 - 28
        if (date3 > 28): date3 = date3 - 28

    date1_window = (f"{date1}/{month1}/{year1}")
    date2_window = (f"{date2}/{month2}/{year2}")
    date3_window = (f"{date3}/{month3}/{year3}")

    def time_selection(x):
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write(f"Date:{date1_window} \n")
            data.close()
        if x == 2:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date2_window} \n")
            data.close()
        if x == 3:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date3_window} \n")
            data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 150, text="Select the time slot:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")
    # buttons on canvas

    slot1 = Button(text=date1_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(1), private_jet_reciept()]).place(x=500, y=300)

    slot2 = Button(text=date2_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(2), private_jet_reciept()]).place(x=500, y=400)

    slot3 = Button(text=date3_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(3), private_jet_reciept()]).place(x=500,
                                                                                     y=500)


# ********************************** Private Jet Internalional Flights Destination*****************************
def private_international_flights_destination():
    data = open("flight user data.txt", "a")
    data.write("Arrival: ")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="ARRIVAL:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), private_international_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), private_international_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), private_international_date_time()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), private_international_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), private_international_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), private_international_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), private_international_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), private_international_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), private_international_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Internalional Flights Departure*****************************
def private_international_flights_departure():
    data = open("flight user data.txt", "a")
    data.write("Flight: International, Departure:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), private_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), private_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), private_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), private_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), private_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), private_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), private_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), private_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), private_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Private Jet Domestic Time Slot Selection *************************************
def private_domestic_date_time():
    current_time = datetime.now()
    year = current_time.year
    date = current_time.day
    month = current_time.month

    date1 = date + 1
    date2 = date + 2
    date3 = date + 3
    month1 = month
    month2 = month
    month3 = month
    year1 = year
    year2 = year
    year3 = year

    if date1 > 31 and month1 == 12:
        year1 += 1
    if date2 > 31 and month2 == 12:
        year2 += 1
    if date3 > 31 and month3 == 12:
        year3 += 1

    if month in (1, 3, 5, 7, 8, 10):
        if date1 > 31: month1 = month + 1
        if date2 > 31: month2 = month + 1
        if date3 > 31: month3 = month + 1
    if month == 2:
        if date1 > 28: month1 = month + 1
        if date2 > 28: month2 = month + 1
        if date3 > 28: month3 = month + 1
    if month in (4, 6, 9, 11):
        if date1 > 30: month1 = month + 1
        if date2 > 30: month2 = month + 1
        if date3 > 30: month3 = month + 1
    if month == 12:
        if date1 > 31: month1 = 1
        if date2 > 31: month2 = 1
        if date3 > 31: month3 = 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (date1 > 31): date1 = date1 - 31
        if (date2 > 31): date2 = date2 - 31
        if (date3 > 31): date3 = date3 - 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        if (date1 > 30): date1 = date1 - 30
        if (date2 > 30): date2 = date2 - 30
        if (date3 > 30): date3 = date3 - 30
    if month == 2:
        if (date1 > 28): date1 = date1 - 28
        if (date2 > 28): date2 = date2 - 28
        if (date3 > 28): date3 = date3 - 28

    date1_window = (f"{date1}/{month1}/{year1}")
    date2_window = (f"{date2}/{month2}/{year2}")
    date3_window = (f"{date3}/{month3}/{year3}")

    def time_selection(x):
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date1_window}")
            data.close()
        if x == 2:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date2_window}")
            data.close()
        if x == 3:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date3_window}")
            data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 150, text="Select the time slot:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")
    # buttons on canvas

    slot1 = Button(text=date1_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(1), private_jet_reciept()]).place(x=500, y=300)

    slot2 = Button(text=date2_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(2), private_jet_reciept()]).place(x=500, y=400)

    slot3 = Button(text=date3_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(3), private_jet_reciept()]).place(x=500,
                                                                                     y=500)


# ********************************** Private Jet Domestic Flights Destination*****************************
def private_domestic_flights_destination():
    data = open("flight user data.txt", "a")
    data.write("Arrival: ")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DESTINATION:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")
    # buttons on canvas

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "Lahore", 2: "Karachi", 3: "Islamabad", 4: "Peshawar", 5: "Sailkot", 6: "Hyderabad", 7: "Sakardu",
            8: "Quetta", 9: "Multan"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), private_domestic_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), private_domestic_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), private_domestic_date_time()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), private_domestic_date_time()]).place(x=a2, y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), private_domestic_date_time()]).place(x=a2, y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), private_domestic_date_time()]).place(x=a2, y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), private_domestic_date_time()]).place(x=a3,
                                                                                                         y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), private_domestic_date_time()]).place(x=a3,
                                                                                                         y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), private_domestic_date_time()]).place(x=a3,
                                                                                                         y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Private Jet Domestic Flights Departure *****************************
def private_domestic_flights_departure():
    data = open("flight user data.txt", "a")
    data.write("Flight: Domestic, Departure:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    # buttons on canvas

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "Lahore", 2: "Karachi", 3: "Islamabad", 4: "Peshawar", 5: "Sailkot", 6: "Hyderabad", 7: "Sakardu",
            8: "Quetta", 9: "Multan"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), private_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), private_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), private_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), private_domestic_flights_destination()]).place(x=a2,
                                                                                                                 y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), private_domestic_flights_destination()]).place(x=a2,
                                                                                                                 y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), private_domestic_flights_destination()]).place(x=a2,
                                                                                                                 y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), private_domestic_flights_destination()]).place(x=a3,
                                                                                                                   y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), private_domestic_flights_destination()]).place(x=a3,
                                                                                                                   y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), private_domestic_flights_destination()]).place(x=a3,
                                                                                                                   y=b + 300)
            a3 += 400

        main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                           , command=first_page).place(
            x=50, y=670)


# ********************************* Flight Nature ************************************
def private_jet_flights_nature():
    data = open("flight user data.txt", "a")
    data.write("Plane:Private Jet, ")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 190, text="Which type of flight you want to have:",
                       font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")

    international = Button(text="International Flights", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF",
                           width=17,
                           height=1, command=private_international_flights_departure).place(x=340, y=370)

    domestic = Button(text="Domestic Flights", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=17, height=1
                      , command=private_domestic_flights_departure).place(
        x=880, y=370)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Private Plane %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Cargo Plane %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# *********************************** Cargo RECIEPT GENERATION *********************************************

def cargo_reciept():
    with open('flight user data.txt') as file:
        for line in file:
            last_line = line
            b = last_line
        file.close()
    a = b
    print(a)

    name = a
    start = name.find('Name') + 5
    end = name.find('Passport', start) - 2
    r_name = name[start:end]

    passport = a
    start = passport.find('Passport') + 9
    end = passport.find('CNIC', start) - 2
    r_passport = passport[start:end]

    cnic = a
    start = cnic.find('CNIC') + 5
    end = cnic.find('Plane') - 2
    r_cnic = cnic[start:end]

    plane = a
    start = plane.find('Plane') + 6
    end = plane.find('Flight') - 2
    r_plane = plane[start:end]

    flight = a
    start = flight.find('Flight') + 7
    end = flight.find('Departure') - 2
    r_flight = flight[start:end]

    departure = a
    start = departure.find('Departure') + 10
    end = departure.find('Arrival') - 2
    r_departure = departure[start:end]

    arrival = a
    start = arrival.find('Arrival') + 8
    end = arrival.find('Date') - 2
    r_arrival = arrival[start:end]

    date = a
    start = date.find('Date') + 5
    end = date.find('/20') + 5
    r_date = date[start:end]

    canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
    canvas1.place(x=0, y=5)
    canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")
    canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
    canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
    canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
    canvas1.create_text(200, 335, text=(f"Plane: {r_plane}"), font=("Neue ", 18))
    canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
    canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
    canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
    canvas1.create_text(720, 470, text=(f"Category: Beoing 737"), font=("Neue ", 18))
    canvas1.create_text(1170, 470, text=(f"Ticket Price:150,000/-Rs"), font=("Neue ", 18))
    canvas1.create_text(720, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
    canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                        fill="#FF9F29")
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)
    full_data = (f"{r_name},{r_passport},{r_cnic},{r_plane},{r_flight},{r_departure},{r_arrival},N/A,N/A,{r_date}\n")
    with open("all data.csv", "a") as data:
        data.write(full_data)


# ****************************************** Cargo Date and Time ********************************
def cargo_date_time():
    current_time = datetime.now()
    year = current_time.year
    date = current_time.day
    month = current_time.month

    date1 = date + 10
    date2 = date + 15
    date3 = date + 18
    month1 = month
    month2 = month
    month3 = month
    year1 = year
    year2 = year
    year3 = year

    if date1 > 31 and month1 == 12:
        year1 += 1
    if date2 > 31 and month2 == 12:
        year2 += 1
    if date3 > 31 and month3 == 12:
        year3 += 1

    if month in (1, 3, 5, 7, 8, 10):
        if date1 > 31: month1 = month + 1
        if date2 > 31: month2 = month + 1
        if date3 > 31: month3 = month + 1
    if month == 2:
        if date1 > 28: month1 = month + 1
        if date2 > 28: month2 = month + 1
        if date3 > 28: month3 = month + 1
    if month in (4, 6, 9, 11):
        if date1 > 30: month1 = month + 1
        if date2 > 30: month2 = month + 1
        if date3 > 30: month3 = month + 1
    if month == 12:
        if date1 > 31: month1 = 1
        if date2 > 31: month2 = 1
        if date3 > 31: month3 = 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (date1 > 31): date1 = date1 - 31
        if (date2 > 31): date2 = date2 - 31
        if (date3 > 31): date3 = date3 - 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        if (date1 > 30): date1 = date1 - 30
        if (date2 > 30): date2 = date2 - 30
        if (date3 > 30): date3 = date3 - 30
    if month == 2:
        if (date1 > 28): date1 = date1 - 28
        if (date2 > 28): date2 = date2 - 28
        if (date3 > 28): date3 = date3 - 28

    date1_window = (f"{date1}/{month1}/{year1}")
    date2_window = (f"{date2}/{month2}/{year2}")
    date3_window = (f"{date3}/{month3}/{year3}")

    def time_selection(x):
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date1_window}")
            data.close()
        if x == 2:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date2_window}")
            data.close()
        if x == 3:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date3_window}")
            data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 150, text="Select the time slot:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")
    # buttons on canvas

    slot1 = Button(text=date1_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(1), cargo_reciept()]).place(x=500, y=300)

    slot2 = Button(text=date2_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(2), cargo_reciept()]).place(x=500, y=400)

    slot3 = Button(text=date3_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(3), cargo_reciept()]).place(x=500,
                                                                               y=500)


# ********************************** Cargo Internalional Flights Destination*****************************
def cargo_international_flights_destination():
    data = open("flight user data.txt", "a")
    data.write("Arrival:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="ARRIVAL:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), cargo_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), cargo_date_time()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), cargo_date_time()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), cargo_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), cargo_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), cargo_date_time()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), cargo_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), cargo_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), cargo_date_time()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Cargo Internalional Flights Departure*****************************
def cargo_international_flight_departure():
    data = open("flight user data.txt", "a")
    data.write("Plane:Cargo, Flight:International, Departure:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f"{x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), cargo_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), cargo_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), cargo_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), cargo_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), cargo_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), cargo_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), cargo_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), cargo_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), cargo_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Cargo Plane %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% AIR BUS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# *********************************** AIR BUS RECIEPT GENERATION *********************************************
def airbus_reciept():
    with open('flight user data.txt') as f:
        for line in f:
            pass
        last_line = line
        f.close()
    a = last_line
    print(a)

    name = a
    start = name.find('Name') + 5
    end = name.find('Passport', start) - 2
    r_name = name[start:end]

    passport = a
    start = passport.find('Passport') + 9
    end = passport.find('CNIC', start) - 2
    r_passport = passport[start:end]

    cnic = a
    start = cnic.find('CNIC') + 5
    end = cnic.find('Plane') - 2
    r_cnic = cnic[start:end]

    plane = a
    start = plane.find('Plane') + 6
    end = plane.find('Flight') - 2
    r_plane = plane[start:end]

    flight = a
    start = flight.find('Flight') + 7
    end = flight.find('Departure') - 2
    r_flight = flight[start:end]

    departure = a
    start = departure.find('Departure') + 10
    end = departure.find('Arrival') - 2
    r_departure = departure[start:end]

    arrival = a
    start = arrival.find('Arrival') + 8
    end = arrival.find('Category') - 2
    r_arrival = arrival[start:end]

    category = a
    start = category.find('Category') + 9
    end = category.find('Seat') - 2
    r_category = category[start:end]

    seat_num = a
    start = seat_num.find('Seat') + 8
    end = seat_num.find('Date') - 2
    r_seat_num = seat_num[start:end]

    date = a
    start = date.find('Date') + 5
    end = date.find('/20') + 5
    r_date = date[start:end]

    canvas1 = Canvas(width=1600, height=800, bg="#82C3EC")
    canvas1.place(x=0, y=5)
    canvas1.create_text(750, 80, text="Booking Receipt", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")
    canvas1.create_text(230, 200, text=(f"Name: {r_name}"), font=("Neue ", 18))
    canvas1.create_text(730, 200, text=(f"Passport: {r_passport}"), font=("Neue ", 18))
    canvas1.create_text(1230, 200, text=(f"CNIC: {r_cnic}"), font=("Neue ", 18))
    canvas1.create_text(200, 335, text=(f"Plane: {r_plane}"), font=("Neue ", 18))
    canvas1.create_text(710, 335, text=(f"Flight: {r_flight}"), font=("Neue ", 18))
    canvas1.create_text(1220, 335, text=(f"Departure: {r_departure}"), font=("Neue ", 18))
    canvas1.create_text(200, 470, text=(f"Arrival: {r_arrival}"), font=("Neue ", 18))
    canvas1.create_text(720, 470, text=(f"Category: {r_category}"), font=("Neue ", 18))
    canvas1.create_text(1170, 470, text=(f"Seat no:{r_seat_num}"), font=("Neue ", 18))
    canvas1.create_text(400, 580, text=(f"Date:{r_date}"), font=("Neue ", 18))
    canvas1.create_text(980, 580, text=(f"Price: 20,000/-Rs"), font=("Neue ", 18))
    canvas1.create_text(750, 660, text="Booking Confirmed ✅", font=(" Hermann Zapf's Optima", 20, "bold"),
                        fill="#FF9F29")
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=first_page).place(
        x=50, y=670)
    full_data = (
        f"{r_name},{r_passport},{r_cnic},{r_plane},{r_flight},{r_departure},{r_arrival},{r_category},{r_seat_num},{r_date}\n")
    with open("all data.csv", "a") as data:
        data.write(full_data)


# ********************************** Airbus International Time Slot Selection *************************************
def airbus_international_date_time():
    current_time = datetime.now()
    year = current_time.year
    date = current_time.day
    month = current_time.month

    date1 = date + 7
    date2 = date + 10
    date3 = date + 16
    month1 = month
    month2 = month
    month3 = month
    year1 = year
    year2 = year
    year3 = year

    if date1 > 31 and month1 == 12:
        year1 += 1
    if date2 > 31 and month2 == 12:
        year2 += 1
    if date3 > 31 and month3 == 12:
        year3 += 1

    if month in (1, 3, 5, 7, 8, 10):
        if date1 > 31: month1 = month + 1
        if date2 > 31: month2 = month + 1
        if date3 > 31: month3 = month + 1
    if month == 2:
        if date1 > 28: month1 = month + 1
        if date2 > 28: month2 = month + 1
        if date3 > 28: month3 = month + 1
    if month in (4, 6, 9, 11):
        if date1 > 30: month1 = month + 1
        if date2 > 30: month2 = month + 1
        if date3 > 30: month3 = month + 1
    if month == 12:
        if date1 > 31: month1 = 1
        if date2 > 31: month2 = 1
        if date3 > 31: month3 = 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (date1 > 31): date1 = date1 - 31
        if (date2 > 31): date2 = date2 - 31
        if (date3 > 31): date3 = date3 - 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        if (date1 > 30): date1 = date1 - 30
        if (date2 > 30): date2 = date2 - 30
        if (date3 > 30): date3 = date3 - 30
    if month == 2:
        if (date1 > 28): date1 = date1 - 28
        if (date2 > 28): date2 = date2 - 28
        if (date3 > 28): date3 = date3 - 28

    date1_window = (f"{date1}/{month1}/{year1}")
    date2_window = (f"{date2}/{month2}/{year2}")
    date3_window = (f"{date3}/{month3}/{year3}")

    def time_selection(x):
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date1_window}")
            data.close()
        if x == 2:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date2_window}")
            data.close()
        if x == 3:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date3_window}")
            data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 150, text="Select the time slot:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")
    # buttons on canvas

    slot1 = Button(text=date1_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(1), airbus_reciept()]).place(x=500, y=300)

    slot2 = Button(text=date2_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(2), airbus_reciept()]).place(x=500, y=400)

    slot3 = Button(text=date3_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(3), airbus_reciept()]).place(x=500,
                                                                                y=500)


# ********************************** Air Bus International Class Booking ***********************************
def airbus_international_class_booking():
    def class_slection(x):
        def seat_no_generation(y):
            seat = random.randint(1, y + 1)
            data = open("flight user data.txt", "a")
            data.write(f"{seat}, ")
            data.close()

        if x == 3:
            data = open("flight user data.txt", "a")
            data.write("Category: Economy Class, Seat no:E-")
            data.close()
            seat_no_generation(30)

        if x == 2:
            data = open("flight user data.txt", "a")
            data.write("Category: Business Class, Seat no:B-")
            data.close()
            seat_no_generation(16)
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write("Category: First Class, Seat no:A-")
            data.close()
            seat_no_generation(9)

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 190, text="Class For Your Travelling:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")

    first_class = Button(text="First Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                         height=1, command=lambda: [airbus_international_date_time(), class_slection(1)]).place(x=280,
                                                                                                                y=330)
    business_class = Button(text="Business Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                            height=1, command=lambda: [airbus_international_date_time(), class_slection(2)]).place(
        x=680, y=330)
    economy_class = Button(text="Economy Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                           height=1, command=lambda: [airbus_international_date_time(), class_slection(3)]).place(
        x=1100, y=330)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Internalional Flights Destination*****************************
def airbus_international_flights_destination():
    data = open("flight user data.txt", "a")
    data.write("Arrival:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="ARRIVAL:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f" {x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), airbus_international_class_booking()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), airbus_international_class_booking()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), airbus_international_class_booking()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), airbus_international_class_booking()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), airbus_international_class_booking()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), airbus_international_class_booking()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), airbus_international_class_booking()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), airbus_international_class_booking()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), airbus_international_class_booking()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Internalional Flights Departure*****************************
def airbus_international_flights_departure():
    data = open("flight user data.txt", "a")
    data.write(" Flight: International, Departure:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f" {x}, ")
        data.close()

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "London", 2: "Dubai", 3: "Paris", 4: "Baku", 5: "Islamabad", 6: "New York", 7: "Qatar", 8: "Frankfurt",
            9: "Melbourne"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), airbus_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), airbus_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), airbus_international_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), airbus_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), airbus_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), airbus_international_flights_destination()]).place(
                x=a2,
                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), airbus_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), airbus_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), airbus_international_flights_destination()]).place(
                x=a3,
                y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Airbus Domestic Time Slot Selection *************************************
def airbus_domestic_date_time():
    current_time = datetime.now()
    year = current_time.year
    date = current_time.day
    month = current_time.month

    date1 = date + 1
    date2 = date + 3
    date3 = date + 5
    month1 = month
    month2 = month
    month3 = month
    year1 = year
    year2 = year
    year3 = year

    if date1 > 31 and month1 == 12:
        year1 += 1
    if date2 > 31 and month2 == 12:
        year2 += 1
    if date3 > 31 and month3 == 12:
        year3 += 1

    if month in (1, 3, 5, 7, 8, 10):
        if date1 > 31: month1 = month + 1
        if date2 > 31: month2 = month + 1
        if date3 > 31: month3 = month + 1
    if month == 2:
        if date1 > 28: month1 = month + 1
        if date2 > 28: month2 = month + 1
        if date3 > 28: month3 = month + 1
    if month in (4, 6, 9, 11):
        if date1 > 30: month1 = month + 1
        if date2 > 30: month2 = month + 1
        if date3 > 30: month3 = month + 1
    if month == 12:
        if date1 > 31: month1 = 1
        if date2 > 31: month2 = 1
        if date3 > 31: month3 = 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if (date1 > 31): date1 = date1 - 31
        if (date2 > 31): date2 = date2 - 31
        if (date3 > 31): date3 = date3 - 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        if (date1 > 30): date1 = date1 - 30
        if (date2 > 30): date2 = date2 - 30
        if (date3 > 30): date3 = date3 - 30
    if month == 2:
        if (date1 > 28): date1 = date1 - 28
        if (date2 > 28): date2 = date2 - 28
        if (date3 > 28): date3 = date3 - 28

    date1_window = (f"{date1}/{month1}/{year1}")
    date2_window = (f"{date2}/{month2}/{year2}")
    date3_window = (f"{date3}/{month3}/{year3}")

    def time_selection(x):
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write(f"Date:{date1_window}\n")
            data.close()
        if x == 2:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date2_window}\n")
            data.close()
        if x == 3:
            data = open("flight user data.txt", "a")
            data.write(f"Date: {date3_window}\n")
            data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 150, text="Select the time slot:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")
    # buttons on canvas

    slot1 = Button(text=date1_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(1), airbus_reciept()]).place(x=500, y=300)

    slot2 = Button(text=date2_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(2), airbus_reciept()]).place(x=500, y=400)

    slot3 = Button(text=date3_window, font="arial", fg="yellow", bg="#68B984", height=2, width=45,
                   command=lambda: [time_selection(3), airbus_reciept()]).place(x=500,
                                                                                y=500)


# ********************************** Air Bus Domestic Class Booking ***********************************
def airbus_domestic_class_booking():
    def class_slection(x):
        def seat_no_generation(y):
            seat = random.randint(1, y + 1)
            data = open("flight user data.txt", "a")
            data.write(f"{seat}, ")
            data.close()

        if x == 3:
            data = open("flight user data.txt", "a")
            data.write("Category: Economy Class, Seat no:E-")
            data.close()
            seat_no_generation(30)

        if x == 2:
            data = open("flight user data.txt", "a")
            data.write("Category: Business Class, Seat no:B-")
            data.close()
            seat_no_generation(16)
        if x == 1:
            data = open("flight user data.txt", "a")
            data.write("Category: First Class, Seat no:A-")
            data.close()
            seat_no_generation(9)

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 190, text="Class For Your Travelling:", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")

    first_class = Button(text="First Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                         height=1, command=lambda: [airbus_domestic_date_time(), class_slection(1)]).place(x=280, y=330)
    business_class = Button(text="Business Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                            height=1, command=lambda: [airbus_domestic_date_time(), class_slection(2)]).place(x=680,
                                                                                                              y=330)
    economy_class = Button(text="Economy Class", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                           height=1, command=lambda: [airbus_domestic_date_time(), class_slection(3)]).place(x=1100,
                                                                                                             y=330)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Domestic Flights Destination*****************************
def airbus_domestic_flights_destination():
    data = open("flight user data.txt", "a")
    data.write("Arrival:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)


    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f" {x}, ")
        data.close()

    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="ARRIVAL:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")
    # buttons on canvas

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "Lahore", 2: "Karachi", 3: "Islamabad", 4: "Peshawar", 5: "Sailkot", 6: "Hyderabad", 7: "Sakardu",
            8: "Quetta", 9: "Multan"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), airbus_domestic_class_booking()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), airbus_domestic_class_booking()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), airbus_domestic_class_booking()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), airbus_domestic_class_booking()]).place(x=a2,
                                                                                                          y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), airbus_domestic_class_booking()]).place(x=a2,
                                                                                                          y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), airbus_domestic_class_booking()]).place(x=a2,
                                                                                                          y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), airbus_domestic_class_booking()]).place(x=a3,
                                                                                                            y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), airbus_domestic_class_booking()]).place(x=a3,
                                                                                                            y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), airbus_domestic_class_booking()]).place(x=a3,
                                                                                                            y=b + 300)
            a3 += 400

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# ********************************** Domestic Flights Departure *****************************
def airbus_domestic_flights_departure():
    data = open("flight user data.txt", "a")
    data.write("Flight: Domestic, Departure:")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(780, 150, text="DEPARTURE:", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#EB455F")

    def seat_file(x):
        data = open("flight user data.txt", "a")
        data.write(f" {x}, ")
        data.close()

    # buttons on canvas

    a, b = 310, 250
    a1, a2, a3 = a, a, a
    city = {1: "Lahore", 2: "Karachi", 3: "Islamabad", 4: "Peshawar", 5: "Sailkot", 6: "Hyderabad", 7: "Sakardu",
            8: "Quetta", 9: "Multan"}
    for seat in city:
        print(city[seat])
        if seat == 1:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[1]), airbus_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 2:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[2]), airbus_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400
        elif seat == 3:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[3]), airbus_domestic_flights_destination()]).place(
                x=a1, y=b)
            a1 += 400

        elif seat == 4:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[4]), airbus_domestic_flights_destination()]).place(x=a2,
                                                                                                                y=b + 150)
            a2 += 400
        elif seat == 5:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[5]), airbus_domestic_flights_destination()]).place(x=a2,
                                                                                                                y=b + 150)
            a2 += 400
        elif seat == 6:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10,
                             command=lambda: [seat_file(city[6]), airbus_domestic_flights_destination()]).place(x=a2,
                                                                                                                y=b + 150)
            a2 += 400
        elif seat == 7:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[7]), airbus_domestic_flights_destination()]).place(x=a3,
                                                                                                                  y=b + 300)
            a3 += 400
        elif seat == 8:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[8]), airbus_domestic_flights_destination()]).place(x=a3,
                                                                                                                  y=b + 300)
            a3 += 400
        elif seat == 9:
            seating = Button(text=city[seat], font="arial", fg="yellow", bg="#68B984", width=10
                             , command=lambda: [seat_file(city[9]), airbus_domestic_flights_destination()]).place(x=a3,
                                                                                                                  y=b + 300)
            a3 += 400

        main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                           , command=first_page).place(
            x=50, y=670)


# ********************************* Flight Nature ************************************
def airbus_flights_nature():
    data = open("flight user data.txt", "a")
    data.write("Plane: AirBus, ")
    data.close()
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 190, text="Which type of flight you want to have:",
                       font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")

    international = Button(text="International Flights", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF",
                           width=17,
                           height=1, command=airbus_international_flights_departure).place(x=340, y=370)

    domestic = Button(text="Domestic Flights", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=17, height=1
                      , command=airbus_domestic_flights_departure).place(
        x=880, y=370)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% AIR BUS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************** Plane Booking
def plane_booking():
    canvas = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas.place(x=0, y=5)

    canvas.create_text(750, 190, text="Choose Your Plane for Booking", font=(" Hermann Zapf's Optima", 40, "bold"),
                       fill="white")

    private_plane = Button(text="Private Jet", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                           height=1, command=private_jet_flights_nature).place(x=280, y=330)
    cargo_plane = Button(text="Cargo Plane", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13,
                         height=1, command=cargo_international_flight_departure).place(x=680, y=330)
    airbus = Button(text="AirBus", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", width=13, height=1,
                    command=airbus_flights_nature).place(
        x=1100, y=330)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


##########################################################################################################################

# ******************************** DATA ENTRY

def get_information():
    global entry1
    name_entry = entry1.get()
    data = open("flight user data.txt", "a")
    data.write("\n")
    data.write(f"Name:{name_entry}, ")
    data.close()

    global entry2
    passport_entry = entry2.get()
    data = open("flight user data.txt", "a")
    data.write(f"Passport:{passport_entry}, ")
    data.close()
    global entry3
    cnic_entry = entry3.get()
    data = open("flight user data.txt", "a")
    data.write(f"CNIC:{cnic_entry}, ")
    data.close()

    plane_booking()


def data_entry():
    canvas = Canvas(width=500, height=400, bg="#F8EDE3")
    canvas.place(x=500, y=190)

    canvas.create_text(150, 60, text="Access to the platform:", font=(" Hermann Zapf's Optima", 18),
                       fill="black")
    canvas.create_text(50, 130, text="Name:", font=(" Hermann Zapf's Optima", 12),
                       fill="black")
    canvas.create_text(70, 180, text="Passport No:", font=(" Hermann Zapf's Optima", 12),
                       fill="black")
    canvas.create_text(55, 230, text="CNIC No:", font=(" Hermann Zapf's Optima", 12),
                       fill="black")
    global entry1
    entry1 = Entry(window, width=30)
    entry1.place(x=650, y=310)

    global entry2
    entry2 = Entry(window, width=30)
    entry2.place(x=650, y=355)

    global entry3
    entry3 = Entry(window, width=30)
    entry3.place(x=650, y=405)

    booking_button = Button(text="Booking", font=("arial", 15), fg="white", bg="#3AB0FF", width=8,
                            command=get_information
                            ).place(x=700, y=530)

    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       ).place(
        x=50, y=670)
    back_page = Button(text="Back", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1,
                       command=passenger_booking).place(
        x=50, y=600)


##########################################################################################################################

# ******************************** Passenger Booking
def passenger_booking():
    # canvas Making
    canvas1 = Canvas(width=1600, height=800, bg="#E5BA73")
    canvas1.place(x=0, y=5)

    # welcome text
    canvas1.create_text(250, 100, text="HAKUNA  MATATA", font=(" Hermann Zapf's Optima", 40, "bold"), fill="#9C254D")
    canvas1.create_text(260, 145, text="AIRWAYS ௹", font=(" Hermann Zapf's Optima", 30, "bold"), fill="#282A3A")

    about_us = Button(text="About Us", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", height=1,
                      command=about_details).place(x=350, y=330)
    flight_booking = Button(text="Flight Booking", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", height=1,
                            command=data_entry).place(x=600, y=330)
    ticket_cancellation = Button(text="Flight Cancellation", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF",
                                 height=1, command=flight_cancel_screen).place(x=930, y=330)
    ticket_details = Button(text="Flight Details", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", height=1,
                            command=flight_details).place(x=470, y=450)
    question = Button(text="FAQ's", font=("arial", 20, "bold"), fg="yellow", bg="#B9E0FF", height=1, width=10,
                      command=faq).place(x=790, y=450)
    main_page = Button(text="Main Page", font=("arial", 20, "bold"), fg="yellow", bg="#CC3636", width=10, height=1
                       , command=first_page).place(
        x=50, y=670)


first_page()
