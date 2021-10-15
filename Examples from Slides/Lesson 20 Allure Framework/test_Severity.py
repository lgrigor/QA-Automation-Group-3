import allure
import pytest
import time

@allure.severity('critical')
def test_file1_method1():
	x=5
	y=6
	time.sleep(5)
	assert x+1 == y,"First test failed"
	assert x == y, f"Second test failed"

@allure.severity('normal')
def test_file1_method2():
	x=5
	y=6
	time.sleep(3)
	assert x+1 == y+1,"test failed"

def test_file1_method3():
	time.sleep(4)
	#assert False
	assert True

def test_file1_method4():
	time.sleep(3)
	#assert False
	assert True