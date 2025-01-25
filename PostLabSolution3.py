import random

nouns = ()
prepositions = ()
verbs = ()
articles = ()

def getVocab(vocab, file_name):
    print(f"Enter {vocab}, one word per line, and type '0' to finish:")

    with open(file_name, "w") as file:
        while True:
            user_input = input()

            if user_input == '0':
                break

            file.write(user_input + "\n")

    return getWords(file_name)

def getWords(file_name):
    words = []
    with open(file_name, "r") as file:
        for line in file:
            words.append(line.strip())

    return tuple(words)

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    global nouns, prepositions, verbs, articles  
    valid_inputs = ['nouns', 'prepositions', 'verbs', 'articles']
    vocab_files = {key: f"{key}.txt" for key in valid_inputs}

   
    while not (nouns and prepositions and verbs and articles):
          for category in valid_inputs:
        
            file_name = vocab_files.get(category)
            
            if category == 'nouns' and not nouns:
                nouns = getVocab(category, file_name)
            elif category == 'prepositions' and not prepositions:
                prepositions = getVocab(category, file_name)
            elif category == 'verbs' and not verbs:
                verbs = getVocab(category, file_name)
            elif category == 'articles' and not articles:
                articles = getVocab(category, file_name)

  
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
