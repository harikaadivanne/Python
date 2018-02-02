list = input("Enter the sentence: ")

longest = 0
for word in list.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print("The longest word is %s" % longest_word)
# reversing the words and storing them into a list at a time
reversewords = [rev[::-1] for rev in list]

# Joining the reversed words into a sentence
revsentence = " ".join(reversewords)

# Printing the new sentence that is reversed
print('The reversed sentence is:', revsentence)
reversed_string = list[::-1]
print (reversed_string)

words = list.split() #Forget ()
len_sentence = len(words)
middle = []
if len_sentence%2==0:
    middle.append(words[(len_sentence//2)-1])
    middle.append(words[len_sentence//2])
else:
    middle.append(words[len_sentence//2])
print(middle)



