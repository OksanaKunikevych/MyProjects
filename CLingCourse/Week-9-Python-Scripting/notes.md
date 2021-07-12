##Notes

1. The calculations in the `ari` functions are correct, but you are supposed to return a number, not a string. The `lexical_diversity` function does not compile. There's an error in this line: `return "Lexical diversity = " + str(round(len(unique) * 100 /len(words),2 + "%"))`. But again, return only the number, please.  
   Update: there's a problem with the `lexical_diversity` function. For example, "The" and "the" represent the same word. Your function counts them as different words.  
   Update: correct!

2. You have missed something in `re.sub(r"(^([^aoei]*)|(?<!u))([a-z]*$)", r"\\3\\2ay")`: `TypeError: sub() takes at least 3 arguments (2 given)`. One more remark: you don't need two slashes when you put an `r` before the expression: `r"\\3\\2ay"`.  
   Update: when applied to "style", your function should return "ylestay", not "estylay", as "y" represents a vowel here.

3. A couple of remarks here:
   - you don't need the `re` module to conduct such a simple search: `re.search(", ", i)`, `re.search(" ", i)`; it is more efficient to use the `find` method of the string class
   - do not state local addresses in scripts: `file = open("/home/ok/cling-course/Homework/Oksana/Week-9-Python-Scripting/animals.txt", "w")`. I cannot run the script because my local address is different from yours. Improve the script so that it knows where to put the file.
   - the script does not do anything; read the part on the scripts in the lecture again  
   Update: the function works, but the script doesn't. The script should work when run from the terminal or in REPL.

4. Well done! A small thing to fix here:
   `AssertionError: "I 'll meet you , and you 'll pay me  $5,000." != "I 'll meet you , and you 'll pay me $5,000 ."`  
   Update: your function adds some extra spaces, but that's not a problem. Let it be :)

5. Your `count_gematria` function should return a number:
   `AssertionError: 'Gematria of the word assassination is 1793' != 1793`
   Moreover, all system arguments are read as strings, so this will never return `True`: `if sys.argv[3] not in [1,2]:`  
   Update: I spotted a few problems with tokenization, but the function works. That's OK.

