from src.chatbot import Chatbot

def main():
    bot = Chatbot('corpus/corpus.json', 'data/user_data.json')
    print("チャットボットへようこそ！終了するには「終了」と入力してください。")

    while True:
        user_input = input("あなた: ")
        if user_input == "終了":
            print("チャットボット: さようなら！")
            break
        
        response = bot.get_response(user_input)
        print(f"チャットボット: {response}")

if __name__ == "__main__":
    main()
