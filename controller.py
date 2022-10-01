from view import (show_menu, print_result, get_search_name, 
                  get_search_number, get_search_adress, get_search_position, get_search_cabinet, get_new_user, get_file_name)
from model import write_txt, write_csv, read_csv, find_by_name, find_by_number, find_by_adress,find_by_position, find_by_cabinet, add_user

def work_with_information():
    choice = show_menu()
    information = read_csv('information.csv')


    while (choice != 9):
        if choice == 1:
            print_result(information)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(information, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(information, number))
        elif choice == 4:
            adress = get_search_adress()
            print(find_by_adress(information, adress))
        elif choice == 5:
            position = get_search_position()
            print(find_by_position(information, position))
        elif choice == 6:
            cabinet = get_search_cabinet()
            print(find_by_cabinet(information, cabinet))
        elif choice == 7:
            user_data = get_new_user()
            add_user(information, user_data)
            write_csv('information.csv', information)
        elif choice == 8:
            file_name = get_file_name()
            write_txt(file_name, information)
        choice = show_menu()
