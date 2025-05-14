profile = {}

def new(name, age, subjects):
    profile[name] = [age, subjects]

def validator(prompt_text):
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print('Invalid input! Please enter a number.')

while True:
    prompt = input('Enter command (add/get/average/view/exit): ').strip().lower()

    if prompt == 'exit':
        break

    elif prompt == 'add':
        sname = input('Name of student: ').lower().strip()
        if sname in profile:
            print('Student already exists\n')
        else:
            age = validator(f"Enter {sname.capitalize()}'s age: ")
            subject_list = {}
            print('\nEnter the subjects student is studying:\n')
            while True:
                subject = input('Name of subject (type "exit" when done): ').strip().lower()
                if subject == 'exit':
                    print('\nSubject(s) added successfully\n')
                    break
                elif subject == '':
                    print('Type a valid subject name to continue\n')
                elif subject in subject_list:
                    print('Subject already exists\n')
                else:
                    midterm = validator(f'   Enter {subject.capitalize()} midterm grade: ')
                    final = validator(f'Enter {subject.capitalize()} final exam grade: ')
                    subject_list[subject] = (midterm, final)
                    print()
            new(sname, age, subject_list)

    elif prompt == 'view':
        if not profile:
            print('No data available\n')
        else:
            for student, data in profile.items():
                age, subjects = data
                print(f'Student name: {student.capitalize()}')
                print(f'         Age: {int(age)} years')
                print('     Courses:')
                for subject, grades in subjects.items():
                    print(f'             {subject.capitalize()} - Midterm: {grades[0]}, Final: {grades[1]}')
                print()

    elif prompt.startswith('get '):
        name = prompt[4:].strip().lower()
        if name in profile:
            age, subjects = profile[name]
            print(f'Student name: {name.capitalize()}')
            print(f'         Age: {int(age)} years')
            print('     Courses:')
            for subject, grades in subjects.items():
                print(f'             {subject.capitalize()} - Midterm: {grades[0]}, Final: {grades[1]}')
            print()
        else:
            print('Student not found\n')

    elif prompt == 'average':
        for student, data in profile.items():
            _, subjects = data
            total_score = 0
            total_items = 0
            for grades in subjects.values():
                total_score += sum(grades)
                total_items += len(grades)
            avg = total_score / total_items if total_items else 0
            print(f'{student.capitalize()} - Average Grade: {avg:.2f}')
        print()

    else:
        print('Enter the right command\n')
