# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        print(self.word)
        # create blank array to return
        anagram_word_list = []
        # create sorted list of characters in word
        chosen_word_list = list(self.word)
        chosen_word_list.sort()
        print(chosen_word_list)
        # loop through words in list
        for word in word_list:
            iterative_word_list = list(word)
            iterative_word_list.sort()
            if iterative_word_list == chosen_word_list:
                anagram_word_list.append(word)
        # for each word, create sorted list of charactes
        # compare lists
        # if lists are equal, add that word to the array to return
        # return aray
        return anagram_word_list
       