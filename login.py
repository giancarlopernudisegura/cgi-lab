#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')


form_correct = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
	cookie_username = cookie["username"].value
if cookie.get("password"):
	cookie_password = cookie["password"].value

cookie_correct = cookie_username == secret.username and cookie_password == secret.password

if cookie_correct:
	username = cookie_username
	password = cookie_password

if form_correct:
	print('Set-Cookie: username=%s' % username)
	print('Set-Cookie: password=%s' % password)

print()

if not username and not password:
	print(login_page())
elif username == secret.username and password == secret.password:
	print(secret_page(username=username, password=password))
else:
	print(after_login_incorrect())
