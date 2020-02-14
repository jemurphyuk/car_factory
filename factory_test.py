from factory_functions import *

print('Testing make_dough() with water, flour and eggs, expect dough')
print(make_dough('water', 'flour', 'eggs') == 'dough')  # these test need to come back true to pass
print('Testing bake() with dough, expect brioche')
print(bake('dough') == 'brioche')

# for our test we only want an expected output or NOT expected output to show that test works
print('Testing make_dough() with water, cement and gravel, expect False')
print(make_dough('water', 'eggs', 'flour') == 'dough')  # these test need to come back true to pass
print('Testing bake() with cement expect false')
print(bake('cement') == 'brioche')

# integration test
print('Testing run_factory() with water, flour and eggs, expect brioche')
print(run_factory('water', 'flour', 'eggs') == 'brioche')  # these test need to come back true to pass
print('Testing run_factory() with other, expect false')
print(run_factory('other', 'make', 'love') == 'not brioche')
