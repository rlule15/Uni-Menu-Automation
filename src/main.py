# Main entery point for the application
import datetime
import os
from dotenv import load_dotenv

from engine import discord_webhook_send, fetch_menu_data

# Load environment variables from .env file
load_dotenv()

# Today's date in YYYY-MM-DD format
today_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Set env variables
api_key: str | None = os.getenv("API_KEY")
api_url: str | None = f"{os.getenv('API_URL')}{today_date}"
webhook_url: str | None = os.getenv("WEBHOOK_URL")


def main():
    # Exit if essential env variables are missing
    if not api_key or not api_url:
        print("API_KEY or API_URL not set in environment variables.")
        return
    
    if not webhook_url:
        print("WEBHOOK_URL not set in environment variables.")
        return
    
    data = fetch_menu_data(api_url, api_key)

    
    if data:
        title = f"Menu for {today_date}"
        description = "\n\n".join(data.values())
    else:
        title = f"Menu for {today_date}"
        description = "No menu items found."

    res = discord_webhook_send(
        webhook_url,
        title=title,
        description=description)
    
    if res is None:
        print("Failed to send webhook.")
        return
    
    if res.ok:
        print("Webhook sent successfully.")
    else:
        print(f"Failed to send webhook. Status code: {res.status_code}")
        print(f"Response: {res.text}")

if __name__ == "__main__":
    main()
