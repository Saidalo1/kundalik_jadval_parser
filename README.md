
# Kundalik Parser (selenium)

This is a script to get schedule from kundalik.com, save to PostgreSQL database and send schedule for today in telegram bot


## Installation for Linux & MacOS

Google Chrome (required)

```bash
  sudo apt update
  sudo apt install chromium
```

Required libraries for the project

```bash
  sudo pip3 install -r requirements.txt
```    

## Installation for Windows

Google Chrome (required)

```bash
  https://www.google.com/intl/en/chrome/
```

Required libraries for the project

```bash
  pip install -r requirements.txt
```    
## Create .env file

To import data create an .env file and write this data

```bash
  # Kundalik settings
    LOGIN=kundalikcomloginFORPUPILACCOUNT
    PASSWORD=kundalikcompasswordFORPUPILACCOUNT

    # Database settings
    DATABASE_NAME=DATABASE_NAME
    DATABASE_USER=DATABASE_USER
    DATABASE_PASS=DATABASE_PASS
    DATABASE_HOST=DATABASE_HOST

    # Telegram bot token
    TOKEN=TELEGRAMBOTTOKEN
```
## Script.py to crontab
Add script.py to crontab for update database every N time!

## How to Run for Linux & MacOS

```bash
python3 main.py
```

## How to Run for Windows

```bash
python main.py
```


## Features

- Easier to manage
- No need to open an online diary: kundalik.com
- Without advertising
- Works fast


## Feedback

If you have any feedback, please reach out to us at saidakhmedovsaidalo@gmail.com


## Screenshots

![App Screenshot](https://imgur.com/pGD0PN6.png)

![App Screenshot](https://imgur.com/WbbViHY.png)

If schedule not found: 
![App Screenshot](https://imgur.com/sqD7U2D.png)

