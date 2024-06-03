from janome.tokenizer import Tokenizer

def tokenize(text):
    """
    テキストをトークン（単語）に分割する関数
    :param text: str, 入力テキスト
    :return: list, トークンのリスト
    """
    t = Tokenizer()
    tokens = [token.surface for token in t.tokenize(text)]
    return tokens
