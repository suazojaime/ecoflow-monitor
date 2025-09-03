# EcoFlow Monitor

A containerized Python service that monitors EcoFlow battery status and sends updates to an API (like Telegram) every 5 minutes using cron inside Docker.

---

## 🚀 Features

- ⏱️ Runs every 5 minutes using cron (inside the container)
- 🐳 Fully containerized with Docker + Docker Compose
- 🔐 Uses `.env` for secret configuration (kept out of version control)
- 📤 Sends updates via HTTP API (e.g., Telegram)
- 🔄 Auto-restart if container stops

---

## 🧪 Project Structure

├── main.py # Main script entry point
├── eco_values.py # Logic to get EcoFlow values
├── telegram_api.py # Sends updates to your API
├── cronjob # Cron schedule config
├── dockerfile # Docker image build file
├── compose.yml # Docker Compose setup
├── .env.example # Environment variable template
└── README.md # You're here


## ⚙️ Usage

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ecoflow-monitor.git
cd ecoflow-monitor
```

### Create .env file
cp .env.example .env

```env
access_key = *** 
secret_key = ***
device_sn = ***
telegram_token = ***
chat_id = ***
```

### Build and start the container

```bash
docker compose up --build -d
```

### How it works

- The container starts and runs cron

- Every minute, main.py is triggered

- eco_values.py collects battery data via EcoFlow API

- telegram_api.py (or your own API client) sends the data

- Output is optionally logged under /var/log inside the container

### Enviromental variables

All sensitive config is stored in .env (not committed):

| Variable             | Description                 |
| -------------------- | --------------------------- |
| `device_sn`     | Your EcoFlow device serial  |
| `secret_key` | Your EcoFlow API secret key |
| `access_key` | Your EcoFlow API access key |
| `telegram_token`     | Telegram bot token          |
| `chat_id`   | Telegram chat/channel ID    |


### License

MIT — free to use, modify, and share.
