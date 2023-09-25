from string import ascii_lowercase as letters
def high(x):
    x = x.split(" ")
    scores = {}
    for word in range(len(x)):
        current_score = 0
        for let in range(len(letters)):
            let_score = let + 1
            current_score += x[word].count(letters[let])*let_score
        scores.setdefault(x[word], current_score)
    d = dict([max(scores.items(), key=lambda k_v: k_v[1])])
    for i in d:
        return i
print(high('what time are we climbing up the volcano'))