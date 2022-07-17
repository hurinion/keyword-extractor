import re

def seperate_to_sentences(paragraph:str) -> list: 
    return re.split(r"[.,!?;]", paragraph.lower())

def retrieve_file(filename_stopword:str) -> list:
    with open(filename_stopword) as f:
        stopword_list = [line.rstrip() for line in f]
    return stopword_list

def generate_stopwords(stopword_list:list):
    stopword_pattern = [r'\b' + word + r'(?![\w-])' for word in stopword_list]
    return re.compile('(?u)' + '|'.join(stopword_pattern), re.IGNORECASE)
    
def seperate_to_words(sentence_list:list, stopwords:list) -> list: 
    phrase_list = [re.split(stopwords, sentence) for sentence in sentence_list]
    return [string.lower().strip() for phrase in phrase_list for string in phrase if string.strip()]

def score_keywords(keyword_list):
    unique_keywords = set(keyword_list)
    return [(word, keyword_list.count(word)) for word in unique_keywords if keyword_list.count(word) > 2]



class keyword_extraction(object):

    def __init__(self, stopword_filename, input_filename) -> None:
        """
        stopword_filename : str
        """
        self.__stopwords = generate_stopwords(retrieve_file(stopword_filename))
        self.__text_input = ' '.join(retrieve_file(input_filename))

    def run(self) -> list:
        sentence_list = seperate_to_sentences(self.__text_input)
        phrase_list = seperate_to_words(sentence_list, self.__stopwords)
        return sorted(score_keywords(phrase_list), key=lambda x: -x[1])

keywords = keyword_extraction('stop_words_english.txt', 'test.txt')

print(keywords.run())

