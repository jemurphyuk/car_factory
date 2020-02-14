
# print(__name__) # identify function call location

# if called directly, __name__ = __main__
# if imported it will have file name of imported location
#
# if __name__ == '__main__': # --> useful method to test if function call location is in imported file,
#                  # used in running tests, starting game etc
#     print('You Called?')


from factory_functions import *
from factory_test import FactoryTest

print('Welcome to the Factory, what would you like to do')
while True:
    user_input = input('Type "1" to run the factory, Type "2" for test, "EXIT" to leave:     ')
    if user_input.upper() == 'EXIT':
        break
    elif user_input == '1':
        user_input2 = input('How many materials are you putting in?:      ')
        material_list = []
        for i in range(1, int(user_input2) + 1):
            material = input(f"Please input material {i}:   ")
            material_list.append(material)
        print(run_factory(material_list))
    elif user_input == '2':
        print('Method 1 = Make Parts\nMethod 2 = Build Car\nMethod 3 = Run Factory')
        while True:
            user_input3 = input('Which method would you like?\n(Type "ALL" for all, "NONE" to leave):  ')
            if user_input3.upper() == 'NONE':
                break
            elif user_input3.upper() == 'ALL':
                FactoryTest.all_tests()
                break
            elif user_input3 == '1':
                FactoryTest.tests_for_make_parts()
                break
            elif user_input3 == '2':
                FactoryTest.tests_for_build_car()
                break
            elif user_input3 == '3':
                FactoryTest.tests_for_run_factory()
                break
            else:
                print('Command not known, please try again')
    else:
        print('Unknown command, please try again')

