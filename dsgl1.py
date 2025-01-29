course_id = input("Хичээл: ")
course_name = input("Хичээлийн нэр: ")
credit = input("Хичээлийн кредит: ")

madlib = " Энэ хичээлийн код нь {}".format(course_id) + \
", хичээлийн нэр нь {}".format(course_name).title() + \
"  бөгөөд уг хичээл нь {}".format(credit) + " кредийн хичээл юм."
print(madlib)