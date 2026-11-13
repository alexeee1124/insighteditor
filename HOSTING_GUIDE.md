# InstaStudio Hosting & Deployment Guide

This repository contains the standalone, fully unlocked InstaStudio Instagram clone application. It has **zero external pip dependencies** and runs cleanly on any standard Python 3.9+ environment or container runtime.

---

## 1. Quick Start (Local or VPS)

To run the server directly:
```bash
python3 server.py 8080
```
- Open [http://localhost:8080/app](http://localhost:8080/app) for the Instagram App.
- Open [http://localhost:8080/login](http://localhost:8080/login) to view connected API keys or update your tokens.
- Open [http://localhost:8080/store](http://localhost:8080/store) for the Play Store interface.

To run on a specific port:
```bash
python3 server.py 3000
# or via environment variable:
PORT=3000 python3 server.py
```

---

## 2. Cloud Hosting Options

### A. Railway / Render / Fly.io (One-Click)
1. Push this directory to a private GitHub repository.
2. In **Render** or **Railway**:
   - Create a new Web Service from your repository.
   - It will automatically detect the included `Dockerfile` or Python runtime.
   - Set Environment Variables (optional, can also be configured from `/login`):
     - `PORT`: (Auto-set by host)
     - `APIFY_TOKEN`: `apify_api_your_token_here`
     - `GEMINI_API_KEY`: (Your Google AI Studio Gemini API Key)
3. Deploy! The service will be live on your custom `*.onrender.com` or `*.up.railway.app` domain.

### B. Docker Container
Build and run with Docker:
```bash
docker build -t instastudio .
docker run -d -p 8080:8080 -e PORT=8080 --name instastudio instastudio
```

---

## 3. License Key Bypass & Activation

- **Access Gate Status:** All license checks (`2b83b07c...`, `adea2547...`, `cb31bdda...`, `3d35ff90...`) are completely unlocked.
- **Permanent Access:** The client wrapper has been converted to a pass-through Fragment, and `localStorage.setItem("ig-access-activated", "1")` is applied automatically.
- **No Device Restrictions:** Devices will never be blocked or prompted with *"This phone is blocked"* or *"Your plan has ended"*.

---

## 4. API Key Management

API keys can be managed in two ways:
1. **Via the Web Interface:** Go to `/login` to view your connected keys or click "Save" / "Remove".
2. **Via `keys.json` or Environment Variables:**
   - `keys.json`:
     ```json
     {
       "apify": "apify_api_your_token_here",
       "gemini": "AIzaSy..."
     }
     ```
   - Cloud Environment variables: `APIFY_TOKEN` and `GEMINI_API_KEY`.
