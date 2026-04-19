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
# An example showing the difference between multiple ifs determining rewards 

def reward_system(marks:int)->str:
    if marks>90:
        print('Gold Reward')
    if marks>70:
        print('Silver Reward')
    if marks>50:
        print('Participation Reward')
    if marks <=50:
        print('No rewards') if marks >=0 else print('Invalid marks')
    if not marks:
        print("0 marks.. Try again next time!")
 
list1_marks = [80,95,20,90,-10,0]

for marks in list1_marks:
    reward_system(marks)

