# coding: utf-8
from login_page import LoginPage

def login(driver, username, password):
	login_page = LoginPage(driver)
	login_page.login(username, password)
