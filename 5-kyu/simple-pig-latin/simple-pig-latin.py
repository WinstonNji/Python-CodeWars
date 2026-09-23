def pig_it(text):
    string = ''
    for word in text.split(' '):
      wordList = list(word)
      reversedWord = ''.join(wordList[1:]) + wordList[0] + 'ay' if wordList[0].isalpha() else wordList[0]
      string += reversedWord + ' '
​
    return string.removesuffix(' ')