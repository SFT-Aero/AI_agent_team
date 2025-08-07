# Instructions To Run
Navigate to your terminal.

Type in the following commands:

`cd AI_agent_team`

` git pull origin main`

`python3 -m venv myenv`

`source myenv/bin/activate`

`pip install -r requirements.txt && python3 main.py`

Let run for 2-5 minutes until complete.

Type in the following command to retrieve the .csv file:

`mv scraped_articles.csv`

`mv general_signals.csv ~/Downloads/`

`mv economic_signals.csv ~/Downloads/`

Open your Downloads folder to retrieve the desired files.

# AI Agent Web Scraping and Analysis

## 📌 Overview

This script automates the process of:

1. Scraping articles from a list of URLs.
2. Analyzing those articles with two AI agents.
3. Saving the results into clearly structured CSV files.

It helps identify future signals and economically disruptive trends from real-world news and articles.

---

## 🧩 What It Does

### ✅ Step 1: Scrape Articles
- **Input**: `urls.csv` — a file with a list of news article URLs.
- **Output**: `scraped_articles.csv` — raw article data (title, content, etc.).

![Alt Text](webscraper.jpg)

### ✅ Step 2: Analyze with AI Agents
Two agents analyze the articles:
- **Futuristic Agent**: Detects trends and weak signals that may influence the future.
- **Disruptive Economy Agent**: Identifies signals of economic disruption or transformation.

### ✅ Step 3: Save Outputs
Each agent's results are saved to a separate file:
- `general_signals.csv` — results from the Futuristic Agent.
![Alt Text](general.png)

- `economic_signals.csv` — results from the Disruptive Economy Agent.
![Alt Text](economic.png)

---

## 📂 Files & Structure

```plaintext
AI_agent_team/
├── urls.csv                  # Input: list of URLs to scrape
├── scraped_articles.csv      # Output: raw scraped articles
├── general_signals.csv       # Output: futuristic signals
├── economic_signals.csv      # Output: economic signals
└── main.py                 # The main script you run
```

## Contact & Support
For any questions or issues with the script, please contact Shandler A. Mason, shandler.mason@gmail.com, CSPS Summer 2025 MTS Graduate Intern III.

**Created by:** [Shandler A. Mason](https://shandlermason.github.io/sm-portfolio/)

