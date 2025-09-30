Bank Management System
This is a desktop-based Bank Management System built with Python and Tkinter. It provides a graphical user interface for both bank customers and administrators to manage accounts and transactions securely. The application features separate portals for users and admins, each with distinct functionalities.

_**Features**_

**->Secure Login:** Users can log in with their username and password.

**->New User Registration:** A comprehensive registration form for new users to request an account. The request is then sent to an administrator for approval.

**->Account Dashboard:** After logging in, users can access their main dashboard.

**->View Balance:** Check the current account balance with a single click.

**->Transactions:**

_Withdrawal:_ Generate a secure 18-digit code to withdraw money from an ATM or the bank.

_Fund Transfer:_ Transfer funds to another user's account securely by verifying the recipient's account number and name.

_Request Detail Changes:_ Users can submit requests to an administrator to update their personal details, such as username, password, mobile number, email, or address.

**->Admin Functionalities**
Secure Admin Login: A separate and secure login portal for administrators.

_Dashboard:_ Admins have access to management tools after logging in.

_New User Approval:_ View a list of pending new user requests, review their details, and choose to either Accept or Reject them.

Upon acceptance, a unique account number is generated, a default balance of Rs. 5000 is credited, and the user's details are moved to the main database.
Approve User Detail Changes: Review and process requests from existing users to change their account information.

Technology Stack
Frontend (GUI): Python's Tkinter library.

Backend Logic: Python.
Database: MySQL Server.

Image Handling: Pillow (PIL Fork) library.

_**Prerequisites**_
Before you begin, ensure you have the following installed on your system:

Python 3.x
MySQL Server
The following Python libraries: Pillow, mysql-connector-python,Tkinter
