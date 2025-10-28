# Task Manager API

A RESTful Task Management API built with **Django** and **Django REST Framework (DRF)**.  
This API allows users to manage tasks: create, update, delete, mark complete/incomplete, filter, sort, and paginate tasks.  

---

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Filtering, Searching, Ordering & Pagination](#filtering-searching-ordering--pagination)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)

---

## Features
- **Task Management (CRUD)**: Create, read, update, delete tasks.
- **Task Attributes**: Title, Description, Due Date, Priority (Low, Medium, High), Status (Pending, Completed), timestamps.
- **User Management**: Register and authenticate users; each user manages their own tasks only.
- **Task Completion**: Mark tasks complete/incomplete with timestamps; completed tasks cannot be edited unless reverted.
- **Advanced Filtering & Sorting**: Filter by status or priority; search by title/description; sort by due date, priority, or creation date.
- **Pagination**: Supports page-based pagination for task lists.

---

## Technologies
- Python 3.x
- Django 5.2.x
- Django REST Framework
- Django Filters
- SQLite (default, can be replaced with other databases)
- Token-based Authentication

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/T0nia/task-manager-api.git
cd task-manager-


| Endpoint                      | Method | Description                                                      |
| ----------------------------- | ------ | ---------------------------------------------------------------- |
| `/api/tasks/`                 | GET    | List tasks (with optional filters, search, ordering, pagination) |
| `/api/tasks/`                 | POST   | Create a new task                                                |
| `/api/tasks/<id>/`            | GET    | Retrieve task details                                            |
| `/api/tasks/<id>/`            | PUT    | Update a task (cannot edit completed tasks)                      |
| `/api/tasks/<id>/`            | DELETE | Delete a task                                                    |
| `/api/tasks/<id>/complete/`   | POST   | Mark task as completed                                           |
| `/api/tasks/<id>/incomplete/` | POST   | Mark task as incomplete                                          |

