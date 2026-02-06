# Uni-Menu-Automation
Simple python script that gets the dinning hall menu, cleans up the data, and sends me a message on discord with the information

## Getting Started

### Prerequisites
You will need the following credentials:
- **Discord Webhook url**
- **Menu API URL** (and Key if required)

### Setup
1. **Clone the repo** and navigate to the project folder
2. **Create a .env file** based on the .env.example file structure

### Running with docker
1. Build the image - ```docker build -t uni-menu-automation-py .```
2. Run the app with you env file  ```docker run --env-file .env uni-menu-automation-py```
    - Alternatively, you can pass the variables directly in the command line  ```docker run -e DISCORD_WEBHOOK_URL="your_url_here" uni-menu-automation-py``` 
