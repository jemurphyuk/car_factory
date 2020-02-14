from factory_functions import *


class FactoryTest:

    @classmethod
    def tests_for_make_parts(cls):
        print('Testing make_parts() with labour and metal in any order, expect shiny parts')
        print(make_parts(['labour', 'metal']) == 'shiny parts')
        print(make_parts(['metal', 'labour']) == 'shiny parts')# these test need to come back true to pass
        print('Testing make_parts() with longer list, expect False')
        print(make_parts(['name', 'geoff', 'any']) == 'shiny parts')
        print('Testing make_parts() with wrong list, expect False')
        print(make_parts(['name', 'geoff']) == 'shiny parts') # these test need to come back true to pass


    # for our test we only want an expected output or NOT expected output to show that test works
    @classmethod
    def tests_for_build_car(cls):
        print('Testing build_car() with shiny parts, expect car')
        print(build_car('shiny parts') == 'car')
        print('Testing build_car() with other, expect false')
        print(build_car('stuff') == 'car')

        # integration test
    @classmethod
    def tests_for_run_factory(cls):
        print('Testing run_factory() with labour and metal, expect car')
        print(run_factory(['labour', 'metal']) == 'car')  # these test need to come back true to pass
        print('Testing run_factory() with other, expect false')
        print(run_factory(['other', 'make', 'love']) == 'not car')

    @classmethod
    def all_tests(cls):
        FactoryTest.tests_for_make_parts()
        FactoryTest.tests_for_build_car()
        FactoryTest.tests_for_run_factory()
