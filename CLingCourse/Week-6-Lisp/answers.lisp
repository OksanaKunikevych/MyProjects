(in-package :cling-course)
(named-readtables:in-readtable rutils-readtable)

;;Task 1.
 (defun hypotenuse (a b)
	"Define the length of hypotenuse using the Pythagorean Theorem"
	    (sqrt (+ (expt a 2) (expt b 2))))

;;Task 2.
(defun reversing (word)
	"Reverse the word if it is not longer than 7 characters"
		(if (< (length word) 8)
		    (strcat word "|" (reverse word))
		    (format t "~&Your name is too long, ~A!" word)))

;;Task 3.
 (defun genealogy (person)
 	"Print out person's genealogy in nice format"
  (format t "~{~&Here is ~A, ~:[he~;she~] is ~A years old~
               ~{, has ~A children~@[ and ~A grandchildren~]~}.~}"
          person))

 (defparameter *person*
  "Define person name, age, children and grandchildren"
  '(("Pepe" nil 5 ())
    ("Mirabella" t 36 (3 nil))
    ("Jose" nil 56 (7 nil))
    ("Constancia" t 67 (5 7))))

;;(mapcar 'genealogy *person*)

;;Task 4. 
 (defun sp (word)
 	"Define the plural form of the given word"
		(cond ((member (substr word -2) '("oy" "ey") :test 'string-equal) (format t "~As" word))
		      ((member (substr word -2) '("ss" "sh" "ch") :test 'string-equal) (format t "~Aes" word))
		      ((ends-with "o" word) (format t "~Aes" word))
		      ((ends-with "fe" word) (format t "~Aves" (substr word 0 -2)))
		      ((ends-with "af" word) (format t "~Aves" (substr word 0 -1)))
		      ((ends-with "y" word) (format t "~Aies" (substr word 0 -1)))
		      (t (format t "~As" word))))

;;Task 5.
(defun sent (subj pred aux not question)
        "Construct a sentence from given subject, 
	 a predicate, an optional auxilary, 
	 an optional negation, and optional question mark"
  (if question
         (if (string-equal "n't" not)
             (fmt "~@[~A~]~A ~@[~A ~]~A?"
                  (string-capitalize aux) not (string-downcase subj) pred)
             (fmt "~@[~A ~]~A ~@[~A ~]~A?"
                  (string-capitalize aux) (string-downcase subj) not pred))
         (if (string-equal "n't" not)
             (fmt "~A~@[ ~A~]~@[~A~] ~A." (string-capitalize subj) aux not pred)
             (fmt "~A~@[ ~A ~]~@[~A~] ~A." (string-capitalize subj) aux not pred))))

;;Task 6.
(defun subtree (tree tag)
		(unless (atom tree)
		  (apply #'append
			 (when (eql (car tree) tag)
			   (list tree))
			 (mapcar #'(lambda (tree) (subtree tree tag))
				 (cdr tree)))))

;;Task 7.
Comming soon...