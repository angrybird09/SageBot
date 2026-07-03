#  SageBot AI

SageBot AI is a Telegram chatbot built with Python and powered by Google's Gemini AI. It allows users to chat with an AI assistant directly through Telegram.

---

##  Features

-  AI-powered conversations using Google Gemini
-  Telegram Bot integration
-  Secure API key management using environment variables
-  Fast and lightweight
-  Built with Python

---

## Tech Stack

- Python 3
- Google Gemini API
- python-telegram-bot
- python-dotenv

---

##  Project Structure

```text
SageBot/
├── .github/
│   └── workflows/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── sbot.py
```

---

## ⚙️Installation

### 1. Clone the repository

```bash
git clone https://github.com/angrybird09/SageBot.git
cd SageBot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it.

**Linux / WSL**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Copy the example file:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder values with your own:

```env
BOT_TOKEN=MY_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=MY_GEMINI_API_KEY
```

---

##  Run the Bot

```bash
python sbot.py
```

If everything is configured correctly, you'll see:

```text
SageBot is running...
```

---

##  Future Improvements

- Add `/help` and `/about` commands
- Conversation history
- Better error handling
- Logging
- Unit testing

---

##💻 Author

**Anwesha Gon**

GitHub: https://github.com/angrybird09
