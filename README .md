
# Fullstack DevOps App (React + Flask + MySQL) — Docker Compose + CI/CD

A minimal portfolio-ready project to showcase DevOps skills: containerization, Compose orchestration, and CI/CD via GitHub Actions.

## 📦 Stack
- Frontend: React (Vite) served by Nginx
- Backend: Flask (Python) + MySQL Connector
- DB: MySQL 8 (init via init.sql)
- DevOps: Docker, Docker Compose, GitHub Actions

## ⚙️ Run locally
```bash
git clone https://github.com/Misbah-Ashiq/fullstack-devops-app
cd fullstack-devops-app
cp .env.example .env
docker compose up -d --build
```
Then open:
- Frontend: http://localhost:5173
- Backend health: http://localhost:5000/api/health
- MySQL: localhost:3306

## 🔐 Endpoints
- `POST /api/signup` → { email, password }
- `POST /api/signin` → { email, password }

## 🗄️ Database schema
Initialized from `db/init.sql` at container start.

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARBINARY(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🧪 Quick test (curl)
```bash
curl -X POST http://localhost:5000/api/signup   -H "Content-Type: application/json"   -d '{"email":"test@example.com","password":"secret"}'
  
curl -X POST http://localhost:5000/api/signin   -H "Content-Type: application/json"   -d '{"email":"test@example.com","password":"secret"}'
```

## 🐳 CI/CD (GitHub Actions → Docker Hub)
1. Create a Docker Hub account and a personal access token.
2. In your GitHub repo **Settings → Secrets and variables → Actions** add:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
3. Push to main → GitHub Actions builds and pushes:
   - `yourname/fullstack-backend:latest`
   - `yourname/fullstack-frontend:latest`

Tip: You can deploy these images to any server and run them with a small compose file that pulls the images.

## 🧭 Architecture (Mermaid)
```mermaid
flowchart LR
  A[React + Nginx (5173)] -->|HTTP /api| B[Flask API (5000)]
  B --> C[(MySQL 8)]
```

## 🧹 Cleanup
```bash
docker compose down -v
```

## 📣 Credit
Created for a DevOps portfolio demo. Replace placeholders and make it yours!
