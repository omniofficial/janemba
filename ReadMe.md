# Janemba - A Python Compiler

This is a top down compiler written in Python that uses a predictive parsing table. This was developed by Henry Dinh, Adrian Diaz, and Aidan Jahn. Below is a to-do list for organizational purposes.

## TASKS

### Y = Yes, N = No, IP = In-Progress

## Compiler

### Part 1 [COMPLETE]

Given a provided text file titled final.txt, translate it into a new file titled final24.txt:

-   Remove spaces [Y]
-   Removes blank lines [Y]
-   Leave one space before and one space after each token [Y]

### Part 2 [COMPLETE]

-   Translate the given text file into a programming language (Python) [Y]

### Part 3 [COMPLETE]

Create program to check provided grammar. If errors are found, display corresponding error messages. See part 4. [Y]

-   Read content of file and tokenize text. [Y].
-   Initialize FIRST, FOLLOW, NON_TERMINALS, TERMINALS, and PARSING TABLE. [Y]
-   Parse tokens using a parsing table.

### Part 4 [COMPLETE?]

-   Add additional functionality to display error messages if given grammar does not compile. [Y]
-   Generate pre-defined error messages [Y]
-   Append pre-defined error messages to expected error message. Output result. [Y]
-   Error messages are descriptive and identifiable using tokens. [Y]

### Part 5 [IN PROGRESS]

-   Project report
    -   MLA Format [Y]
    -   Cover Page (page 1) [Y]
    -   Original Program (page 2) [IP]
    -   Original grammar (page 3) [IP]
    -   Grammar in BNF - remove all {, }, and | (page 4) [IP]
    -   Grammar in BNF for predictive parsing, remove left recursion (page 5) [IP]
    -   List members of first and follow (page 6)
    -   Show parsing table (page 7)
    -   Full program files printed, sample run displayed (pages 8 - ?)

## Project Presentation

### Non-Technical Explanation

-   Intro page (Y)
-   Brief summary (Y)
-   How to run the program
-   Program files, organization of the project, and guide

### Technical Explanation

-   Function analysis
-   How to prepare for the tokenization of input file (removing comment lines, blank, and extra spaces in the provided program)
-   How to translate the prepared text file to our programming language: Python.
-   Explain Part 3 by going line by line
-   Explain our error handling in Part 4
-   Difficulties / Questions...
