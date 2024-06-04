import json
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

class Chatbot:
    def __init__(self, corpus_path, user_data_path):
        self.corpus_path = corpus_path
        self.user_data_path = user_data_path
        self.tokenizer = Tokenizer()

        # コーパスのロード
        with open(corpus_path, 'r', encoding='utf-8') as file:
            self.responses = json.load(file)

        # ユーザーデータのロードまたは初期化
        if os.path.exists(user_data_path):
            with open(user_data_path, 'r', encoding='utf-8') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = {}

        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize, stop_words=None)
        self.vectorizer.fit(list(self.responses.keys()) + list(self.user_data.keys()))

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
        all_responses = {**self.responses, **self.user_data}
        user_tfidf = self.vectorizer.transform([user_input])
        response_tfidf = self.vectorizer.transform(all_responses.keys())
        
        similarities = cosine_similarity(user_tfidf, response_tfidf).flatten()
        max_similarity_index = similarities.argmax()
        max_similarity = similarities[max_similarity_index]

        print("\n--- 類似度のログ ---")
        for i, key in enumerate(all_responses.keys()):
            print(f"入力: {user_input} | コーパス: {key} | 類似度: {similarities[i]:.2f}")
        print("-------------------\n")

        if max_similarity < 0.4:
            # 新しい入力に対して応答を学習
            print("新しい質問ですね。どのように応答すればよいですか？")
            new_response = input("応答: ")
            self.user_data[user_input] = new_response
            self.save_user_data()
            return new_response

        response_key = list(all_responses.keys())[max_similarity_index]
        return all_responses[response_key]

    def save_user_data(self):
        """
        ユーザーデータを保存する関数
        """
        with open(self.user_data_path, 'w', encoding='utf-8') as file:
            json.dump(self.user_data, file, ensure_ascii=False, indent=4)
