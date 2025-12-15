# Docker Voting App Demo

A simple multi-container Docker application demonstrating a voting system with a **Vote App**, **Worker**, **Redis**, and **Results App**.

---

## Features

- Vote for **Option A** or **Option B**  
- Live results display  
- Background processing with a **worker**  
- Easy setup with Docker Compose

---

## Folder Structure
shreeja_docker_demo/
├── docker-compose.yml
├── vote/ # Vote App
├── result/ # Results App
└── worker/ # Worker script


---

## Run the App

```bash
git clone <repo-url>
cd shreeja_docker_demo
docker compose up --build -d


Voting App: http://localhost:5000

Results App: http://localhost:5001

Stop the app:

docker compose down
