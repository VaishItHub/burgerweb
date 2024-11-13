import wikipediaapi
from wikipediaapi import *

# Define user-agent for Wikipedia access
user_agent = "MyWikipediaApp/1.0 (Contact: your-email@example.com)"
wiki_wiki = Wikipedia(language='en',user_agent=user_agent)

def fetch_and_save_summary(topic):
    # Retrieve the Wikipedia page for the given topic
    page = wiki_wiki.page(topic)

    # Check if the page exists
    if page.exists():
        # Define the filename for the output text file
        filename = f"{topic.replace(' ', '_')}.txt"
        
        # Write the page summary to the file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Title: {page.title}\n")
            file.write("Summary:\n")
            file.write(page.summary)
        
        print(f"Summary for '{topic}' has been saved to '{filename}'")
    else:
        print(f"The page '{topic}' does not exist.")

# Input topics as a list
topics = input("Enter the topics separated by commas: ").split(',')

# Fetch and save each topic's summary
for topic in topics:
    topic = topic.strip()  # Remove any leading/trailing whitespace
    fetch_and_save_summary(topic)