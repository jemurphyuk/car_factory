# As a user

def make_parts(argument_list):
    if argument_list[0] != 'metal' and argument_list[0] != 'labour':
        return 'no parts'
    elif len(argument_list) > 2:
        return 'no parts'
    elif (argument_list[0] == 'metal' or argument_list[1] == 'metal') and (
            argument_list[0] == 'labour' or argument_list[1] == 'labour'):
        return 'shiny parts'
    else:
        return 'no parts'


def build_car(arg1):
    if arg1 == 'shiny parts':
        return 'car'
    else:
        return 'no car'


def run_factory(argument_list):
    result_parts = make_parts(argument_list)
    result_car = build_car(result_parts)
    return result_car

# component_list = ['metal', 'labour']
# print(make_parts(component_list))
