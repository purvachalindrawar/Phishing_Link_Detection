# 🚨 Phishing URL Detection System 🚨

Welcome to the **Phishing URL Detection System** project! This tool helps detect and manage potential phishing URLs using a streamlined web interface built with **Streamlit** and a backend powered by **MySQL**. The system allows users to check URLs against a database, visualize data trends, and contribute to the database by adding new phishing URLs.

---

## ✨ Features

1. **🔍 URL Verification**: 
   - Paste any URL to check if it’s present in the database.
   - Alerts are provided if the URL is detected as a phishing attempt.

2. **📊 Dashboard**:
   - View the number of phishing URLs detected.
   - Track common domains and phishing trends over time.

3. **💾 Database Management**:
   - Add new URLs to the database directly from the web interface if they are not already present.
   - Automatic domain extraction and labeling for newly added URLs.

4. **⚠️ User Alerts**:
   - Instant alerts for URLs not present in the database with an option to add them.

---

## 🛠️ Installation

### Prerequisites
- Python 3.x
- MySQL Server
- Streamlit
- MySQL Connector for Python

## Configure the Database
### Create a MySQL database:

### Run 
```bash
streamlit run app.py
