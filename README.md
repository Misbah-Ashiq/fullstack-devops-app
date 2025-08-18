# Fullstack DevOps App (React + Flask + MySQL) — Docker Compose + CI/CD  

A minimal portfolio-ready project to showcase DevOps skills: containerization, Compose orchestration, and CI/CD via GitHub Actions.  

---

## 📦 Stack
- **Frontend:** React (Vite) served by Nginx  
- **Backend:** Flask (Python) + MySQL Connector  
- **DB:** MySQL 8 (init via `init.sql`)  
- **DevOps:** Docker, Docker Compose, GitHub Actions, EC2 Deployment  

---

## ⚙️ Run Locally
```bash
git clone https://github.com/Misbah-Ashiq/fullstack-devops-app.git
cd fullstack-devops-app
cp .env.example .env
docker compose up -d --build
Then open:

Frontend: http://localhost:5173

Backend health: http://localhost:5000/api/health

MySQL: localhost:3306

🔐 Endpoints
POST /api/signup → { email, password }

POST /api/signin → { email, password }

🗄️ Database Schema
Initialized from db/init.sql at container start.

sql
Copy
Edit
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARBINARY(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
🧪 Quick Test (via curl)
bash
Copy
Edit
curl -X POST http://localhost:5000/api/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"secret"}'

curl -X POST http://localhost:5000/api/signin \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"secret"}'
🐳 CI/CD (GitHub Actions → Docker Hub → EC2)
Docker Images
GitHub Actions automatically builds and pushes:

misbahashiq/fullstack-backend:latest

misbahashiq/fullstack-frontend:latest

Deployment
On every push to main, GitHub Actions:

Builds images and pushes to Docker Hub

SSH into EC2 server

Pulls the latest code & Docker images

Runs docker compose up -d

🧭 Architecture (Mermaid)
mermaid
Copy
Edit
flowchart LR
  A[React + Nginx (5173)] -->|HTTP /api| B[Flask API (5000)]
  B --> C[(MySQL 8)]
🧹 Cleanup
bash
Copy
Edit
docker compose down -v
📣 Credit
Created by Misbah Ashiq for DevOps portfolio demo 🚀
