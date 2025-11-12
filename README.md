## 📞 Twilio Autodialer Application

This is a simple Python application that uses the **Twilio Voice API** to initiate an automated phone call to a specified recipient number. The call delivers a pre-defined text-to-speech message using Twilio Markup Language (TwiML).

---

## ✨ Features

* **Automated Calling:** Instantly initiates a phone call upon execution.
* **Text-to-Speech:** Uses Twilio's `<Say>` TwiML verb to convert text into spoken audio.
* **Simple Setup:** Uses environment variables for secure and easy configuration of Twilio credentials and phone numbers.
* **Clear Output:** Provides immediate feedback, including the Call SID, upon successful call initiation or an error message if the call fails.

---

## 🛠️ Prerequisites

Before running this application, you need the following:

1.  **Python 3.x** installed on your system.
2.  A **Twilio Account**.
3.  A **Twilio Phone Number** with Voice capabilities.
4.  Your **Twilio Account SID** and **Auth Token**.

---

## 🚀 Getting Started

Follow these steps to set up and run the autodialer.

### 1. Save the Code

Save the provided Python code as a file named, for example, `autodialer.py`.

### 2. Install Dependencies

This project requires the `twilio` library for interacting with the Twilio API and `python-dotenv` for loading environment variables.

```bash
pip install twilio python-dotenv