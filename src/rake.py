import re

class rake(object):

    def __init__(self, stopword_filename, input_filename) -> None:
        """
        stopword_filename : str
        """
        self.__stopwords = self.generate_stopwords(self.retrieve_file(stopword_filename))
        self.__text_input = ' '.join(self.retrieve_file(input_filename))

    def run(self) -> list:
        sentence_list = self.seperate_to_sentences(self.__text_input)
        phrase_list = self.seperate_to_words(sentence_list, self.__stopwords)
        return sorted(self.score_keywords(phrase_list), key=lambda x: -x[1])

    "###################################################"
    
    def seperate_to_sentences(self, paragraph:str) -> list: 
        return re.split(r"[.,!?;]", paragraph.lower())

    def retrieve_file(self, filename:str) -> list:
        with open(filename) as f:
            output_list = [line.rstrip() for line in f]
        return output_list

    def generate_stopwords(self, stopword_list:list):
        stopword_pattern = [r'\b' + word + r'(?![\w-])' for word in stopword_list]
        return re.compile('(?u)' + '|'.join(stopword_pattern), re.IGNORECASE)
        
    def seperate_to_words(self, sentence_list:list, stopwords:list) -> list: 
        phrase_list = [re.split(stopwords, sentence) for sentence in sentence_list]
        return [string.lower().strip() for phrase in phrase_list for string in phrase if string.strip()]

    def score_keywords(self, keyword_list):
        unique_keywords = set(keyword_list)
        return [(word, keyword_list.count(word)) for word in unique_keywords if keyword_list.count(word) > 1]

keywords = rake('stop_words_english.txt', 'input.txt')

print(keywords.run())


