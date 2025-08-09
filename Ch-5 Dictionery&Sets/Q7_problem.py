# Mood-Based Auto-Filling Emoji Generator:
import random

# Define mood-based emojis
mood_emojis = {
    "happy": ["😃", "😊", "😂", "🥳", "🤩"],
    "sad": ["😢", "😞", "💔", "😔", "😭"],
    "angry": ["😡", "😠", "🤬", "💢"],
    "love": ["❤️", "😍", "😘", "💖", "💞"],
}

def mood_fill(sentence):
    words = sentence.split()  # Split sentence into words
    mood = None  # Initialize mood as None

    # Detect mood request in the sentence
    for key in mood_emojis:
        if f"(fill with {key} emojis)" in sentence:
            mood = key  # Store the detected mood
            sentence.replace(f"fill with {key} emojis", "").strip() # it remove (fill..)
            break  # Exit the loop after finding the first mood

    # Append random emojis if a mood was detected
    if mood:
        words.append("".join(random.choices(mood_emojis[mood], k=3)))  # Select 3 random emojis

    return " ".join(words)  # Return the modified sentence

# Example Usage
print(mood_fill("Hey, how are you doing? (fill with happy emojis)"))
print(mood_fill("I am feeling a bit low today. (fill with sad emojis)"))
print(mood_fill("I love my new phone! (fill with love emojis)"))
print(mood_fill("This is making me so mad! (fill with angry emojis)"))

