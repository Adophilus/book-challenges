# The Pragmatic Programmer | Challenges: Orthogonality (page 43)

### Question 1

Consider the difference between large GUI-oriented tools typically found on
Windows systems and small but combinable command line utilities used
at shell prompts. Which set is more orthogonal, and why? Which is easier
to use for exactly the purpose for which it was intended? Which set is
easier to combine with other tools to meet new challenges?

### Solution 1
I believe that small, combinable command line utilities are more orthogonal for the purpose they were intended for. Command line utilities are very often developed in totally separate environments. But in either case, their "contract's" very rarely change. And even when they do, there is almost always another command line tool that is capable of interfacing directly with the new contract of the modified version.

It is easier, by a very convincing margin, to combine multiple different command line utilities to meet new challenges than it is to combine multiple full-blown GUI apps to work together. The main reason for this is because GUI apps typically are developed to perform a set of actions with as little effort from the user as possible. Initially, the cost of putting together command line utilities to solve a problem is higher than using a GUI app tailored to solve that particular problem. But as time as time goes on (after the commands are assembled the first time), they need only very little customization from time to time. As opposed to GUI apps where the cost remains constant or decreases slightly due to features that could allow users create their own custom actions.

### Question 2
C++ supports multiple inheritance, and Java allows a class to implement
multiple interfaces. What impact does using these facilities have on orthogonality? Is there a difference in impact between using multiple inheritance
and multiple interfaces? Is there a difference between using delegation and
using inheritance?

### Solution 2
The only difference I can percieve between delegation and using inheritance is the fact that using inheritance allows for easier 'composability' (for lack of a better term). It is easier to define multiple behaviours in separate classes and then 'compose' them together in a new class to form an entity that does what each of those individual classes do. Whereas in the case of inheritance, you a given a contract which you must honour in order for your code to compile. Besides this difference I believe that delegation and using inheritance are very much alike and have no impact on orthogonality.

## Excercises

### Excersise 1
You are writing a class called Split, which splits input lines into fields. Answer. Which of the following two Java class signatures is the more orthogonal design?
```java
class Split1 {

  public Split1(InputStreamReader rdr) {
    // ...
  }

  public void readNextLine() throws IOException {
    // ...
  }

  public int numFields() {
    // ...
  }

  public String getField(int fieldNo) {
    // ...
  }
}

class Split2 {

  public Split2(String line) {
    // ...
  }

  public int numFields() {
    // ...
  }

  public String getField(int fieldNo) {
    // ...
  }
}
```

### Solution 1
I believe that the draft for second class, `Split2`, is the more orthogonal design. My reasoning goes thus:
- in the question, it stated that the ideal implementation is one which **splits input lines into fields**
- `Split2` does just what the question asks.
- `Split1` makes the assumption that the lines to split must come from a file, hence rendering it useless when receiving the input lines from other input sources

### Exercise 2
Which will lead to a more orthogonal design: modeless or modal dialog Answer boxes?

### Solution 2
I believe modal dialog boxes are more orthogonal than modalless dialog boxes because in the case of modal dialog boxes, each modal has a contract that it must honour. Take, for example, a 'save file' dialog box. The dialog box returns the file path selected by the user to the parent modal which then proceeds to do whatever it wants with it (save a file in this case). But in the case of modalless dialog boxes, both parent and child window have to be aware of one another's side effects in order to function properly (which breaks the principle of orthogonality).
PS: in the case of the 'save file' dialog box, the contract of the modal could be a function which returns a string (the file path selected by the user).

### Exercise 3
How about procedural languages versus object technology? Which results in a more orthogonal system?

### Solution 3
My knowledge on the topic is lacking. I will need to conduct some research on this topic.
I belive the OO pattern is more orthogonal than procedural system. My main reason for going with this is because in the case of procedural programming there could be situations where the order in which operations are performed are more important than just performing those operations. But in the case of the OO paradigm, the object 'knows' what to do when it is required to perform an operation. This way, the object performs those operations in whatever order it deems fit (without the calling party needing to know much about what is actually going on behind the scenes).
