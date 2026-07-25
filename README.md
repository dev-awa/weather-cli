# ☁️ Weather CLI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange.svg)

**A powerful command-line weather application built with Python**

[Installation](#-installation) •
[Usage](#-usage) •
[Features](#-features) •
[API Reference](#-api-reference) •
[Contributing](#-contributing)

</div>

---

## 📖 About

**Weather CLI** is a lightweight and feature-rich command-line tool that fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/api). Built with Python, this project demonstrates:

- 🌐 **API Integration** - Making HTTP requests to REST APIs
- 🎯 **CLI Development** - Building professional command-line interfaces
- 💾 **Caching Strategies** - Optimizing performance with intelligent caching
- 🎨 **User Experience** - Colorful and readable terminal output

Perfect for developers learning API integration, Python CLI development, or anyone who wants quick weather updates from their terminal!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌍 **City Lookup** | Get weather for any city worldwide |
| 🌡️ **Unit Selection** | Switch between metric (°C) and imperial (°F) |
| 💾 **Smart Caching** | Cache results for 10 minutes to reduce API calls |
| 🔄 **Force Refresh** | Bypass cache with `--force` flag |
| 🎨 **Colored Output** | Beautiful, color-coded terminal display |
| 📖 **Built-in Help** | Comprehensive help with `--help` |
| 🚀 **Lightweight** | Minimal dependencies, fast execution |

---

## 📸 Screenshot

```bash
🌍 City: Tehran, IR
🌡️  Temp: 24°C
🌡️  Feels like: 22°C
☁️  Weather: Clear Sky
💧 Humidity: 45%
💨 Wind: 12 km/h
```

---

🛠️ Installation

Prerequisites

· Python 3.8 or higher
· OpenWeatherMap API Key (free)

Step-by-Step Setup

```bash
# 1. Clone the repository
git clone git@github.com:dev-awa/weather-cli.git
cd weather-cli

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env and add your API_KEY

# 5. Run the application
python weather.py --help
```

---

🚀 Usage

Basic Commands

```bash
# Get weather for Tehran (default)
python weather.py

# Get weather for a specific city
python weather.py --city London

# Use imperial units (°F)
python weather.py --city NewYork --units imperial

# Force refresh (ignore cache)
python weather.py --city Paris --force

# Display help
python weather.py --help
```

Command Options

Option Description Default

--city City name to get weather for Tehran

--units Unit system: metric or imperial metric

--force Ignore cache and fetch fresh data False

--help Show help message -

Example Output

```bash
$ python weather.py --city Tokyo --units metric

🌍 City: Tokyo, JP
🌡️  Temp: 28°C
🌡️  Feels like: 30°C
☁️  Weather: Partly Cloudy
💧 Humidity: 65%
💨 Wind: 8 km/h
```

---

📂 Project Structure

```
weather-cli/
├── .gitignore              # Git ignore rules
├── .env.example            # Environment variables template
├── .env                    # Environment variables (not tracked)
├── LICENSE                 # MIT License
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── weather.py              # Main CLI application
├── src/
│   └── cache_manager.py    # Caching logic
└── cache/                  # Cache directory (auto-generated)
```

---

🔧 Dependencies

Library Version Purpose

Requests 2.31.0 HTTP requests to API

python-dotenv 1.0.0 Environment variable management

Click 8.1.7 CLI interface framework

Colorama 0.4.6 Colored terminal output

---

🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: git checkout -b feature/amazing-feature
3. Commit your changes: git commit -m 'feat: add amazing feature'
4. Push to the branch: git push origin feature/amazing-feature
5. Open a Pull Request

Development Workflow

```bash
# Create a new branch
git checkout -b feature/your-feature

# Make your changes and commit
git add .
git commit -m "feat: describe your changes"

# Push to remote
git push origin feature/your-feature

# After PR approval, clean up
git checkout main
git pull origin main
git branch -d feature/your-feature
git push origin --delete feature/your-feature
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🙏 Acknowledgments

· OpenWeatherMap for providing the weather data API

· The Python community for amazing libraries and tools

· All contributors and users of this project

---

## 📬 Contact & Support

- **Author**: [dev-awa](https://github.com/dev-awa)
- **Repository**: [github.com/dev-awa/weather-cli](https://github.com/dev-awa/weather-cli)
- **Issues**: [Report a bug](https://github.com/dev-awa/weather-cli/issues)
- **Pull Requests**: [Submit a PR](https://github.com/dev-awa/weather-cli/pulls)

---

<div align="center">

**⭐ Star this repo if you found it useful!**

Made with ❤️ by [dev-awa](https://github.com/dev-awa)

</div>