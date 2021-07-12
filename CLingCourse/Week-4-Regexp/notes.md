#### Notes

1. You are supposed to catch "37,66,91,72" as four different numbers. Also think how to make your regexp more flexible. `-\d+` doesn't do anything.

   Update: Correct.

2. Correct, but there's a more efficient way to solve this task without using lookbehinds.

3. Good job!

4. You weren't supposed to catch this sentence:
   "Or perhaps adopt the tactic of very quietly lying in wait and then smash him in court when he scams again , as promised ?"
   Find out why you caught it and fix the regexp.

   Update: Well done!

5. Your regexp didn't catch some of the sentences. For example:
   "What_WP developed_VBD a_DT crack_NN in_IN 0000_NNP while_IN tolling_VBG the_DT death_NN of_IN U.S._NNP Chief_NNP Justice_NNP John_NNP Marshall_NNP ?_."
   Find out why and fix the regexp.
   Think of a better way to write `NNS?P?(PS)?`. See your answer to task 8.

   Update: Good job!

6. Remarks:
   Think of a better way to write `VBD?G?P?Z?N?`
   `(\bgo(es|ne|ing)?|went\b)`: the left `\b` should be outside brackets, and the right one is unnecessary because you specify the right context later, and the right context is `_` in your case, which is in the same class of characters as letters, so you contradict yourself writing `\b_`. This is the reason why you missed some sentences.
   You do not need brackets here: `(\w+)`.

   Update: Very nice!

7. Perfect!

8. Well done. `\b` is unnecessary in `NNP?S?\b after`. You already state the boundary with a letter and a space.

9. Correct!

10. Very nice! Yes, you can also sort them.
