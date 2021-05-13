def insert_word_in_sentence(sentence, word, position):
    res = ""
    count = 0
    num = 0
    for i in range(len(sentence)):
        num = i
        if position == 1:
            return word + " " + sentence[:]
        res += sentence[i]
        if (i < len(sentence) - 1 and sentence[i + 1] == " "):
            count += 1
        if count == position - 1:
            count += 1
            res += " " + word
            break
    return res + " " + word if word not in res else res + sentence[num + 1:]


sentence = "i am a boy"
position = 5
word = "bad"
print(insert_word_in_sentence(sentence, word, position))