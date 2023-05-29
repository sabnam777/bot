Copy

# Real-ESRGAN Telegram Bot

A Telegram bot that uses the [Real-ESRGAN](https://replicate.com/nightmareai/real-esrgan/api) API to enhance image quality.

## Installation

### Using Docker

1. Clone the repository:
git clone https://github.com/yourusername/real-esrgan-telegram-bot.git
Copy


2. Create a `.env` file in the root directory of the project and fill in the required environment variables:
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
REPLICATE_API_TOKEN=your_replicate_api_token
Copy


3. Build and run the Docker container:
docker-compose up -d
Copy


### Without Docker

1. Clone the repository:
git clone https://github.com/yourusername/real-esrgan-telegram-bot.git
Copy


2. Install the required dependencies:
pip install -r requirements.txt
Copy


3. Set up your Telegram bot token and Replicate API token as environment variables:
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
export REPLICATE_API_TOKEN="your_replicate_api_token"

4. Run the bot:
