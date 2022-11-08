import pickle


def user_write():
    def choose_option():
        user_option = input("Enter [YES | NO | MENU]: ")
        user_option.lower()
        if user_option == 'menu' or user_option == 'm':
            pickle.dump(records, file_name)
            print('Student Data, Saved Successfully!')
            file_name.close()
            menu()
        elif user_option == 'n' or user_option == 'no':
            pickle.dump(records, file_name)
            print('Student Data, Saved Successfully!')
            file_name.close()
            quit()
        elif user_option == 'y' or user_option == 'yes':
            pickle.dump(records, file_name)
            print('Student Data, Saved Successfully!\n')
            file_name.close()
            user_write()
        else:
            print('Enter the Yes or No or Menu')
            choose_option()

    file_name = open('BinaryData.dat', 'ab')
    records = []
    while True:
        roll_no = int(input('Enter Roll Number: '))
        user_name = input('Enter the Student Name: ')
        marks = int(input('Enter Marks: '))
        data_store = [roll_no, user_name, marks]
        records.append(data_store)
        print('Do you want to enter more Records of the Students? or want to go the MENU')
        choose_option()


def user_read():
    def choose_option():
        user_option = input("Enter [YES | NO | MENU]: ")
        user_option.lower()
        if user_option == 'menu' or user_option == 'm':
            menu()
            print('Okay')
        elif user_option == 'n' or user_option == 'no':
            print('Okay')
            quit()
        else:
            print('Enter the Yes or No or Menu! KIDDO!!')
            choose_option()

    file_name = open('BinaryData.dat', 'rb')
    file_data = pickle.load(file_name)
    if file_data:
        print('Data Available')
        for i in file_data:
            roll_no = i[0]
            user_name = i[1]
            marks = i[2]
            print('\nRoll No:', roll_no, '\nStudent Name: ', user_name, '\nMarks: ', marks)
            print('\n')
            file_name.close()
            choose_option()
    else:
        print('No Data Available')
        choose_option()


def user_search():
    file_name = open('BinaryData.dat', 'rb')
    file_data = pickle.load(file_name)
    search_result = 0
    user_search_input = int(input('Enter Roll Number of the Student: '))
    for i in file_data:
        if i[0] == user_search_input:
            print('Student Information Found!')
            print('Student Information: ')
            print('\tRoll No:', i[0], '\n\tStudent Name: ', i[1], '\n\tMarks', i[2])
            print('\nDo you want to Search again?')

            search_result += 1
            if i[0] != user_search_input:
                print('Searching')
        else:  # IF THE SEARCH RESULT NOT FOUND
            print('Student Information Not Found!')
            print('Do you want to Search again?')

            def user_option():
                user_choice = input('Enter [YES | NO | MENU]: ')
                if user_choice.lower() == 'n' or user_choice.lower() == 'no':
                    print('Stopping Search!')
                    quit()
                elif user_choice.lower() == 'y' or user_choice.lower() == 'yes':
                    print('Okay!')
                    user_search()
                elif user_choice.lower() == 'menu' or user_choice.lower() == 'm':
                    print('Okay!')
                    menu()
                else:
                    print('That is not a YES! or NO! Kiddo!')
                    user_option()


def menu():
    print('MENU')
    print('What do you want to do?')
    print('''
    1. Input Student Info.
    2. Read Student Info.
    3. Search Student.
    4. Quit the Program.
    ''')
    choice = int(input('Enter (1 | 2 | 3 | 4): '))
    if choice == 1:
        user_write()
        print('\n')
    elif choice == 2:
        user_read()
        print('\n')
    elif choice == 3:
        user_search()
        print('\n')
    elif choice == 4:
        quit()
    else:
        print('Enter only 1 or 2 or 3 not anything else. KIDDO!!')
        print('\n')
        menu()


menu()
