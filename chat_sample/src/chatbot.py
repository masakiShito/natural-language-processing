import json
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Chatbot:
    def __init__(self, corpus_path):
        with open(corpus_path, 'r', encoding='utf-8') as file:
            self.responses = json.load(file)
        self.tokenizer = Tokenizer()
        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize, stop_words=None)
        self.vectorizer.fit(self.responses.keys())

    def tokenize(self, text):
        """
        テキストをトークン化する関数
        :param text: str, テキスト
        :return: list, トークンのリスト
        """
        return [token.surface for token in self.tokenizer.tokenize(text)]

    def get_response(self, user_input):
        """
        ユーザーの入力に基づいて適切な応答を返す関数
        :param user_input: str, ユーザーの入力
        :return: str, 応答メッセージ
        """
        user_tfidf = self.vectorizer.transform([user_input])
        response_tfidf = self.vectorizer.transform(self.responses.keys())
        
        similarities = cosine_similarity(user_tfidf, response_tfidf).flatten()
        max_similarity_index = similarities.argmax()
        max_similarity = similarities[max_similarity_index]

        print("\n--- 類似度のログ ---")
        for i, key in enumerate(self.responses.keys()):
            print(f"入力: {user_input} | コーパス: {key} | 類似度: {similarities[i]:.2f}")
        print("-------------------\n")

        if max_similarity < 0.4:
            return "すみません、よくわかりません。"

        response_key = list(self.responses.keys())[max_similarity_index]
        return self.responses[response_key]
