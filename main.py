import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="drowssaPtooR",
    database="librarymanagement"
)
print(mydb)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        # Show login page
        self.login_page()

    def login_page(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Login components
        tk.Label(self.root, text="Admin Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple login check (replace this with real authentication)
        if username == "admin" and password == "password":
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main menu components
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=10)
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=10)
        tk.Button(self.root, text="View Members", command=self.view_members).pack(pady=10)
        tk.Button(self.root, text="View Loan Statuses", command=self.view_loans).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.login_page).pack(pady=10)

    def search_books(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Search components
        tk.Label(self.root, text="Search for a book:").pack(pady=10)
        self.search_input = tk.Entry(self.root, width=40)
        self.search_input.pack(pady=5)
        tk.Button(self.root, text="Search", command=self.perform_search).pack(pady=10)

        # Listbox for displaying results
        self.results_list = Listbox(self.root, width=60)
        self.results_list.pack(pady=10)

        # Scrollbar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_list.yview)

        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

    def perform_search(self):
        search_query = self.search_input.get()
        if not search_query:
            messagebox.showwarning("Warning", "Please enter a search term!")
            return

        try:
            cursor = mydb.cursor()
            # Modify query to select both Title and AvailableCopies
            cursor.execute("SELECT Title, AvailableCopies FROM Books WHERE Title LIKE %s", ('%' + search_query + '%',))
            results = cursor.fetchall()
            self.results_list.delete(0, END)  # Clear previous results

            if results:
                for row in results:
                    # Display both the title and available copies
                    self.results_list.insert(END, f"Title: {row[0]}, Available Copies: {row[1]}")
            else:
                messagebox.showinfo("Info", "No books found.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()

    def add_book(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display current authors, genres, and publishers
        self.show_authors()
        self.show_genres()
        self.show_publishers()

        # Book details input fields
        tk.Label(self.root, text="Add a New Book", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Title:").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        tk.Label(self.root, text="Author ID:").pack()
        self.author_id_entry = tk.Entry(self.root)
        self.author_id_entry.pack()

        tk.Label(self.root, text="Genre ID:").pack()
        self.genre_id_entry = tk.Entry(self.root)
        self.genre_id_entry.pack()

        tk.Label(self.root, text="Publisher ID:").pack()
        self.publisher_id_entry = tk.Entry(self.root)
        self.publisher_id_entry.pack()

        tk.Label(self.root, text="Year Published:").pack()
        self.year_entry = tk.Entry(self.root)
        self.year_entry.pack()

        tk.Label(self.root, text="ISBN:").pack()
        self.isbn_entry = tk.Entry(self.root)
        self.isbn_entry.pack()

        tk.Label(self.root, text="Total Copies:").pack()
        self.total_copies_entry = tk.Entry(self.root)
        self.total_copies_entry.pack()

        # Submit button
        tk.Button(self.root, text="Add Book", command=self.insert_book).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

    def show_authors(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT AuthorID, AuthorName FROM Authors")
        authors = cursor.fetchall()
        cursor.close()

        tk.Label(self.root, text="Available Authors (ID - Name):", font=("Arial", 10, "bold")).pack(pady=5)
        for author in authors:
            tk.Label(self.root, text=f"{author[0]} - {author[1]}").pack()

    def show_genres(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT GenreID, GenreName FROM Genres")
        genres = cursor.fetchall()
        cursor.close()

        tk.Label(self.root, text="Available Genres (ID - Name):", font=("Arial", 10, "bold")).pack(pady=5)
        for genre in genres:
            tk.Label(self.root, text=f"{genre[0]} - {genre[1]}").pack()

    def show_publishers(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT PublisherID, PublisherName FROM Publishers")
        publishers = cursor.fetchall()
        cursor.close()

        tk.Label(self.root, text="Available Publishers (ID - Name):", font=("Arial", 10, "bold")).pack(pady=5)
        for publisher in publishers:
            tk.Label(self.root, text=f"{publisher[0]} - {publisher[1]}").pack()

    def insert_book(self):
        # Retrieve values from the form
        title = self.title_entry.get()
        author_id = self.author_id_entry.get()
        genre_id = self.genre_id_entry.get()
        publisher_id = self.publisher_id_entry.get()
        year_published = self.year_entry.get()
        isbn = self.isbn_entry.get()
        total_copies = self.total_copies_entry.get()

        try:
            cursor = mydb.cursor()
            cursor.execute(
                "INSERT INTO Books (Title, AuthorID, GenreID, PublisherID, YearPublished, ISBN, TotalCopies, AvailableCopies) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (title, author_id, genre_id, publisher_id, year_published, isbn, total_copies, total_copies)
            )
            mydb.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            self.main_menu()  # Go back to main menu after adding the book
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()

    def view_members(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display members
        tk.Label(self.root, text="Members List").pack(pady=10)
        members_list = Listbox(self.root, width=60)
        members_list.pack(pady=10)

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        members_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=members_list.yview)

        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT FullName, Email FROM Members")
            members = cursor.fetchall()

            if members:
                for member in members:
                    members_list.insert(END, f"{member[0]} - {member[1]}")
            else:
                members_list.insert(END, "No members found.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()

    def view_loans(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display loans
        tk.Label(self.root, text="Loans List").pack(pady=10)
        loans_list = Listbox(self.root, width=60)
        loans_list.pack(pady=10)

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        loans_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=loans_list.yview)

        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT BookID, MemberID, LoanDate, ReturnDate FROM Loans")
            loans = cursor.fetchall()

            if loans:
                for loan in loans:
                    loans_list.insert(END, f"Book ID: {loan[0]}, Member ID: {loan[1]}, Loan Date: {loan[2]}, Return Date: {loan[3]}")
            else:
                loans_list.insert(END, "No loans found.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()

# Initialize the main window
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
