import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from moviepy.editor import VideoFileClip
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# document = """
#     Apple is looking at buying U.K. startup for $1 billion. The deal is expected to close by Q3 2024. 
#     Tim Cook, Apple's CEO, said this is an important step for the company's expansion in Europe.
# """



document  = """

The new software update has been a complete disaster. Since installing it, the system has become unbearably slow, with frequent crashes that disrupt work and lead to data loss. The interface is confusing and unintuitive, making even basic tasks frustrating and time-consuming. Customer support has been unresponsive, offering no solutions or even acknowledging the issues. Overall, the update has been a major disappointment, significantly diminishing productivity and leaving users dissatisfied.
"""
doc = nlp(document)

# print(doc)

# Tokenization
tokens = [token.text for token in doc]
# print("Tokens:", tokens)

# Part-of-Speech Tagging
pos_tags = [(token.text, token.pos_) for token in doc]
# print("POS Tags:", pos_tags)

# Named Entity Recognition
entities = [(entity.text, entity.label_) for entity in doc.ents]
# print("Entities:", entities)

# Dependency Parsing
dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
# print("Dependencies:", dependencies)

# Sentence Segmentation
sentences = list(doc.sents)
# print("Sentences:", sentences)

# Lemmatization
lemmas = [(token.text, token.lemma_) for token in doc]
# print("Lemmas:", lemmas)


# Analyze sentiment
blob = TextBlob(document)
sentiment = blob.sentiment

print("Sentiment:", sentiment)


# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([document])
features = vectorizer.get_feature_names_out()
scores = X.toarray()[0]

# Extract top keywords
keyword_scores = dict(zip(features, scores))
sorted_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)

# print("Top Keywords:", sorted_keywords[:10])

labels = ['Terms','terms','website','Website','Condition','condition','location','']

# first analyze sentiment from document


def analyze_sentiment(polarity,subjectivity):
    if polarity > 0.1:
        sentiment_result = "Positive"
    elif polarity < -0.1:
        sentiment_result = "Negative"
    else:
        sentiment_result = "Neutral"
    
    if subjectivity > 0.5:
        subjectivity_result = "Subjective"
    else:
        subjectivity_result = "Objective"
    
    return sentiment_result, subjectivity_result

sentiment_result, subjectivity_result = analyze_sentiment(
    polarity=sentiment.polarity,
    subjectivity=sentiment.subjectivity
)

# print(f"Sentiment Analysis Result: {sentiment_result}")
# print(f"Text is {subjectivity_result}")

# extract audio from video using moviepy library

def extract_audio_from_video(video_path, audio_path):
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract the audio from the video
    audio = video.audio
    
    # Write the audio to a file
    audio.write_audiofile(audio_path)
    
    print(f"Audio extracted and saved to {audio_path}")

# Example usage
video_path = 'Project 1.avi'
audio_path = 'audio.wav'
extract_audio_from_video(video_path, audio_path)