import praw
import pandas as pd
import re
from transformers import pipeline
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

reddit = praw.Reddit(
    client_id="94Fia5p1XAlfzYldSfZJbA",
    client_secret="yGxdSIwXgIbUdSzlXdh-b-79_1MDGg",
    user_agent="my-application",
)


def filter_data(text):
    """
    function to clean the extracted comments.
    """
    clean_text = re.sub(r"<.*?>", "", text)
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    clean_text = url_pattern.sub("", clean_text)
    clean_text = re.sub(r'<[^>]*>',"",clean_text)
    clean_text = re.sub(r'[<>!]', '', clean_text)
    clean_text = re.sub(r"\s+", " ", clean_text)
    filter_text = re.compile(r"[^\x00-\x7F]+")
    clean_text = filter_text.sub("", clean_text)
    return clean_text

def get_summary(text):
    """
    function to summarize all comments per topic
    """
    model_path = "google-t5/t5-base"
    summarizer = pipeline("summarization", model=model_path, tokenizer=model_path)
    summary = summarizer(text, max_length=512)
    return summary[0]["summary_text"]


def get_sentiment(text):
    """
    returns entiments for each comments
    """
    sentiment_task = pipeline(
        "sentiment-analysis"
    )
    output = sentiment_task(text)
    result = output[0]["label"]
    return result



def reddit_comments(subreddit:str):
    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.top(limit=3)
    data = []
    extended_data = []
    for post in posts:
        post_title = post.title
        text=""
        for comment in post.comments[:5]:
            if isinstance(comment, praw.models.Comment):
                body = comment.body
                body = filter_data(body)
                sentiment = get_sentiment(body)
                text += body + " "
                
                data.append({'Subreddit':f"r/{subreddit}",'Post Title': post_title, 'Comment Body': body,"Sentiment":sentiment})
        summary = get_summary(text)
        summary = str(summary)
        nltk.word_tokenize(text.lower())
        nltk.word_tokenize(summary.lower())
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text, summary])
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        similarity_score = cosine_sim[0][0]
        extended_data.extend(data)
        extended_data.append({"Original Text":text,"Summary Generated":summary,"Similarity score":similarity_score})
        data = []
        
    df = pd.DataFrame(extended_data)
    return df


if __name__== "__main__":
    # subreddit_name = "news"
    subreddit_name = "technology"
    df = reddit_comments(subreddit_name)
    df.to_excel('data.xlsx', index=False)