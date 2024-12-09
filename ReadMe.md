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
-   Parse tokens using a parsing table. [Y]

### Part 4 [COMPLETE]

-   Add additional functionality to display error messages if given grammar does not compile. [Y]
-   Generate pre-defined error messages [Y]
-   Append pre-defined error messages to expected error message. Output result. [Y]
-   Error messages are descriptive and identifiable using tokens. [Y]

### Part 5 [COMPLETE]

-   Project report
    -   MLA Format [Y]
    -   Cover Page (page 1) [Y]
    -   Original Program (page 2) [Y]
    -   Original grammar (page 3) [Y]
    -   Grammar in BNF - remove all {, }, and | (page 4) [Y]
    -   Grammar in BNF for predictive parsing, remove left recursion (page 5) [Y]
    -   List members of first and follow (page 6) [Y]
    -   Show parsing table (page 7) [Y]
    -   Full program files printed, sample run displayed (pages 8 - ?) [Y]

## [Project Presentation](https://docs.google.com/presentation/d/1M_c6-o-KFVf6Jpgd8vFNdLSwECEmiMmrDnKDWoGh2p8/edit?usp=sharing)

### Non-Technical Explanation [COMPLETE]

-   Intro page [Y]
-   Brief summary [Y]
-   How to run the program [Y]
-   Program files, organization of the project, and guide [Y]

### Technical Explanation [COMPLETE]

-   Function analysis [Y]
-   How to prepare for the tokenization of input file (removing comment lines, blank, and extra spaces in the provided program) [Y]
-   How to translate the prepared text file to our programming language: Python. [Y]
-   Explain Part 3 by going line by line [Y]
-   Explain our error handling in Part 4 [Y]
-   Difficulties / Questions... [Y]
