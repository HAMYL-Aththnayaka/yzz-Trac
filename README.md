# 📦 Yzz Trac

A modern full-stack **Inventory Management System** built with **React** and **FastAPI**. YSS Trac provides a clean and responsive interface for managing products while exposing a RESTful API for inventory operations. The project demonstrates modern frontend-backend integration, clean architecture, and scalable application development.

---

## ✨ Features

### 🖥️ Frontend (React)

* Modern and responsive user interface
* Product inventory dashboard
* Add new products
* Edit existing products
* Delete products
* Search products
* Sort products
* Real-time API integration
* Responsive design

### ⚡ Backend (FastAPI)

* RESTful API
* CRUD operations
* Automatic request validation with Pydantic
* Interactive Swagger documentation
* ReDoc documentation
* Fast asynchronous endpoints
* Clean project structure

---

# 🛠 Tech Stack

## Frontend

* React
* Axios
* CSS3

## Backend

* FastAPI
* Pydantic
* Uvicorn

---

# 📁 Project Structure

```text
YSS-Trac/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── ...
│
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/HAMYL-Aththnayaka/YSS-Trac.git
cd YSS-Trac
```

---

# ⚙️ Backend Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```powershell
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

# 💻 Frontend Setup

Navigate to the frontend directory

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Start the development server

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://localhost:8000/docs
```

### ReDoc

```
http://localhost:8000/redoc
```

---

# 🔗 API Endpoints

| Method | Endpoint         | Description                         |
| ------ | ---------------- | ----------------------------------- |
| GET    | `/`              | Welcome endpoint                    |
| GET    | `/products`      | Get all products                    |
| GET    | `/products/{id}` | Get a product by ID                 |
| POST   | `/products`      | Create a new product                |
| PUT    | `/products/{id}` | Update a product *(if implemented)* |
| DELETE | `/products/{id}` | Delete a product *(if implemented)* |

---

# 📦 Product Model

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 999.99,
  "quantity": 25
}
```

---

# 🎯 Learning Objectives

This project was built to strengthen my knowledge of:

* FastAPI
* React
* REST API Development
* Frontend & Backend Integration
* CRUD Operations
* API Communication with Axios
* Component-Based Architecture
* Modern Full-Stack Development

---

# 🚀 Future Improvements

* JWT Authentication
* PostgreSQL Database
* SQLAlchemy ORM
* Product Categories
* Image Uploads
* Dashboard Analytics
* Pagination
* Filtering & Search
* Docker Support
* Unit & Integration Testing
* CI/CD Pipeline
* Cloud Deployment

---

# 📸 Screenshots

<img width="946" height="945" alt="image" src="https://github.com/user-attachments/assets/79467e69-7257-47a9-8a92-a1e791239318" />


---

# 🌐 Live Demo

Coming Soon...

---

# 👨‍💻 Author

## Yasas Aththanayaka

IT Undergraduate at the **University of Vavuniya, Sri Lanka** with a passion for backend engineering, full-stack development, and building scalable software solutions.

### Connect with Me

* 🌐 Portfolio: https://yazaz-exe-6wnj.vercel.app/
* 💼 LinkedIn: https://www.linkedin.com/in/yasas-aththanayaka-a9b9b2333
* 🐙 GitHub: https://github.com/HAMYL-Aththnayaka
* 📧 Email: [Aththanayakayasas@gmail.com](mailto:Aththanayakayasas@gmail.com)

> *"Building software that solves real-world problems, one project at a time."*

---

# 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful or interesting, consider giving it a **Star** on GitHub!
