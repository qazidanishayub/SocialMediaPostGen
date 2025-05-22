# 🤖 AI-Powered LinkedIn Post Generator

This project is a powerful, two-part application designed to generate high-quality, LinkedIn-ready posts using Google’s Gemini AI. Ideal for AI/ML engineers, SaaS leaders, and thought leaders aiming to increase professional visibility and engagement on LinkedIn.

---

## 📦 Project Structure

```
linkedin-post-generator/
├── frontend/        # Next.js application (UI)
│   └── pages/       # Contains index.tsx for main interface
│
├── api/             # FastAPI backend (Gemini integration)
│   ├── generate.py  # AI-powered post generator endpoint
│   └── requirements.txt
```

---

## 🚀 Live Stack Overview

| Layer        | Tech           | Hosted On    |
|--------------|----------------|--------------|
| Frontend     | Next.js (React) | Vercel       |
| Backend API  | FastAPI         | Render / Railway |
| AI Engine    | Gemini Pro 1.5  | Google AI Studio |

---

## 🧠 Features

- Multi-domain post generation (AI/ML, SaaS, Agentic AI, etc.)
- User-guided or auto-generated content paths
- FastAPI backend with Gemini 1.5 Pro integration
- Clean UI built with React + TypeScript
- Vercel + Render compatible

---

## 🔧 Deployment Guide

### ➤ Frontend (Vercel)

1. Deploy from GitHub
2. Set **Root Directory** to `frontend/`
3. No additional config needed
4. Environment Variables: *None required*

### ➤ Backend (Render / Railway)

1. Navigate to `/api/`
2. Add this to `requirements.txt`:
   ```txt
   fastapi
   uvicorn
   google-generativeai
   ```
3. Set Environment Variable:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Deploy as a **Web Service** on port `8000`

---

## 🌐 API Endpoint

> POST `/generate`

**Request JSON:**
```json
{
  "user_idea": "Using RAG with LangChain...",
  "domain": "Generative AI"
}
```

**Response JSON:**
```json
{
  "post": "Here’s your LinkedIn-ready post..."
}
```

---

## 🧪 Local Development

```bash
# Run frontend
cd frontend
npm install && npm run dev

# Run backend
cd ../api
uvicorn generate:app --reload --port 8000
```

---

## ✍️ Author

**Qazi Danish**  
AI/SaaS Strategist | Product Builder | Founder, [LinkedIn AI Post Studio]  
[LinkedIn](https://linkedin.com/in/qazidan) · [GitHub](https://github.com/qazidan)

---

## 📄 License

MIT License — feel free to fork, extend, and build on this.
