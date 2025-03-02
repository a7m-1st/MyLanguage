# MyLang  

MyLang is a simple, structured, and expressive programming language designed for readability and ease of use. It features a variety of control flow statements, including `if-else`, `while`, `for`, `unless`, `switch`, and `do-while` loops. The language also supports variable declarations, print statements, and expressions with arithmetic and comparison operators.  

## Features  
✅ **Control Flow:** `if-else`, `while`, `do-while`, `unless`, `switch`, and multiple `for` loop variations (`foreach`, `range`, `step`, `limit`).  
✅ **Expressions & Operators:** Arithmetic (`+`, `-`, `*`, `/`, `%`), Boolean values, and ternary expressions.  
✅ **Data Structures:** Arrays, objects, and key-value pairs.  
✅ **Comments:** Supports both single-line (`//`) and multi-line (`/// ... ///`) comments.  
✅ **Whitespace & Formatting:** Skips unnecessary whitespace and newline characters.  

## Example Code  
```MyLang
let x = 10;
let y = [1, 2, 3];

if (x > 5) {
    print "x is greater than 5";
} else {
    print "x is small";
}

for (i from 1 to 5) {
    print i;
}

while (x > 0 limit 3) {
    print x;
    x = x - 1;
}
```
How to Use
1. Clone the repository.
2. Build the lexer and parser using ANTLR or any compatible parsing tool.
3. Run main.py with code written in 'expression'

# Example Call in main.py
```
# Input from the user
expression = """
    let i = 0
    while (i < 2) {
        let j = 0
        while (j < 2) {
            print j
            let j = (j + 1)
        }
        let i = (i + 1)
    }

"""
```
Let us know if you need any modifications! 🚀

🚀 License: MIT
