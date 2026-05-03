# get a dictionary

specific_words = {
    "coffee" : "☕️",
    "love" : "❤️",
    "happy": "🥳"
}


input_message = input("Please enter your message  ").lower()

massive = input_message.split()


def emoji_add_function(message):
    result = []
    for word in message:
        clean_word = word.strip(",.!")
        if clean_word in specific_words:
            result.append(f"{word} {specific_words[clean_word] }")
        else:
            result.append(word)
    return " ".join(result)

print(emoji_add_function(massive))