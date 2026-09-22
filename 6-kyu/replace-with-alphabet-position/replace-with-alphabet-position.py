def alphabet_position(text):
​
  letter_array = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
  
  return " ".join([str(letter_array.index(letter.lower()) + 1)  for letter in list(text) if letter.lower() in letter_array])