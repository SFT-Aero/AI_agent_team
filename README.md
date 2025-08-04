# AI_agent_team
1. Navigate to the correct directory
2. Run 'pip install -r requirements.txt' to install all the project dependencies
3. Verify that the packages were installed 'pip list'

# Quick Overview: How Our Web Scraper Gathers News Articles

## What does this tool do?

- It **visits a list of websites** (news sources) and collects articles automatically.
- From each article, it extracts important details like:
  - Title
  - Link (URL)
  - Date (when published)
  - Category or topic
  - A short teaser or summary
  - The full article body text
  - Images related to the article

## How it works — simply:

1. We provide the scraper with a list of website URLs from a CSV file.
2. The scraper **goes to each website** and finds article sections.
3. It **pulls out the key info** from each article using common patterns on news sites.
4. All gathered articles are saved into a CSV file for easy review and later use.

## Why is this useful?

- It saves **hours of manual research** by collecting news automatically.
- Gives us **fresh, relevant data** to feed our AI agents for analysis.
- Helps keep track of trends by monitoring multiple sources regularly.
- Makes sure we get detailed info (like dates and images) for better insights.

# Quick Overview: How Our AI Finds Future Signals in News Articles

## What does this code do?

- **Reads news articles** from a list (with titles and short summaries).
- **Asks an AI “expert”** to find the top 5 articles that show early signs of important future changes in society, technology, or the economy.
- The AI **explains why each article is important** (called a “justification”).
- The results are **saved into a spreadsheet** (CSV file) with the article titles and the AI’s explanations.

## How it works — simply:

1. We prepare a list of news articles.
2. We create a task for the AI to analyze those articles and pick the most important ones.
3. The AI returns a clear, numbered list of articles with reasons why they matter.
4. We take that list and save it neatly in a CSV file for easy reading and sharing.

## Why is this useful?

- It helps us **spot early trends and risks** before they become obvious.
- Makes **complex news easier to understand** by summarizing key future signals.
- Helps guide **strategic planning and decision making** with AI-powered insights.

