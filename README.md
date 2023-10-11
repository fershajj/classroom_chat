# classroom_chat

REQUIREMENTS:
      python

INTRODUCTION:

The Classroom Chat Application is designed to facilitate communication among students and mentors within a local area network (LAN) environment. It serves as a reliable communication channel, particularly in scenarios with limited or disrupted internet access. Here are the key features and functionalities:

LAN-Based Communication: Students can interact with their peers and mentors without relying on the internet. This is especially useful in areas with unstable or limited internet connectivity.

Python GUI Application: The application is built using the Python GUI library Tkinter. It provides an intuitive interface for users to connect and communicate in a local network.

LAN Server: A LAN server is employed to connect mentors and students, serving as a communication hub within the network.

IP Address and Port Configuration: Each chatroom is assigned a unique IP address and port number, ensuring secure and efficient communication within the LAN.

User Registration and Authentication: Users (mentors and students) can register themselves with a unique username and an email address without a domain name. Email addresses must be unique, preventing duplicate registrations. Users can log in using their registered email and password. In case of a forgotten password, a recovery process is in place, including OTP generation and password reset.

Chatroom Features: The chatroom interface includes elements such as a user list, a chat message display, and an input box. Users can also send text files within the LAN environment.

Chat History: The chat application stores chat history, allowing users to view previous conversations even after relogging. However, the chat history is limited to messages sent after the user's initial login.

Mentor Authority: Mentors have the privilege to clear chat history, a useful feature for managing older and less relevant chat content.

Email Integration: For password recovery, the application requires users to specify their school/university email domain in the code, which is used for sending password reset emails.

Multiple Chatrooms: The application allows users to log in to multiple chatrooms simultaneously from the same PC, enhancing versatility and convenience.

It's important to note that the application's functionality depends on the server being operational. Users can enjoy seamless communication and support within the LAN environment, ensuring uninterrupted interaction within the educational setting.

STEPS TO FOLLOW:

1.download the classroom doubts folder and save it in directory

2.enter host ip address where ever necessary(mentioned in code in server/server.py , student1/client.py, student2/client.py, moderator/client.py)

3.Enter root path of where classroom doubts folder is stored where ever necessary(mentioned in code in student1/client.py, student1/login.py, student2/client.py, student2/login.py, moderator/client.py, moderator/login.py)

4.Enter senders email address,senders name where ever necessary(mentioned in code in  student1/pwreset.py, student2/pwreset.py, moderator/pwreset.py)

5.In terminal, run: (root is the path to classroon doubts folder)

      python -u "root\classroom doubts\server\server.py"
      
6.simultaneously run:

      python -u "root\classroom doubts\student1\client.py"
      
      python -u "root\classroom doubts\student2\client.py"
      
      python -u "root\classroom doubts\moderator\client.py"
      
7.register and login, to go to chat window
