#Tox is a tool for automating testing in multiple python environments
#when you write a tox file usually called tox.ini it allows you to
#Run your python tests automatically
#Test your code in multiple python versions(e g:python 3.8,3.9 3.10)
#check dependencies are properly installed
#Ensure your package works on all environments

#why do we use tox ?
#you dont want to manually create virtual environments and install dependencies for each version
#Tox will
#Create virtual environemnts  for each python version
#install dependencies from requirements.txt or setup.py
#run your all python tests in all environments

#sample tox.ini

# [tox]
# envlist = py38,py39,py310
#
# [testenv]
# deps =
#     pytest
#     pytest-html
#
# commands = pytest --html =report.html



