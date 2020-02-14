# Car Factory TDD

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
- FOR CAR FACTORY
    - CAR - known output (for build_car)
    - PARTS - known input (for build_car), known output (for make_parts)
    - Ingredients - known input (for make_parts)
- make_parts - should make dough when given correct three arguments

### Integration test
- run_factory
    - As a user I want to be able to run a factory function. Give metal and labour and receive car

### Usage
````
make_parts(arg1, arg2, arg3)
build_car(arg1)
run_factory(arg1, arg2, arg3)
````
## dunder main and dunder name
````
__main__, __name__
````
