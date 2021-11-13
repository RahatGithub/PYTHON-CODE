def concatenate(*words):
    
    l = len(words)

    for i in range(l):

        print(words[i], end="")

        if i < l-1:
            print("-", end="")
            


concatenate("I", "love", "Python", "!")