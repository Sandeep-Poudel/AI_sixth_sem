sentence = input("Enter the sentence: ")

def findFrequency(sentence):
    frequency = {}
    for letter in sentence:
        if(letter  in frequency):
            frequency[letter] = frequency[letter]+1
        else:
            frequency[letter]=1
    
    keys = frequency
    for key in keys:
        print(f"The frequency of {key} = ", frequency[key])

findFrequency(sentence)