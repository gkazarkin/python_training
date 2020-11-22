# python_training
env = cd <project>\env\Scripts
activate

chromedriver = C:\Windows\SysWOW64\chromedriver86.exe

# Tests in cmd
cd <path to tests>
py.test --browser=chrome test_delete_group.py

# You can specify the browser for testing
in cmd type --browser=firefox (or opera, ie)
1) Also need add the webriver's file before and specify path to it
2) Change path to webdriver in application.py / def __init__
For example:
self.wd = webdriver.Chrome("C:\\Windows\\SysWOW64\\chromedriver86.exe"))

# You can specify the address of the application under test
in cmd --baseUrl=YOUR_URL