import allure

TEST_CASE_LINK = r'https://github.com/lgrigor/Homeworks/blob/main/Examples%20from%20Slides/Lesson%2020%20Allure%20Framework/test_Links.py'

@allure.link('https://www.youtube.com/watch?v=NeQM1c-XCDc')
def test_with_link():
    pass

@allure.link('https://www.youtube.com/watch?v=NeQM1c-XCDc', name='Rammstein')
def test_with_named_link():
    pass

@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass

@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass
