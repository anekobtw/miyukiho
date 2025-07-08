# Moderation bot

# 🛠️ How to install

## Linux

```bash
# Update everything
sudo apt update
sudo apt upgrade

# Creating virtual environment
python3 -m venv .venv
source .venv\bin\activate
cd src
pip install -r requirements.txt

# Installing postgres
sudo apt install postgresql postgresql-contrib  # if you're on Liunux
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo -i -u postgres
psql
ALTER USER postgres PASSWORD 'yourpassword';  # SET YOUR PASSWORD
```

## Windows

https://www.python.org/downloads/ - Install Python

https://www.postgresql.org/download/windows/ - Install postgres

```bash
# Creating virtual environment
python3 -m venv .venv
.\.venv\scripts\activate
cd src
pip install -r requirements.txt
```
