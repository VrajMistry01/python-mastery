# A grading system using if/elif/else 

def grading_system(marks:int)->str:

    if marks > 90:
        print('GRADE A')
    elif marks > 70:
        print("GRADE B")
    else:
        print("GRADE C")

list_marks = [80,95,20,90]
for marks in list_marks:
    grading_system(marks)