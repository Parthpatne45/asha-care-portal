# AshaCare – Digital Support System for ASHA & Anganwadi Workers

**Second Year College Project**

A simple web application that helps ASHA and Anganwadi workers manage:
- Maternal Surveillance
- Child Nutrition Monitoring
- Immunization Tracking
- NCD Screening

This replaces paper-based tools with a digital system that provides basic real-time support.

---

## How to Run

1. Open the folder in **VS Code**
2. Open Terminal (`Ctrl + `` `)
3. Install Flask:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open browser → **http://127.0.0.1:5000**

---

## Demo Login

| Worker Type       | Worker ID     | Password |
|-------------------|---------------|----------|
| ASHA Worker       | asha001       | 123456   |
| Anganwadi Worker  | anganwadi01   | 123456   |

---

## Features

- Home, About, Services, Contact pages
- Worker Login (Session based)
- Dashboard with statistics and alerts
- Add new beneficiary form
- Responsive design

---

## Project Structure

```
asha-care-portal/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_beneficiary.html
│   └── contact.html
└── static/
    ├── css/style.css
    └── js/script.js
```

---

**Created as Second Year College Demo Project – 2026**
