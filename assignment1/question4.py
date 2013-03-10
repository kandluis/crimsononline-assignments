"""question 4

Practice creating a new Python project. In a separate directory, you should:
    * initialize a new Git repository
    * create a new virtual environment
    * find a fun Python package online
    * install that package into your virtual environment
    * run `pip freeze > requirements.txt` to save a listing of your virtual
      environment's packages into requirements.txt
    * write a short Python program that does something fun with the package
    * create a public GitHub repository and push your code to this new
      repository
    * provide a link to the GitHub page in question4.py

Don't feel obligated to spend more than about ten minutes on your test program.
We just want to see that you can use the toolchain.
"""

GITHUB_URL = "http://github.com/kandluis/question4"

from numpy import *

def funprogram():
    arr = array([[3,2,1,2,3,4],
                    [2,3,4,1,4,5],
                    [4,1,4,5,2,4]])
    
    return dot(arr,arr)
