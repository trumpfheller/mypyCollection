# to get the second half of a list when you don’t know what size it is
x = [0]
len(x)

x = ["first", "second", "third", "fourth"]
num_itemsX = len(x)

#y = x[:len(x)]
y = len(x)/2
#num_itemsY = len(y)

print(y)

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
