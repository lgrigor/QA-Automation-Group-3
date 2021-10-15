import allure
import pytest

def test_multiple_attachments():
    allure.attach.file('./21.jpg', attachment_type=allure.attachment_type.JPG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)

    x = 10
    y = 100
    assert y == x ** 3