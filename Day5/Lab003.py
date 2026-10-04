#Keyword Arguments
def student_details(name, age, course):
    print(f"Student name is {name}, age {age} and course taking {course}.")
student_details(age=20, course="Software testing", name="Amar")

def display_children(child1, child2, child3):
    print("Youngest child is " + child2)
display_children(child1="John", child2="Mary", child3="Alice")


#Arbitrary keyword Arguments, **kwargs
def show_details(**details):
    print(details) #printin list form
    for key, value in details.items():
         print(f"{key}: {value}") #print in the key and value form using for loop
show_details(name="Amar", course="ST", insitute="PS")

