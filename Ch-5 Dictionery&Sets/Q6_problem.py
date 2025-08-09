# Building a Basic Emoji Translator:
emoji_dict={
    "happy":"😄",
    "love":"❤️",
    "fire":"🔥",
    "sad":"😔",
    "cool":"😎",
    "food":"😋",
    "dog":"🐶",
    "cat":"😺",
}

def emoji_translate(sentence):
    words=sentence.split() # break the sentence in ist of word like ["I","am"..] in list
    return " ".join(emoji_dict.get(word,word) for word in words)

# (" ".join) it joins the modified words back into a single sentence
'''
emoji_dict.get(word, word) checks if the word exists in emoji_dict:
If it exists, it replaces the word with its corresponding emoji.
.get() use for prevent error if the the particular word is not present in dict it give as it is without error that it not emoji_dict
If it does not exist, it keeps the word as it is.
'''
print(emoji_translate("I am happy and in love"))