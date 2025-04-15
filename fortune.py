# fortune.py (v1.1)
import random

print("🔮 Welcome to Priyanshu Singh's Fortune Teller (21JE0715) 🔮")
choice = input("Enter your mood (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "😊✨ Joy attracts joy! Something wonderful is heading your way. Priyanshu ✨🎉",
        "😁🌈 Keep smiling — your happiness is contagious and the universe notices! ✨🍀"
    ],
    "sad": [
        "😢🌧️ Even the darkest night will end, and the sun will rise. 🌅✨",
        "😭💖 You’re stronger than you think — better days are coming. 🌤️💪"
    ],
    "neutral": [
        "😐📝 Today is a blank page — you hold the pen. Write something great! 🚀✨",
        "😶🌟 A calm day brings quiet opportunities. Stay open to surprises. 🎁📘"
    ],
    "stressed": [
        "😩🧘‍♂️ Take a deep breath. Storms don't last forever — peace is coming. 🌤️🌿",
        "😫📉 You’ve got this! One small step at a time is still progress. 💪📈"
    ]
}
if choice in fortunes:
    print(random.choice(fortunes[choice]))
else:
    print("😕 Please enter a valid mood: happy, sad, neutral, or stressed.")
