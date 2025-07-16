# MPIN Strength Checker – OneBanc Assignment

This project checks whether a given MPIN (4-digit or 6-digit) is **STRONG** or **WEAK**.  
It uses common patterns and personal demographic data such as Date of Birth (DOB), Spouse's DOB, and Wedding Anniversary to assess the MPIN's security.

The project was created as part of the Data Science assignment for OneBanc Technologies.

# MPIN Strength Checker – OneBanc Assignment

This project checks whether a given MPIN (4-digit or 6-digit) is **STRONG** or **WEAK**.  
It uses common patterns and personal demographic data such as Date of Birth (DOB), Spouse's DOB, and Wedding Anniversary to assess the MPIN's security.

The project was created as part of the Data Science assignment for OneBanc Technologies.

---

## 📁 Project Structure

📦 MPIN-Checker
├── mpin_check.py # Core logic for MPIN evaluation
├── app.py # Streamlit UI (optional)
├── common_mpin_list.txt # External list of common MPINs
├── test_mpin_check.py # 25 detailed test cases
├── README.md # This file

## Features

- Accepts 4-digit and 6-digit MPINs
- Evaluates MPIN based on:
  - Commonly used MPINs (e.g., 1234, 0000)
  - Match with user’s date of birth
  - Match with spouse’s date of birth
  - Match with wedding anniversary
- Gives a final `strength` verdict (`STRONG` or `WEAK`)
- If weak, lists out specific reasons
- Supports:
  - Streamlit web interface
  - 25+ automated test cases

---

## How to Use

### 1. Web Interface (Streamlit)

```bash
streamlit run app.py
```

### 2. Run Tests

```bash
   python test_mpin_check.py
```

Submitted By
Name: Sumit Jha
University: Jaypee University of Engineering and Technology, Guna
Email: sumitjha0745@gmail.com
