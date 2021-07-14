# -*- coding: utf-8 -*-'
# !/usr/bin/env python3
"""
created: 7/13/2021
@author: Will Massey
project: Pig Latin
"""


def main():
    while True:
        user_input = input('Enter a word or phrase: ')
        if user_input.isdigit():
            print('Enter letters only!')
            continue
        print(f'PigLatin Translation:\n>>> {englishToPigLatin(user_input)}\n')


def englishToPigLatin(words):
    words = words.split()
    for i, word in enumerate(words):
        words[i] = translateWord(word)
    return ' '.join(words)


def translateWord(word):
    vowels = 'aeiou'
    # Check if first letter of word is capitalized.
    # If True, then capitalize word before returning it.
    isCap = word[0].isupper()

    # Check if last character is a punctuation:
    isPunctuated = word[-1] in '!?.'

    punctuation = None
    if isPunctuated:
        punctuation = word[-1]
        word = word[:-1]

        # Result if word begins with vowel:
    wordA = word.lower() + 'way'
    # Result if word begin with consonant:
    wordB = word[1:].lower() + word[0] + 'ay'
    # Result if word begins with double consonants:
    wordC = word[2:].lower() + word[:2] + 'ay'
    pigLatin = ''

    # Establish boolean variables:
    wordBeginswithVowel = word[0] in vowels
    wordBeginswithConsonant = word[0] not in vowels
    doubleConsonant = word[0] not in vowels and word[1] not in vowels

    if wordBeginswithVowel:
        pigLatin = wordA
    if wordBeginswithConsonant:
        pigLatin = wordB
    if doubleConsonant:
        pigLatin = wordC
    # If the word was originally capitalized
    if isCap:
        pigLatin = pigLatin.capitalize()
    if isPunctuated:
        pigLatin += punctuation
    return pigLatin


if __name__ == '__main__':
    main()


