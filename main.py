from flask import Flask, redirect, url_for, render_template, request



#######################################Python task 1

def intial_input():
    applicants_num = input("Please, type the total number of applicants:\n")
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

a = 1
########################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student_list.html", methods=["POST","GET"])

def applicants():
    lst_applicants = []
    applicants_num = 0
    applicants_num_approved = 0
    applicants_num_request = "Please, type the total number of applicants:"
    applicants_num_approved_request = "Please, type the total number of applicants to be accepted:"
    error1 = ''
    error2 = ''
    continuance = ''
    warning1 = ''
    empty1 = ''
    warning2 = ''
    warning3 = ''
    warning4 = ''
    warning5 = ''
    warning6 = ''
    warning7 = ''
    warning8 = ''
    warning9 = ''
    warning10 = ''
    warning11 = ''
    warning12 = ''
    warning13 = ''
    warning14 = ''
    warning15 = ''
    warning16 = ''
    warning17 = ''
    warning18 = ''
    warning19 = ''
    warning20 = ''
    warning21 = ''
    warning22 = ''
    missing_or_cancel = ''

    if request.method == "POST":
        applicants_num = request.form.get("number")
        applicants_num_approved = request.form.get("number1")
        if applicants_num == '':
            empty1 = ''
        elif applicants_num_approved == '':
            empty1 = ''
        try:
            applicants_num_converted = int(applicants_num)
            try:
                applicants_num_approved_converted = int(applicants_num_approved)
                if applicants_num_approved_converted <= applicants_num_converted:
                    continuance = "Lets continue"

                    def add_postwarning():
                        warning5 = "Please type the first name:\n"
                        warning6 = "Please type the last name:\n"
                        firstname_student = request.form.get("number4")
                        lastname_student = request.form.get("number5")
                        try:
                            warning7 = "Please type the GPA:\n"
                            gpascore = request.form.get("number6")
                            gpascore_converted = float(gpascore)
                            full_name = firstname_student + " " + lastname_student
                            lst_applicants.append([gpascore_converted, full_name])
                            if len(lst_applicants) < applicants_num_converted:
                                warning_lower_num()
                            else:
                                warning8 = "All applicants were added. Check bellow the final results\n"

                        except:
                            warning9="Strings are not accepted, only integers and floats are accepted.\n"
                            add_postwarning()

                    def warning_lower_num():
                        warning2 = "It seems like, there are more students to add. The number of students should be " + str(
                            applicants_num_converted) + "."
                        warning3 = "If you want to cancel the subscription type [1]\nIf you want to input the remaining students type [2]\n"
                        missing_or_cancel = request.form.get("number3")
                        try:
                            missing_or_cancel = int(missing_or_cancel)
                            if missing_or_cancel == 1:
                                if len(lst_applicants) == 0:
                                    warning4 = "No Student to Evaluate.\n"
                            elif missing_or_cancel == 2:
                                add_postwarning()
                            else:
                                warning10 = "Please type exclusively [1] or [2]"
                                warning_lower_num()
                        except:
                            warning10 = "Please type, exclusively [1], [2]"
                            warning_lower_num()

                    def final_stats():
                        warning17 = "Number of Applicants: " + str(applicants_num_converted) + "\n"
                        warning18 = "Number of Applicants to be Approved: " + str(applicants_num_approved) + "\n"
                        warning19 = "All applicants:\n"
                        dict_applicants_sorted = sorted(lst_applicants, key=lambda x: (-x[0], x[1]))
                        for i in dict_applicants_sorted:
                            warning20 = i[1] + " " + str(i[0])
                        warning21 = "Approved applicants:\n"

                        for i in dict_applicants_sorted[0:applicants_num_approved_converted]:
                            warning22 = i[1]

                    def addstudent():
                        warning10 = "Do you want to add an applicant? [1] Yes /// [2] No\n"
                        question_mark = request.form.get("number7")
                        try:
                            question_mark = int(question_mark)
                            if question_mark == 1:
                                warning11 = "Please type the first name:\n"
                                warning12 = "Please type the last name:\n"
                                firstname_student = request.form.get("number7")
                                lastname_student = request.form.get("number8")
                                try:
                                    warning13 = "Please type the GPA:\n"
                                    gpascore = request.form.get("number9")
                                    gpascore_converted = float(gpascore)
                                    full_name = firstname_student + " " + lastname_student
                                    lst_applicants.append([gpascore_converted, full_name])
                                    if len(lst_applicants) < applicants_num_converted:
                                        warning_lower_num()
                                    else:
                                        warning14 = "All applicants were added.Check bellow the final results\n"

                                except:
                                    warning15="Strings are not accepted, only integers and floats are accepted.\n"
                                    add_postwarning()
                            elif question_mark == 2:
                                if len(lst_applicants) < applicants_num_converted:
                                    warning_lower_num()
                            else:
                                warning16 = "Please type exclusively [1] or [2]\n"
                                addstudent()
                        except:
                            warning16 = "Please type exclusively [1] or [2]\n"
                            addstudent()

                    addstudent()
                    final_stats()

                else:
                    warning1 = "Number of approved Students are greater than applicants"
            except:
                error1 = "Floats and Strings are not accepted, only integers are accepted."
                error2 = "Please, run again."
        except:
            error1 = "Floats and Strings are not accepted, only integers are accepted."
            error2 = "Please, run again."


    return render_template("student_list.html", applicants_num_request = applicants_num_request,
                           applicants_num_approved_request = applicants_num_approved_request, applicants_num=applicants_num,
                           error1 = error1, error2 =error2, continuance =continuance,
                           warning1 = warning1, empty1=empty1, warning2=warning2, warning3=warning3,
                                warning4=warning4,
                                warning5=warning5,
                                warning6=warning6,
                                warning7=warning7,
                                warning8=warning8,
                                warning9=warning9,
                                warning10=warning10,
                                warning11=warning11,
                                warning12=warning12,
                                warning13=warning13,
                                warning14=warning14,
                                warning15=warning15,
                                warning16=warning16,
                                warning17=warning17,
                                warning18=warning18,
                                warning19=warning19,
                                warning20=warning20,
                                warning21=warning21,
                                warning22=warning22,)


@app.route("/grades.html")
def grades():
    return render_template("grades.html")


if __name__== '__main__':
    app.run(debug=True)

