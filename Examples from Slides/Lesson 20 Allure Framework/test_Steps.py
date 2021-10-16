import allure
import pytest

@allure.step
def passing_step():
    pass

@allure.step
def step_with_nested_steps():
    x = 2
    y = x ** 5
    print(y)
    nested_step()

@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')

@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass

def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
