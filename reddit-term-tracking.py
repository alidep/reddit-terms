import praw
from collections import defaultdict
from datetime import datetime
import csv

# Step 1: Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='JNBneD5vYI4mWbNnrQ0p0Q',        # Replace with your client_id
    client_secret='q258qwajHs1hIMhejJs4Q27Km9MJ4w',# Replace with your client_secret
    user_agent='trends by flourescentblue'       # Replace with your user_agent (e.g., 'RedditTermTracker/0.1 by YourUsername')
)

# Step 2: Define the terms to track
search_terms = [
    "Cultural Marxism", "Socialism", "Communism", "Globalists",
    "Deep State", "Open Borders", "Woke", "Woke Mind Virus",
    "Critical Race Theory", "DEI", "Antifa", "The Great Replacement",
    "SJW", "Gender Ideology", "Transgender Agenda", "Cultural Elites",
    "Radical Left", "Gay Lobby", "Fake News"
]

# Set up a data structure to hold the results
start_year = 2010
end_year = 2024
term_counts_by_year = defaultdict(lambda: {year: 0 for year in range(start_year, end_year + 1)})

# Query Reddit for each term and aggregate results by year
for term in search_terms:
    print(f"Searching for term: {term}")
    for submission in reddit.subreddit('all').search(term, time_filter='all', limit=1000):
        year = datetime.fromtimestamp(submission.created_utc).year
        if start_year <= year <= end_year:
            term_counts_by_year[term][year] += 1

# Output the results
for term, counts in term_counts_by_year.items():
    print(f"{term}: {counts}")

# Save the results to a CSV file
with open('reddit_term_counts.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Term", "Year", "Count"])
    for term, counts in term_counts_by_year.items():
        for year in range(start_year, end_year + 1):
            writer.writerow([term, year, counts[year]])

print("Data collection complete. Results saved to 'reddit_term_counts.csv'.")