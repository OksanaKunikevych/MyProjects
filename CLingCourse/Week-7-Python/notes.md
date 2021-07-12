##Notes

1. Very smart if-else expression) But here comes the problem:
   `AssertionError: Lists differ: ['Nlp', 'is', 'fun', '!'] != ['NLP', 'is', 'fun', '!']`
   Update: Correct, but it could be more efficient. Try to avoid repetitions of code.

2. Correct!

3. Good job!

4. Well done!

5. No questions here!

6. Looks pretty, but the function was supposed to return the solution to the problem (of a numerical type as shown in the example). Your function returns the whole mathematical problem as a string, which is nice, but cannot be used futher in programming. The calculations are correct.
   Update: very elegant! I love it.

7. The same problem as above. The calculation is correct, though.
   Update: `AssertionError: ('Average number of articles per sentence = ', 1.397) != 1.396`

8. Correct. One remark about the algorithm: it is bad practice to open a file multiple times. It is better either to extract all necessary information in one read or to read the content of the file into a variable and then reuse it.
   Update: very nice!

9. Very nice! Two small remarks:
   - use `elif` instead of `if`. In your case, you check all three `if`s on every line, which is unnecessary. If you need further explanation as to why `elif` will spare processing time in this function, please tell me.
   - your function should have produced `incorrect ~ correct`, not vice versa
   Update: very nice!

10. No solution provided yet.

P.S. You forgot to add `import re` at the beginning of the file.

