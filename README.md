# Yardly Backend

**Yardly** is a mobile-first classifieds application backend built with **FastAPI**, **MongoDB**, and **Docker**.  
It supports user registration/login via JWT, posting products, and messaging between users.

## 🚀 Technologies

- FastAPI
- MongoDB
- Motor (async Mongo driver)
- Docker & Docker Compose
- JWT Authentication
- Python 3.10

## 📂 Project Structure

```
/app
  /routes
    auth.py
    products.py
    messages.py
  /schemas
    user.py
    product.py
    message.py
  /models
  /utils
    token.py
Dockerfile
docker-compose.yml
.env (not tracked in Git)
.gitignore
```

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/yardly-backend.git
   cd yardly-backend
   ```

2. **Create a `.env` file**
   ```env
   MONGO_URI=mongodb://mongo:27017/yardly
   SECRET_KEY=your_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

4. **Access the API**
   ```
   http://localhost:8000/docs
   ```

## 📜 Available API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/auth/register` | Register a new user |
| POST   | `/auth/login` | Login and obtain token |
| POST   | `/products/` | Create a new product |
| GET    | `/products/` | List all products |
| GET    | `/products/{id}` | View a specific product |
| POST   | `/messages/send` | Send a message |
| GET    | `/messages/{conversation_id}` | Get conversation history |

## 📄 License

This project is licensed under the MIT License.
