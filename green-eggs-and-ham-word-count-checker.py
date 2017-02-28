import re;
import string;

def processWord(word):
  wordNoPunctuation = word.translate(None, string.punctuation);
  wordLowercase = wordNoPunctuation.lower();
  return wordLowercase;

words = set();
with open('/Users/jthoms/Desktop/green-eggs-and-ham-script.txt', 'r') as scriptFile:
  for line in scriptFile:
    for hyphenWord in line.split():
      for word in re.split('-', hyphenWord):
        processedWord = processWord(word);
        words.add(processedWord);

print words;
print len(words);

