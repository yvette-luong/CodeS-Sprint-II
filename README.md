# CodeS-Sprint-II

❕ **_`Binary Search`_** is always work ONLY when array is **_`sorted`_**

## **_L I N K_**

- https://app.codesignal.com/test-result/qdaXFqsywu89J794H?accessToken=riSN79DwWmRmwFk5H-TTMxmQFwQTCDKoXbLtkBdBwG

### **_1. ReverseLinkedList_**

**Problem**

- Given a singly linked list, reverse and return it.

**Note:**

- Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

**Example:**

_For l = [1, 2, 3, 4, 5], the output should be_
_reverseLinkedList(l) = [5, 4, 3, 2, 1]._

### **_2.CheckBlanagrams_**

**Problem**

- Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.
- Given two words, check if they are blanagrams of each other.

**Example**

- For word1 = "tangram" and word2 = "anagram", the output should be checkBlanagrams(word1, word2) = true;

- After changing the first letter 't' to 'a' in the word1, the words become anagrams.

- For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

- Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

- For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

- You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

- For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

- These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

### **_3.FindValueSortedShiftedArray_**

**Problem**

- You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

- Write a function that returns the target value's index. If the target value is not present in the array, return -1.

 - You may assume no duplicate exists in the array.

- Your algorithm's runtime complexity must be in the order of O(log n).
    `

**Example**

- Example 1:

    + Input: nums = [4,5,6,7,0,1,2], target = 0
    + Output: 4

- Example 2:

    + Input: nums = [4,5,6,7,0,1,2], target = 3
    + Output: -1
