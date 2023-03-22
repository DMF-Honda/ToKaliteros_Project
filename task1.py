#task 1
lst_applicants = []

def warning_lower_num():
    print("It seems like, there are more students to add. The number of students should be " + str(applicants_num_converted) + ".")
    missing_or_cancel = input("If you want to cancel the subscription type [1]\nIf you want to input the remaining students type [2]\n")
    try:
        missing_or_cancel = int(missing_or_cancel)
        if missing_or_cancel == 1:
            if len(lst_applicants) == 0:
                print("No Student to Evaluate.\n")
            else:
                print("")
        elif missing_or_cancel == 2:
            add_postwarning()
        else:
            print("Please type exclusively [1] or [2]")
            warning_lower_num()
    except:
        print("Please type, exclusively [1], [2]")
        warning_lower_num()

def add_postwarning():
    firstname_student = input("Please type the first name:\n")
    lastname_student = input("Please type the last name:\n")
    try:
        gpascore = input("Please type the GPA:\n")
        gpascore_converted = float(gpascore)
        full_name = firstname_student + " " + lastname_student
        lst_applicants.append([gpascore_converted, full_name])
        if len(lst_applicants) < applicants_num_converted:
            warning_lower_num()
        else:
            print("All applicants were added. Check bellow the final results\n")

    except:
        print("Strings are not accepted, only integers and floats are accepted.\n")
        add_postwarning()

def addstudent():
    question_mark = input("Do you want to add an applicant? [1] Yes /// [2] No\n")
    try:
        question_mark = int(question_mark)
        if question_mark == 1:
            firstname_student = input("Please type the first name:\n")
            lastname_student = input("Please type the last name:\n")
            try:
                gpascore = input("Please type the GPA:\n")
                gpascore_converted = float(gpascore)
                full_name = firstname_student + " " + lastname_student
                lst_applicants.append([gpascore_converted, full_name])
                if len(lst_applicants) < applicants_num_converted:
                    warning_lower_num()
                else:
                    print("All applicants were added.Check bellow the final results\n")

            except:
                print("Strings are not accepted, only integers and floats are accepted.\n")
                add_postwarning()
        elif question_mark == 2:
            if len(lst_applicants) < applicants_num_converted:
                warning_lower_num()
        else:
            print("Please type exclusively [1] or [2]\n")
            addstudent()
    except:
        print("Please type exclusively [1] or [2]\n")
        addstudent()

def final_stats():
    print("Number of Applicants: " + str(applicants_num_converted) + "\n")
    print("Number of Applicants to be Approved: " + str(applicants_num_approved) + "\n")
    dict_applicants_sorted = sorted(lst_applicants, key=lambda x: (-x[0], x[1]))
    print("All applicants:\n")
    for i in dict_applicants_sorted:
        print(i[1] + " " + str(i[0]))
    print("Approved applicants:\n")
    for i in dict_applicants_sorted[0:applicants_num_approved_converted]:
        print(i[1])

applicants_num=input("Please, type the total number of applicants:\n")
try:
    applicants_num_converted = int(applicants_num)
    applicants_num_approved = input("Please, type the total number of applicants to be accepted:\n")
    try:
        applicants_num_approved_converted = int(applicants_num_approved)
        if applicants_num_approved_converted <= applicants_num_converted:
            addstudent()
            final_stats()
    except:
        print("Floats and Strings are not accepted, only integers are accepted.")
        print("Please, run again.\n")
except:
    print("Floats and Strings are not accepted, only integers are accepted.")
    print("Please, run again.\n")


