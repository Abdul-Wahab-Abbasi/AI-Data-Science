# 📚 Library Management System

A terminal-based Library Management System built with Python. It allows you to manage a book inventory through a simple command-line interface — add, update, delete, and view books, along with inventory statistics.

---

## Features

- **Admin Login** — Secure access with username and password before entering the system
- **Add Books** — Register new books with name, author, price, and quantity
- **View Books** — Display all books in a formatted table with stock status
- **Update Books** — Edit specific fields or update all book details at once
- **Delete Books** — Remove books with a confirmation prompt before deletion
- **Inventory Statistics** — View total books, average price, most/least expensive book, and stock summary
- **Input Validation** — All inputs are validated (empty checks, type checks, range checks)
- **Persistent Storage** — Book data is saved to a `.txt` file and persists across sessions

---

## Tech Stack

- **Language:** Python 3
- **Storage:** Flat file (`data/books.txt`, comma-separated)
- **Interface:** Command-line (terminal)

---

## Project Structure

```
library-management-system/
│
├── data/
│   └── books.txt         # Book data storage
│
└── main.py               # Main application file
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

**2. Run the app**
```bash
python main.py
```

> No external dependencies required. Pure Python 3.

---

## Default Credentials

| Field    | Value   |
|----------|---------|
| Username | `admin` |
| Password | `123`   |

---

## How It Works

On launch, the system prompts for login. Once authenticated, a menu is displayed with the following options:

```
1. See All Books
2. Add New Book
3. Update Book
4. Delete Book
5. View Statistics
6. Exit
```

Books are stored in `data/books.txt` in the format:

```
id,name,author,price,quantity,status
10001,The Alchemist,Paulo Coelho,12.99,5,In-Stock
```

Book IDs are auto-generated starting from `10001` and increment with each new entry.

---

## Data Validations

| Field    | Rules                                           |
|----------|-------------------------------------------------|
| Name     | Cannot be empty                                 |
| Author   | Alphabets and spaces only, cannot be numeric    |
| Price    | Must be a positive number                       |
| Quantity | Must be a non-negative integer                  |
| Book ID  | Must exist in the system                        |


## License

This project is open source and available under the [MIT License](LICENSE).