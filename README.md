# InstaStudio Web Application

This repository contains the reconstructed frontend of **InstaStudio** (Instagram Insights & Social Growth Dashboard), extracted from `mitytechandram.online`.

---

## 📁 Project Structure

```text
instastudio-app/
├── index.html            # Landing page (Features, Pricing, Offer)
├── app.html              # Main InstaStudio Dashboard (/app)
├── store                 # Simulated Play Store UI (/store)
├── assets/               # De-bundled JavaScript chunks & CSS styles
├── __l5e/                # Brand logos & high-resolution icons
├── manifest.webmanifest  # Progressive Web App manifest
├── server.py             # Local single-page application server
└── README.md             # This guide
```

---

## 🚀 How to Run Locally

### 1. Launch the Local Server
From this directory, run:
```bash
python3 server.py 8080
```
Or if you prefer `npx serve`:
```bash
npx serve -s . -l 8080
```

### 2. Open in Your Browser
- **Landing Page:** [http://localhost:8080/](http://localhost:8080/)
- **Dashboard (/app):** [http://localhost:8080/app](http://localhost:8080/app)
- **Store UI (/store):** [http://localhost:8080/store](http://localhost:8080/store)

---

## 🔑 Offline Access & Dashboard Activation

The application uses client-side state checks stored in `localStorage` to guard the `/app` dashboard:
- Key: `ig-access-activated`
- Value: `"1"`

To unlock the dashboard in local preview mode without needing an external activation key:
1. Open [http://localhost:8080/app](http://localhost:8080/app) in your browser.
2. Open Developer Tools (`F12` or `Cmd + Option + I`).
3. In the **Console**, run:
   ```javascript
   localStorage.setItem("ig-access-activated", "1");
   location.reload();
   ```

---

## 📱 Installing on Android

### Method 1: Progressive Web App (PWA)
1. Expose or host this directory on your local network (e.g. `http://<your-lan-ip>:8080/`).
2. Open the URL in Google Chrome on your Android device.
3. Tap the three dots menu (**⋮**) and select **"Add to Home screen"** or **"Install app"**.
4. Android and Chrome will automatically generate a native WebAPK launcher for it.

### Method 2: Convert to Standalone APK
You can wrap this directory into a native APK using tools such as:
- **Capacitor**: `npx @capacitor/cli create` -> copy assets to `www/` -> `npx cap add android` -> `npx cap open android`.
- **PWABuilder**: Package the PWA manifest into a signed APK using [PWABuilder CLI](https://www.pwabuilder.com/).
