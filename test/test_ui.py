import os
import unittest
import sys
sys.path.append('.')

from project.ui import choice

TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/test/test_files'
new_dir = '/home/hadi/Documents/GitHub/file_categorizer/test/test_files/test2'

try:
    wrong_input = choice("", "")
except AssertionError:
    print('Cought empty intput')

try:
    wrong_input = choice("message", "")
except AssertionError:
    print('Cought empty choices')


right_input = choice("Test 3 selection", ('choice 1', 'choice 2', ' choice 3'))
right_input.selection = ''
print(right_input.selection)
right_input.check_selection()
right_input.selection = -1
print(right_input.selection)
right_input.check_selection()
right_input.selection = 0
print(right_input.selection)
right_input.check_selection()
right_input.selection = 4
print(right_input.selection)
right_input.check_selection()
right_input.selection = 3
right_input.choices
print(right_input.choices, right_input.msg, right_input.selection)
right_input.check_selection()


right_input.get_user_input()
