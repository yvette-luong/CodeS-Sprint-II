'''
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

Test 1
Input:
word1: "tangram"
word2: "anagram"
Expected Output:
true

Test 2
Input:
word1: "tangram"
word2: "pangram"
Expected Output:
true

Test 3
Input:
word1: "aba"
word2: "bab"
Expected Output:
true
'''
def checkBlanagrams(word1, word2):
    
    s_word1 = sorted(word1)
    s_word2 = sorted(word2)
    print(s_word1, s_word2)
    count = 0
    for i in range(len(word1)):
        if s_word1[i] in s_word2:
            s_word2.pop(s_word2.index(s_word1[i]))
    if len(s_word2) == 1:
        return True
    return False