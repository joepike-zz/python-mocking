
from unittest import mock

import simple

# def use_simple_function():
#     result = simple.simple_function()
#     print(result)
#
# use_simple_function()
#
# @mock.patch('simple.simple_function')
# def mock_simple_function(mock_simple_func):
#     mock_simple_func.return_value = "You have mocked simple_function"
#     result = simple.simple_function()
#     print(result)
#
# mock_simple_function()

# output:
# You have called simple_function
# <MagicMock name='simple_function' id='4467801840'>
# <MagicMock name='simple_function' id='4467801840'>
# <MagicMock name='simple_function()' id='4470148904'>

# New MagicMock object created when simple_function is called. simple_function is itself a MagicMock
# object, so how is a new MagicMock object created and how can you call an object???

# __call__ is called when an object is called as a function

# if a class has a __call__ function then an instance of the class can be created, and then call that instance
# like a function, e.g.

# class ExampleClass:
#     def __call__(self, *args, *kwargs):
#         print "Hell yeah!"
#
# inst = ExampleClass()
#
# inst()

# So when MagicMock is called as a function (in the form of simple_function here), the __call__ function
# is called, and magicmock implements this as a new MagicMock object

def side_effect_function():
    return "Woooh!"

@mock.patch('simple.simple_function')
def mock_simple_function_with_side_effect(mock_simple_func):
    mock_simple_func.side_effect = side_effect_function
    result = simple.simple_function()
    print(result)
