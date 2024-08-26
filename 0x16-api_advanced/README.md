# 0x16. API Advanced

## About
This project is focused on advanced usage of APIs, specifically using the Reddit API to gather data, process it, and display results according to specific requirements. The project includes tasks such as making recursive API calls, handling pagination, and sorting results.

## Project Files

### 0-subs.py
**Function:** `number_of_subscribers(subreddit)`

- **Description:** Queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is provided, the function returns 0.

### 1-top_ten.py
**Function:** `top_ten(subreddit)`

- **Description:** Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If the subreddit is invalid, it prints `None`.

### 2-recurse.py
**Function:** `recurse(subreddit, hot_list=[])`

- **Description:** A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, it returns `None`.

### 100-count.py
**Function:** `count_words(subreddit, word_list)`

- **Description:** A recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords (case-insensitive). Results are printed in descending order by count, and alphabetically if counts are the same. Words with no matches are skipped.
