# The Pragmatic Programmer | Challenges: Domain Languages (page 63)

### Question 1

We want to implement a mini-language to control a simple drawing package (perhaps a turtle-graphics system). The language consists of single-letter commands. Some commands are followed by a single number. For example, the following input would draw a rectangle.
```
P 2 # select pen 2
D # pen down
W 2 # draw west 2cm
N 1 # then north 1
E 2 # then east 2
S 1 # then back south
U # pen up
```

Implement the code that parses this language. It should be designed so that it is simple to add new command

### Solution 1
See [here](/codes/domain-languages/main.py)

### Question 2

Design a BNF grammar to parse a time specification. All of the following examples should be accepted.

```
4pm, 7:38pm, 23:42, 3:16, 3:16am
```

### Solution 2
My knowledge on the topic is lacking, so I need to conduct some research on it.

### Question 3

Implement a parser for the BNF grammar in [Question 2](#question-2) using yacc, bison, or a similar parser-generator.

### Solution 3
My knowledge on the topic is lacking, so I need to conduct some research on it.

### Question 4

Implement the time parser using Perl. [Hint: Regular expressions make good parsers.]

### Solution 4
My knowledge on the topic is lacking, so I need to conduct some research on it.
