from src.japanese_stopwords import japanese_stopwords

def remove_stopwords(tokens):
    """
    トークンからストップワードを除去する関数
    :param tokens: list, トークンのリスト
    :return: list, ストップワードが除去されたトークンのリスト
    """
    stop_words = set(japanese_stopwords)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens
