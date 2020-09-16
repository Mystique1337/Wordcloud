#Import the required libraries
from wordcloud import WordCloud, STOPWORDS
#Open the text file which will be used for the wordcloud
words_file = open("words.txt", "r").read()

def create_word_cloud(string):
   """Creates the wordcloud"""
   cloud = WordCloud(background_color = "black", max_words = 40, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.jpg")

words_file = words_file.lower()  #turns text to lowercase
create_word_cloud(words_file) # creates the word cloud