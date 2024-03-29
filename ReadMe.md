### Files

main.py: Contains all the code for scraping comments from subreddit and summarizing comments based on topics extracted.

test.py: Rouge test to check if the summary generated is accurate or not.

data.xlsx: Contains data extracted after scrapping. 


### Excel file columns

Subreddit: Name of the subreddit from where the data will be extracted

Post Title: Title of the post from the given subreddit

Comment Body: Comments related to the given topic

Sentiment: Sentiment of the specific comment (positive or negative)

Original Text: all the comments concatenated from a single post

Summary Generated: generated summary by the LLM given the original text

Similarity score: Cosine simialirty score of the original text and summary generated. Determines how much similary the generated summary is. 


### Project setup 

1. Clone the repo 

```<git clone url>```

2. Navigate to the project directory:

```cd <project-directory>```

3. Activate virtual environment:

On Windows: ```env\Scripts\activate```

On macOS and Linux: ```source env/bin/activate```


5. Install dependencies from requirements.txt:

```pip install -r requirements.txt```


### Usage

1. Ensure your virtual environment is activated.

2. Run the main script

```streamlit run main.py```

