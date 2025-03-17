#Persian Calendar Teller Bot

This Telegram bot is designed to send the current date along with its Gregorian equivalent to a specified Telegram channel. The dates are displayed in both Persian and English, including information about the current day and the next day.

## Features
- Retrieves the Jalali (Persian) and Gregorian dates
- Displays the weekday names in Persian and English
- Sends the date to a specific Telegram channel
- Checks if the bot is an admin in the channel
- Can be modified for automated daily messages

## Requirements
To run this bot, you need:
- **Python 3**
- **Required Libraries**:
  - `telepot`
  - `jdatetime`

Install the required libraries using:
```sh
pip install telepot jdatetime
```

## Usage
1. **Obtain your bot token:**
   - Create a new bot using BotFather on Telegram and get its token.
2. **Set the channel ID:**
   - Add the bot to your channel and make it an admin.
   - Assign the channel ID to the `CHANNEL_ID` variable in the script.
3. **Run the script:**
   - Execute the following command in your terminal:
   ```sh
   python Persian-Calendar-Teller-Bot.py
   ```
   - If the bot is an admin, it will send the current and next day's date to the channel.

## Automating Message Sending
To automate daily messages, you can use `cronjob` on Linux or `Task Scheduler` on Windows.

### Method 1: Using `cronjob` on Linux
1. Edit the `crontab`:
   ```sh
   crontab -e
   ```
2. Add the following line to run the script every day at 9 AM:
   ```sh
   0 9 * * * /usr/bin/python3 /path/to/Persian-Calendar-Teller-Bot.py
   ```

### Method 2: Using `Task Scheduler` on Windows
1. Open `Task Scheduler`.
2. Create a new task and set it to run at a specified time.
3. Use `python.exe` to execute `Persian-Calendar-Teller-Bot.py` from the specified directory.

## Security Tips
- Do not expose your bot token in public repositories like GitHub.
- Use environment variables (`.env` file) to store sensitive data securely.

## License
This project is licensed under the **MIT** License, allowing free use and modification.

