from src.tokenizer import tokenize
from src.stopword_removal import remove_stopwords
from src.word_frequency import count_word_frequency

# 処理するサンプルテキスト
text = "自然言語処理（NLP）は、コンピュータと人間の間で自然言語を使用して相互作用することに関する人工知能の一分野です。"

# トークン化：テキストを単語に分割する
tokens = tokenize(text)
print("トークン:", tokens)

# ストップワードの除去：意味をほとんど持たない一般的な単語を除去する
filtered_tokens = remove_stopwords(tokens)
print("フィルタリングされたトークン:", filtered_tokens)

# 単語の頻度解析：各単語の出現回数をカウントする
word_freq = count_word_frequency(filtered_tokens)
print("単語の頻度:", word_freq)

# 結果をファイルに保存する（オプション）
with open("word_frequencies.txt", "w") as f:
    for word, freq in word_freq.items():
        f.write(f"{word}: {freq}\n")
