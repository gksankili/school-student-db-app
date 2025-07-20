# School Student DB App

A simple containerized Python Flask web application to manage school student records. It supports creating, viewing, editing, and deleting records stored in a CSV file. The app runs inside a Red Hat UBI 8 minimal container using Python 3.9.

---

## 🛠 Features

- View all student records
- Create a new student entry
- Edit existing student details
- Delete a student record
- View details of a student
- Persistent storage using a CSV file

---

## 🐳 Run with Docker

```bash
docker build -t student-db-app .
docker run -p 5000:5000 student-db-app
