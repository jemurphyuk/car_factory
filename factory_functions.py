# As a user

def make_dough(arg1, arg2, arg3):
    if arg1 == 'water' and arg2 == 'flour' and arg3 == 'eggs':
        return 'dough'
    else:
        return 'not dough'


def bake(arg1):
    if arg1 == 'dough':
        return 'brioche'
    else:
        return 'you burned it'

def run_factory(arg1, arg2, arg3):
    result_dough = make_dough(arg1, arg2, arg3)
    result_bake = bake(result_dough)
    return result_bake