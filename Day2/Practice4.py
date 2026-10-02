#Create variables for a student's name (string), marks (integer), and whether they passed (boolean, True/False). Print all details in one sentence using f-string.
student_name = "Amar Kushwaha"
student_marks = 78
student_result = True

print(f"{student_name} scored {student_marks} marks and passed status is {student_result}")


#Create a variable with value 100 (int). Try adding a string "5" directly to it without converting (e.g., 100 + "5") and run it. What error do you get? Then fix it using proper conversion.
value = 100
adding  = "5"
print(100 + int("5"))
print(str(100) + "5")