# -------------------------------- #
# Title: Assignment 7
# Description: Demonstrating pickling and
#   structured error handling in Python
# Change Log:
#   MG / 5.28.20 / outlined script
#   MG / 5.30.20 / created functions for pickling to & from file
#   MG / 5.31.20 / added some structured error handling
#   MG / 6.1.20 / modified script & added comments
# -------------------------------- #

# --- Data --- #
import pickle  # import pickle module for writing binary data to file

string_file_name = ''  # captures the user's file name input
string_title = ''  # captures the user's title input
reading_lst = []  # a list of titles


# --- Processing --- #
class Processor:
    """ Performs processing tasks """

    @staticmethod
    def add_title_to_list(new_title, list_of_titles):
        """ Adds data to a list

        :param new_title: (string) to add to list
        :param list_of_titles: (list) to add data to
        :return: (list)
        """
        list_of_titles.append(new_title)  # add new title to list
        print('\n' + 'Title added to reading list.')
        return list_of_titles  # return updated list

    @staticmethod
    def remove_title_from_list(remove_title, list_of_titles):
        """ Removes data from a list

        :param remove_title: (string) to remove from list
        :param list_of_titles: (list) to remove data from
        :return: (list)
        """
        for title in list_of_titles:
            if title.lower() == remove_title.lower():
                list_of_titles.remove(title)  # remove title from list
                print('\n' + 'Title removed from reading list.')
        return list_of_titles  # return updated list

    @staticmethod
    def pickle_to_file(file_name, list_of_titles):
        """ Pickles data to a file

        :param file_name: (object) representing file to pickle to
        :param list_of_titles: (list) of data to pickle
        :return: nothing
        """
        file = open(file_name, 'wb')  # open the file for writing
        pickle.dump(list_of_titles, file)  # "dump" pickled data to file
        file.close()  # close file
        print('\n' + 'Reading list saved to file.')

    @staticmethod
    def unpickle_from_file(file_name):
        """ Unpickles data from a file

        :param file_name: (object) representing file to unpickle from
        :return: (list) that was unpickled from file
        """
        try:
            file = open(file_name, 'rb')  # open the file for reading
            global reading_lst
            reading_lst = pickle.load(file)
            file.close()  # close file
            print('\n' + 'Reading list loaded from file.')
            return reading_lst  # return unpickled list
        except FileNotFoundError:  # catch file not found error
            print('\n' + 'File not found: Please choose an existing file.')
        except pickle.UnpicklingError:  # catch corrupted data error
            print('\n' + 'Data error: Please check file for corruption.')


# --- Presentation --- #
class IO:
    """ Performs input and output tasks """

    @staticmethod
    def print_reading_list(list_of_titles):
        """ Displays list to the user

        :param list_of_titles: (list) to display
        :return: nothing
        """
        print('\n' + 'Reading List:')
        for title in list_of_titles:
            print(' * ' + title)

    @staticmethod
    def print_menu():
        """ Displays menu of options to the user

        :return: nothing
        """
        print('''
        Options
        1 - Display reading list
        2 - Add title to list
        3 - Remove title from list
        4 - Save list to file
        5 - Load list from file
        6 - Exit
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets menu choice from the user

        :return: (int) choice
        """
        try:
            choice = int(input('Which option would you like to perform? [1 to 6]: '))  # convert string choice to int
            return choice  # return user input as int
        except ValueError:  # catch input that can't be converted to int
            print('\n' + 'Value error: Please enter a number.')

    @staticmethod
    def input_file_name():
        """ Gets file name from the user

        :return: (string) file name
        """
        global string_file_name  # declare global variable
        string_file_name = input('\n' + 'Enter file name: ')
        return string_file_name  # return input file name

    @staticmethod
    def input_title():
        """ Gets title from the user

        :return: (string) title
        """
        global string_title  # declare global variable
        string_title = input('\n' + 'Title: ')
        return string_title  # return input title


# --- Main --- #
while True:
    IO.print_menu()  # display menu to the user
    menu_choice = IO.input_menu_choice()  # capture user's menu choice

    try:

        if menu_choice == 1:  # display current list
            if reading_lst == []:  # if empty list
                print('\n' + 'List is currently empty.')
            else:
                IO.print_reading_list(reading_lst)  # displays list
            continue

        elif menu_choice == 2:  # add title to list
            IO.input_title()  # gets title input
            Processor.add_title_to_list(string_title, reading_lst)  # adds title to list
            continue

        elif menu_choice == 3:  # remove title from list
            IO.input_title()  # gets title input
            Processor.remove_title_from_list(string_title, reading_lst)  # removes title from list

        elif menu_choice == 4:  # pickle list to file
            IO.input_file_name()  # gets file name input
            Processor.pickle_to_file(string_file_name, reading_lst)  # pickles data to file
            continue

        elif menu_choice == 5:  # unpickle list from file
            IO.input_file_name()  # gets file name input
            Processor.unpickle_from_file(string_file_name)  # unpickles data from file
            continue

        elif menu_choice == 6:  # exit
            print('\n' + 'Goodbye! Happy reading!')
            break

        elif menu_choice != 1-6:
            raise IndexError()

    except IndexError as e:  # catch input that is not a number from 1-6
        print('\n' + 'Index error: Please enter a number from 1 to 6.')