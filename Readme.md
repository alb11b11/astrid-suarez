
# 🎨 Astrid Suarez Gallery — Project README

## 📍 Project Overview

This project is a **static web gallery** showcasing paintings by Astrid Suarez.

It is deployed using Netlify and accessible at:
👉 https://astrid-suarez.netlify.app

The goal of this project is to:

* Display artwork in a clean, mobile-friendly format
* Allow easy sharing via QR code
* Enable potential buyers to view and contact the artist

---

## 📁 Project Structure

```
gallery/
│
├── index.html              # Main gallery page
├── paintings/              # Folder containing all images
│   ├── bosque-encantado.jpeg
│   ├── flores-en-ceramica.jpeg
│   └── ...
└── README.md               # This file
```

### 📌 Naming Convention (IMPORTANT)

All images must follow:

* Lowercase
* No spaces → use `-`
* No accents (é → e, ñ → n)

✅ Example:

```
cordillera-de-ahuachapan.jpeg
```

❌ Avoid:

```
Cordillera de Ahuachapán.jpeg
```

---

## 🚀 Deployment (Netlify)

### 🔑 Access

1. Go to Netlify
2. Click **Log in**
3. Use the same account used to create the project
4. Select: `astrid-suarez`

---

### 🟢 Deployment Method Used

This project uses **manual drag & drop deployment**

### 📦 To Update the Website

1. Modify files locally
2. Go to Netlify dashboard
3. Click **Deploys**
4. Drag and drop the updated `gallery/` folder

✅ Netlify will automatically redeploy

---

## ⚠️ Important Notes

* Netlify does **NOT store your source as a working project**
* Your **local folder is the source of truth**
* Always keep a backup of:

  ```
  /Users/alejandrooyarbide/Desktop/Astrid/
  ```

---

## 📱 QR Code Generation

### Generate QR (image file)

```bash
qrencode -o astrid-gallery.png "https://astrid-suarez.netlify.app"
```

### Terminal display

```bash
qrencode -t ansiutf8 "https://astrid-suarez.netlify.app"
```

### Install tool (if needed)

```bash
# macOS
brew install qrencode

# Linux / WSL
sudo apt install qrencode
```

---

## 🛠 How to Add New Paintings

1. Add image to:

   ```
   paintings/
   ```

2. Rename properly (see naming rules)

3. Edit `index.html` and add a new entry:

```html
<img src="paintings/new-painting.jpeg" alt="New Painting">
```

4. Redeploy on Netlify

---

## 💡 Recommended Improvements (Next Steps)

### 💰 Monetization Features

* Add price below each painting
* Add “Available / Sold” labels
* Add WhatsApp contact button

### 📲 Mobile Optimization

* Ensure images resize properly
* Improve spacing for phone screens

### 🌐 Custom Domain

* Example:

  ```
  astridsuarez.art
  ```
* Configure in Netlify → Domain settings

---

## 🔄 Optional Upgrade (Recommended)

Move project to GitHub for:

* Version control
* Backup
* Automatic deploys

Flow:

```
Local → GitHub → Netlify (auto deploy)
```

---

## 🧠 Key Concept

This is a **static website**:

* No backend
* No database
* Fast and simple
* Easy to maintain

---

## 📞 Contact Integration (Future)

You can add:

```html
<a href="https://wa.me/YOURNUMBER">Contact via WhatsApp</a>
```

---

## ✅ Maintenance Checklist

Before each update:

* [ ] Images properly named
* [ ] Added to `index.html`
* [ ] Tested locally (optional)
* [ ] Deployed via Netlify
* [ ] QR code still valid

---

## 🧾 Local Path

Project location:

```
/Users/alejandrooyarbide/Desktop/Astrid/
```

---

## 🎯 Final Goal

A simple, elegant, and shareable online gallery that:

* Showcases art professionally
* Is easy to update
* Can generate real sales

---

