def chatbot():
    print("Hello! I'm ChatBot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("ChatBot: Goodbye! Have a great day.")
            break

        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hi there! How can I help you today?")

        elif 'how are you' in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm doing great! What about you?")

        elif 'your name' in user_input:
            print("ChatBot: I'm ChatBot, your friendly assistant.")

        elif 'time' in user_input:
            from datetime import datetime
            print(f"ChatBot: The current time is {datetime.now().strftime('%H:%M:%S')}")

        elif 'weather' in user_input:
            print("ChatBot: I can't check the weather yet, but I hope it's nice where you are!")

        elif 'bye' in user_input:
            print("ChatBot: Bye! Talk to you soon.")
            break

        elif 'hobby' in user_input or 'do you like' in user_input:
            print("ChatBot: I enjoy processing data and chatting with curious minds like you!")

        elif 'color' in user_input:
            print("ChatBot: I like blue—it's the color of calm and clarity.")

        elif 'where are you' in user_input or 'location' in user_input:
            print("ChatBot: I live in the cloud, floating between servers and conversations.")

        elif 'joke' in user_input:
            print("ChatBot: Why did the developer go broke? Because he used up all his cache!")

        elif 'thank you' in user_input or 'thanks' in user_input:
            print("ChatBot: You're welcome! I'm always here to help.")

        elif 'you are smart' in user_input or 'you are cool' in user_input:
            print("ChatBot: Aw, you're making my circuits blush!")

        else:
            print("ChatBot: I'm not sure how to respond to that. Can you rephrase or ask something else?")

chatbot()