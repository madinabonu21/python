# Homework 1. ToDo List Application

# Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.


from datetime import datetime

# ------------------ Task Class ------------------
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False  # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = " Completed" if self.status else " Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


# ------------------ ToDoList Class ------------------
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f" Task '{task.title}' added successfully!\n")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f" Task '{task.title}' marked as complete!\n")
                return
        print("Task not found!\n")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.\n")
            return
        print(" All Tasks:")
        for task in self.tasks:
            print(task)

    def display_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.status]
        if not incomplete:
            print(" All tasks are complete!\n")
            return
        print(" Incomplete Tasks:")
        for task in incomplete:
            print(task)


# ------------------ Main Program (CLI) ------------------
def main():
    todo = ToDoList()

    while True:
        print("\n==== ToDo List Menu ====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            # Optional: validate date format
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print(" Invalid date format! Please use YYYY-MM-DD.\n")
                continue

            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == "2":
            title = input("Enter task title to mark as complete: ")
            todo.mark_task_complete(title)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.display_incomplete_tasks()

        elif choice == "5":
            print(" Exiting... Have a productive day!")
            break

        else:
            print(" Invalid choice! Please try again.\n")


# ------------------ Run Program ------------------
if __name__ == "__main__":
    main()


# Homework 2. Simple Blog System

# Define Post Class:
# Create a Post class with attributes like title, content, and author.
# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
# Create instances of posts and test the functionality of your Blog system.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"\n Post '{post.title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("\n No posts available.")
        else:
            print("\n All Blog Posts:")
            for index, post in enumerate(self.posts, start=1):
                print(f"{index}. {post.title} by {post.author}")

    def display_by_author(self, author):
        author_posts = [p for p in self.posts if p.author.lower() == author.lower()]
        if not author_posts:
            print(f"\n No posts found by author '{author}'.")
        else:
            print(f"\n Posts by {author}:")
            for post in author_posts:
                post.display()

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"\n Post '{title}' deleted successfully.")
                return
        print(f"\n No post found with title '{title}'.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print(f"\n Post '{title}' edited successfully.")
                return
        print(f"\nNo post found with title '{title}'.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("\nNo posts to display.")
        else:
            print(f"\n Latest {min(count, len(self.posts))} Posts:")
            for post in self.posts[-count:][::-1]:
                post.display()


def main():
    blog = Blog()

    while True:
        print("\n========== Simple Blog System ==========")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)

        elif choice == "6":
            blog.display_latest_posts()

        elif choice == "7":
            print("\n Exiting Blog System. Goodbye!")
            break

        else:
            print("\n Invalid choice! Please select from 1–7.")


if __name__ == "__main__":
    main()


# Homework 3. Simple Banking System

# Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
# Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
# Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# Test the Application:
# Create instances of accounts and test the functionality of your Banking system.

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder_name)
        print("Current Balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def add_account(self, account):
        if self.find_account(account.account_number):
            print("Account with this number already exists.")
        else:
            self.accounts.append(account)
            print("Account added successfully.")

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print("Current balance:", acc.balance)
        else:
            print("Account not found.")

    def deposit_money(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if not from_acc or not to_acc:
            print("One or both accounts not found.")
            return

        if from_acc.balance < amount:
            print("Insufficient funds for transfer.")
            return

        from_acc.balance -= amount
        to_acc.balance += amount
        print("Transfer successful.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            for acc in self.accounts:
                print(f"{acc.account_number} - {acc.holder_name} - Balance: {acc.balance}")


def main():
    bank = Bank()

    while True:
        print("\nSimple Banking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display All Accounts")
        print("7. Display Account Details")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(acc_num, name, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_money(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_money(acc_num, amount)

        elif choice == "5":
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer_money(from_acc, to_acc, amount)

        elif choice == "6":
            bank.display_all_accounts()

        elif choice == "7":
            acc_num = input("Enter account number: ")
            acc = bank.find_account(acc_num)
            if acc:
                acc.display_account_details()
            else:
                print("Account not found.")

        elif choice == "8":
            print("Exiting Banking System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
