from typing import Optional
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

# List of desired menu groups
wanted_groups = [
    "BLISS",
    "SAVORY",
    "SIZZLE",
    "SIMPLE SERVINGS"
    ]

# Function to get menu data from API
def fetch_menu_data(url: str, api_key) -> dict:
    # Dictionary to hold cleaned menu data
    cleaned_menu = {}

    headers = {
        "API-Key": api_key,
        "Accept": "application/json"
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            data = res.json()

            # Loop through the nested JSON to find menu items
            for menu in data:
                menu_list = f"### {menu['name']} ###\n"
                menu_list += "-" * (len(menu['name']) + 7) + "\n"
                for group in menu.get('groups', []):
                    if group['name'] in wanted_groups:
                        menu_list += f"**\n{group['name']}**\n"
                        for item in group.get('items', []):
                            menu_list += f"- {item['formalName']}\n"
                    cleaned_menu[menu['name']] = menu_list
            return cleaned_menu
        else:
            res.raise_for_status()
            return {}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching menu data: {e}")
        return {}

def discord_webhook_send(webhook_url: str, title: str, description: str) -> Optional[requests.Response]:
    res: Optional[requests.Response]= None
    try:
        if not description:
            description = "No menu items found."

        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title=title, description=description, color='03b2f8')
        webhook.add_embed(embed)
        res = webhook.execute()

        return res
    except Exception as e:
        print(f"Error sending webhook: {e}")
        return res