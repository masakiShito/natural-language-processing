from collections import Counter

def count_word_frequency(tokens):
    """
    トークンの頻度をカウントする関数
    :param tokens: list, トークンのリスト
    :return: dict, 各トークンの出現回数を示す辞書
    """
    word_freq = Counter(tokens)
    return word_freq
