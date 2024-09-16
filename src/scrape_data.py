import requests
from bs4 import BeautifulSoup

def scrape_web_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract all the text content from the page
        text_content = soup.get_text(separator="\n", strip=True)

        # Save the scraped content to a text file
        text_file_path = 'text_storage.txt'
        with open(text_file_path, 'w') as f:
            f.write(text_content)
        print("Web scraping completed. Data saved to text file.")

    except Exception as e:
        print(f"An error occurred during scraping: {e}")

if __name__ == "__main__":
    # Example URL to scrape
    url = "https://medium.com/gooddata-developers/a-way-to-production-ready-ai-analytics-with-rag-0c71fc3b23e8"
    scrape_web_content(url)
