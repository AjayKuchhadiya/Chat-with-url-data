# Web Scraper and Question-Answering Chatbot

This project implements a web scraping tool and a chatbot that provides answers based on the scraped data. The project uses `BeautifulSoup` for web scraping and `langchain_groq` for natural language processing capabilities.

## Approach

### Web Scraping (`scrape_data.py`):
- The script extracts all textual content from a given web page using `BeautifulSoup`.
- The extracted text is saved to a file (`text_storage.txt`) for later use.
  
### Question-Answering Chatbot (`chatbot.py`):
- The chatbot is powered by the `ChatGroq` language model (Llama3-8b-8192).
- It reads the scraped content from `text_storage.txt` and answers user queries based on that content.
- A custom template ensures the chatbot provides precise responses without additional explanations.

### Task Workflow:
1. **Scraping the Website:**
   - `scrape_data.py` extracts the content from a URL and saves it in a text file.
2. **Running the Chatbot:**
   - `chatbot.py` loads the scraped content and answers user queries by analyzing the data.
   
## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/AjayKuchhadiya/Chat-with-url-data.git
cd Chat-with-url-data
```

### Step 2: Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
# or 
.\venv\Scripts\activate    # For Windows
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the root directory with the necessary environment variables:

```bash
# Example .env file
GROQ_API_KEY=your_groq_api_key
```

## Running the Application

### Step 1: Scrape Web Content

- Open `scrape_data.py` and set the URL you want to scrape.
- Run the following command:

```bash
cd src
python scrape_data.py
```

This will scrape the content from the specified webpage and save it to `text_storage.txt`.

### Step 2: Run the Chatbot

- After the content is scraped, run `chatbot.py` to interact with the chatbot and ask questions based on the scraped data:

```bash
cd src
python chatbot.py
```

- The chatbot will prompt you to enter your queries and will generate answers based on the scraped content.

### Example Usage:

1. First, scrape data from a webpage using:

```bash
python scrape_data.py
```

2. Then, interact with the chatbot:

```bash
python chatbot.py
```

## Output

- The scraped data is stored in `text_storage.txt`.
- The chatbot will print responses to the console based on the questions you ask.
  
## Notes

- Ensure you have an active internet connection to use the `ChatGroq` model in `chatbot.py`.
- If you encounter any issues, check that your environment variables (e.g., API keys) are correctly set up in the `.env` file.

```
