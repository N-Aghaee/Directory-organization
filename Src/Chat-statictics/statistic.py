import json
from  Src.data import DATA_DIR
import json
from collections import Counter
from hazm import Normalizer,word_tokenize
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display


class ChatStatistics:
    def __init__(self,chat_json):
        # load data
        with open(chat_json) as f:
            self.chat_data = json.load(f)

        self.normalizer = Normalizer()


        # load stopword
        stop_word = open(DATA_DIR /'stopswords.txt').readlines()
        stop_word = list(map(str.strip, stop_word))
        self.stop_word = list(map(self.normalizer.normalize, stop_word))

    def generate_word_cloud(self, output_dir):
        text_content = ''
        for msg in self.chat_data['messages']:
          if type(msg['text']) is str:
            tokens = word_tokenize(msg['text'])
            tokens = list(filter(lambda item: item not in self.stop_word, tokens))
            text_content += f"{''. join(tokens)}"
        
    # normalize, reshape for final word cloud
        text_content = self.normalizer.normalize(text_content)
        text_content = arabic_reshaper.reshape(text_content)
        text_content = get_display(text_content)

    #generate word cloud
        wordcloud = WordCloud(width= 1200, height = 1200,
                          font_path = str(DATA_DIR /'BHoma.ttf'),
                          background_color= 'white',
                          max_font_size= 250).generate(text_content)

        wordcloud.to_file(DATA_DIR/'wordcloud.png')

if __name__ == "__main__":
    chat_stats = ChatStatistics(chat_json =  DATA_DIR /'result.json')
    chat_stats.generate_word_cloud(output_dir = DATA_DIR) 
    print("Done")