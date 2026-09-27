# Mobile Shop CRUD

A simple command-line Mobile Shop Management System built with Python.

The project uses a Python list to store mobile records and provides the basic CRUD operations needed to manage them.

## Features

- Add a new mobile
- Display all mobiles
- Search for a mobile by ID
- Update mobile details
- Delete a mobile
- Exit through a simple menu

## Data Format

Each mobile is stored as a list in this format:

```text
[id, brand, model, price, quantity]
```

Example:

```python
[101, "Samsung", "Galaxy A55", 35000, 5]
```

## Project Structure

```text
mobile-shop/
│
├── mobile_shop_crud.py
└── README.md
```

## Requirements

- Python 3

No external libraries are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python3 mobile_shop_crud.py
```

On systems where `python` points to Python 3, this also works:

```bash
python mobile_shop_crud.py
```

## Menu

When the program starts, you will see:

```text
======================================
       MOBILE SHOP MANAGEMENT
======================================
1. Add Mobile
2. Display All Mobiles
3. Search Mobile
4. Update Mobile
5. Delete Mobile
6. Exit
```

Enter the number of the operation you want to perform.

## Example

Adding a mobile:

```text
--- Add Mobile ---

Enter Mobile ID: 101
Enter Brand: Samsung
Enter Model: Galaxy A55
Enter Price: 35000
Enter Quantity: 5
Mobile added.
```

Displaying mobiles:

```text
--- Mobile List ---

-----------------------------------------------------------------
ID      Brand          Model               Price       Qty
-----------------------------------------------------------------
101     Samsung        Galaxy A55          35000.00    5
-----------------------------------------------------------------
```

## CRUD Operations

| Operation | Function | What it does |
|-----------|----------|--------------|
| Create | `add_mobile()` | Adds a new mobile |
| Read | `display_mobiles()` | Shows all mobiles |
| Read | `search_mobile()` | Finds a mobile using its ID |
| Update | `update_mobile()` | Changes mobile details |
| Delete | `delete_mobile()` | Removes a mobile |

## Notes

- Mobile IDs must be unique.
- Price is stored as a decimal value.
- Quantity is stored as an integer.
- Data is stored only while the program is running.
- Closing the program clears the current data because no database or file storage is used.

## Learning Concepts

This project demonstrates:

- Lists
- Functions
- `for` loops
- `if`, `elif`, and `else`
- User input
- Searching
- Updating list elements
- Removing list elements
- A menu-driven program
- Basic CRUD logic

## Author

**Mobile Shop CRUD Project**
