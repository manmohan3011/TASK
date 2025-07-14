# TASK

📝 Document360 API Task – Beginner Explanation
🎯 Goal of the Task

The task is about writing a simple Python program (like a mini app) that can talk to a remote server (Document360) and do 4 things with folders:


See all folders (GET)
Create a folder (POST)
Rename a folder (PUT)
Delete a folder (DELETE)
This is called doing CRUD operations using an API.


💻 What is an API?
An API (Application Programming Interface) is like a menu in a restaurant. It tells you what operations you can do. In this case, Document360 gives us some URLs (called endpoints), where we can send requests to do things like:

“Give me the list of folders”
“Create a new folder”
“Change folder name”
“Delete this folder”

🛠️ What Tools Did I Use?
Python – Programming language used to write the code.
VS Code – A code editor (like MS Word but for code).
Requests Library – This helps Python make API requests (like sending messages to the API).

🔨 What I Built, Step by Step

📁 Step 1: Setup Configuration
I created a file called config.py
It contains:
The base URL of the API.
My API token (like a password that tells the system I have access).

🔍 Step 2: View All Folders (GET)
I wrote a function to fetch all existing folders from Document360 using the GET method.
It prints the list of folders with their names and IDs.

🆕 Step 3: Create New Folder (POST)
I created a function to make a new folder called "TestFolder" by sending data to the API.
I saved the folder ID returned by the API so I can use it later.

✏️ Step 4: Rename Folder (PUT)
I used the saved folder ID to update its name to "UpdatedTestFolder".

❌ Step 5: Delete Folder (DELETE)
I used the same folder ID to delete the folder from the drive.


🧱 How the Files Are Organized
document360_api_task/
│
├── config.py        → Contains base URL and token
├── api_client.py    → All the main logic (GET, POST, PUT, DELETE)
├── main.py          → Runs everything step by step
├── README.md        → Easy instructions for setup
└── .gitignore       → To hide sensitive files

🔐 What is an API Token?
An API token is like a key to your locker.
Without it, the system won’t let you do anything.



I included it in the request headers like this:


headers = {
    "api_token": "<your_token_here>",
    "Content-Type": "application/json"
}


🧪 What Extra Things I Did (Bonus)

📋 Printed every request and response clearly (so we know what’s happening).

❗ Used error handling (try/except) so the app doesn’t crash if something goes wrong.

🔁 Used the folder ID dynamically instead of hardcoding it.


▶️ How to Run This Project
Install Python (if not already).
Install the requests library by running this command:
pip install requests
Open config.py and add your API token:
"api_token": "your_actual_token_here"
Run the program using:
python main.py



🗣️ Final Summary (For Interview)
This task helped me learn how to talk to a REST API using Python, handle dynamic data (like folder IDs), and write clean, easy-to-read code. I made sure the app logs everything clearly and handles errors gracefully. Everything runs in a proper sequence using functions and modular design.


OUTPUT:

<img width="1570" height="909" alt="Screenshot 2025-07-14 110523" src="https://github.com/user-attachments/assets/1ef404cb-12a6-44c2-90ce-d234216c7d13" />

