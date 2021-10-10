import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

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