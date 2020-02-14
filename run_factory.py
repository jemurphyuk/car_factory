from factory_functions import *

print(__name__) # identify function call location

# if called directly, __name__ = __main__
# if imported it will have file name of imported location

if __name__ == '__main__': # --> useful method to test if function call location is in imported file,
                                # used in running tests, starting game etc
    print('You Called?')

