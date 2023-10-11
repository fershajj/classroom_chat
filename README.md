# classroom_chat

REQUIREMENTS:
      python

STEPS TO FOLLOW:

1.download the classroom doubts folder and save it in directory

2.enter host ip address where ever necessary(mentioned in code in server/server.py , student1/client.py, student2/client.py, moderator/client.py)

3.Enter root path of where classroom doubts folder is stored where ever necessary(mentioned in code in student1/client.py, student1/login.py, student2/client.py, student2/login.py, moderator/client.py, moderator/login.py)

4.Enter senders email address,senders name where ever necessary(mentioned in code in  student1/pwreset.py, student2/pwreset.py, moderator/pwreset.py)

5.In terminal, run: (root is the path to classroon doubts folder)

      python -u "root\classroom doubts\server\server.py"
      
6.simultaneously run each lines in different terminals:

      python -u "root\classroom doubts\student1\client.py"
      
      python -u "root\classroom doubts\student2\client.py"
      
      python -u "root\classroom doubts\moderator\client.py"
      
7.register and login, to go to chat window

8.If forgot password, and sending mail via gmail to get otp for password reset, create an app password in google account and use it in place of password in pwreset.py
