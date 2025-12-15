name = input('Enter student name: ')
marks = int(input('Enter marks (0-100):'))
upper_name= name.upper()

if marks >= 90:
    grade = "A"
    message = "Phenomenal! You're crushing it keep that fire alive!"
elif marks >= 80:
    grade = "B"
    message = "Great job! You're on a strong path just a little more push to reach the top!"
elif marks >= 70:
    grade = "C"
    message = "Solid effort! You're growing steadily stay curious and keep building!"
elif marks >= 60:
    grade = "D"
    message = "You're getting there! Every step counts keep refining your skills!"
else:
    grade= "F"
    message = "This grade does not define you. Your effort, your mindset, and your comeback will. Keep going."

print(f'\n📊RESULT FOR {upper_name}:')
print('Marks: ' , f'{marks}/100')
print('Grade: ' ,f'{grade}')
print(f'{message}')
