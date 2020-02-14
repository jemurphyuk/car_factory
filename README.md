# Brioche Factory TDD

## Unit Test
- Test singular and unitary pieces of code

## Integration Test
- Tests code from end to end

## TDD - Test driven development
- First write a test, then code
- Code the minimum amount to pass the test

## Basics of a test
- Known inputs and know outputs
- Assertion with inputs and outputs
- Testing frameworks help you achieve this
- FOR BRIOCHE FACTORY
    - Brioche - known output (for bake_bread)
    - Dough - known input (for bake_bread), known output (for make_dough)
    - Ingredients - known input (for make_dough)
- make_dough - should make dough when given correct three arguments

### Integration test
- run_factory
    - As a user I want to be able to run a factory function. Give flour, water and eggs and recieve brioche

### Usage
````
make_dough(arg1, arg2, arg3)
bake(arg1)
run_factory(arg1, arg2, arg3)
````
## dunder main and dunder name
````
__main__, __name__
````
