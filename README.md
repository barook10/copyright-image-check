# 📷 Copyright Image Checker

![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=flat&logo=vuedotjs&logoColor=%234FC08D)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)

A minimal web app that checks images for copyright infringement using a simulated AI backend.

## 🚀 Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
Frontend Setup
bash
cd frontend
npm install
npm run dev
🌐 Endpoints
Method	Endpoint	Description
POST	/check_copyright	Upload image for analysis
🖥️ Tech Stack
Frontend: Vue 3 + Vite

Backend: Flask (Python)

Build: npm

📂 Project Structure
.
├── backend/
│   ├── app.py          # Flask server
│   ├── uploads/        # Image storage
│   └── requirements.txt
└── frontend/
    ├── src/            # Vue components
    └── vite.config.js  # Dev config
🛠️ Development
bash
# Backend (Flask)
http://localhost:5000

# Frontend (Vue)
http://localhost:5173
📝 Notes
Backend randomly generates results (simulated AI)

No database - uploads stored temporarily

CORS enabled for local development



 Key features:
- Clean markdown formatting
- Badges for tech stack
- Code blocks for commands
- Table for API endpoints
- Minimal file tree
- Quick reference URLs
- Concise notes section

