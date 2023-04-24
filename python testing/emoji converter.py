message = input(">")
words = message.split(' ')
emojis = {
    ":)": "Smiling Emoji",
    ":(": "Sad Emoji"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
