##Notes

1. Nice analysis! You must have meant quotation marks, not brackets ;)

2. Correct! Interesting answers, too. A couple of improvements:
   - try to fit 80 characters per line (Python allows breaking code into lines, too)
   - if you do an operation a few times, it's better to create a variable (like with `w.lower()`)

3. Very nice, but the output data type is wrong. See the specifications again. The answers to the questions are missing too.  
   Update: good job!

4. `ZeroDivisionError: float division by zero` I have found the mistake. Can you? ;)  
   Update: the error is still there. Check line 34.  
   Update #2: the error was "/n" instead of "\n". In the new version, instead of using `f.read()` and then `adj_words.splitlines()`, you could have used just `f.readlines()`. Well done!

5. When you print the synonyms, they should not include the word in question. Compare: "It has the following synonyms: sofa, lounge" vs "It has the following synonyms: sofa, couch, lounge"  
   You should not print the synonyms if the word in question is the only one in the list: "It has the following synonyms: couch".  
   Update: Works well! An easier way would be to use the `remove` method instead of creating a cycle: `synonyms = [item for item in synset.lemma_names() if item!=word]`

6. Perfect! I hope you had fun!
