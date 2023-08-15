import json
from  Src.data import DATA_DIR

class ChatStatistics:
    def __init__(self,chat_json):
        with open(chat_json) as f:
            self.chat_json = json.load(f)
if __name__ == "__main__":
    chat_stats = ChatStatistics(chat_json= DATA_DIR / 'result.json')

    print("HOOOO")