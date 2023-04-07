import os
import sys

# if __name__ == '__main__':

def start():
    os.system('del report')
    os.system('pytest -s -v ./testcases/ --alluredir ./report --clean-alluredir')
    os.system('allure serve ./report')

if __name__ == '__main__':
    start()