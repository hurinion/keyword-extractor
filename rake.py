import re

def seperate_to_sentences(paragraph:str) -> list: 
    return re.split(r"[.,!?;]", paragraph.lower())

def retrieve_file(filename_stopword:str) -> list:
    with open(filename_stopword) as f:
        stopword_list = [line.rstrip() for line in f]
    return stopword_list

def generate_stopwords(stopword_list:list) -> list:
    stopword_pattern = [r'\b' + word + r'(?![\w-])' for word in stopword_list]
    return re.compile('(?u)' + '|'.join(stopword_pattern), re.IGNORECASE)
    
def seperate_to_words(sentence_list:list, stopwords:list) -> list: 
    phrase_list = [re.split(stopwords, sentence) for sentence in sentence_list]
    return [string.lower().strip() for phrase in phrase_list for string in phrase if string.strip()]


class rake(object):

    def __init__(self, filename_stopword) -> None:
        """
        filename_stopword : str
        """
        self.__stopwords = generate_stopwords(retrieve_file(filename_stopword))
        self.__text_input = "Look Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over."

    def run(self) -> list:
        sentence_list = seperate_to_sentences(self.__text_input)
        phrase_list = seperate_to_words(sentence_list, self.__stopwords)
        return phrase_list
        
obj = rake('stop_words_english.txt')

print(obj.run())


