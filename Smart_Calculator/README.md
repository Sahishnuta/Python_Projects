## Problem Statement

**Create an intelligent calculator that can:**

1. **Handle basic arithmetic operations** (addition, subtraction, multiplication, division)
2. **Process complex expressions** with multiple operations and parentheses
3. **Maintain memory** of previous results using variables
4. **Follow proper mathematical precedence** (PEMDAS/BODMAS rules)
5. **Provide error handling** for invalid inputs and edge cases
6. **Offer a user-friendly interface** with commands like `/help` and `/exit`

## Key Features Implemented

### 1. **Basic Arithmetic**
- Supports `+`, `-`, `*`, `/`, `^` (exponentiation)
- Handles unary plus and minus operators

### 2. **Variable Support**
- Store and recall values using variables (e.g., `x = 5`, `y = x + 3`)
- Variables can contain only letters
- Case-sensitive variable names

### 3. **Expression Parsing**
- Converts infix notation to postfix (Reverse Polish Notation)
- Handles operator precedence and associativity
- Manages nested parentheses

### 4. **Smart Input Handling**
- Processes multi-line inputs
- Ignores multiple spaces and tabs
- Validates expression syntax

### 5. **Special Commands**
- `/help` - Shows usage instructions
- `/exit` - Terminates the program
- Empty input handling

## Technical Implementation

### Core Components:

1. **Input Processing**
   - Tokenizes input strings
   - Identifies operators, operands, and variables
   - Handles consecutive operators (e.g., `+++`, `---`)

2. **Expression Evaluation**
   - Shunting Yard algorithm for infix to postfix conversion
   - Stack-based postfix evaluation
   - Proper precedence handling

3. **Variable Management**
   - Dictionary-based storage
   - Assignment and retrieval operations
   - Validation of variable names and values

## Example Usage Patterns:

```
> 2 + 2
4

> x = 5
> y = 3
> x * y
15

> (2 + 3) * (4 - 1)
15

> /help
The program calculates mathematical expressions
Supports +, -, *, /, ^ operators
Use variables with letters only
Type /exit to quit

> /exit
Bye!
```

## Challenges Solved:

1. **Operator Precedence**: Correctly evaluates complex expressions
2. **Variable Scoping**: Maintains state across multiple inputs
3. **Error Recovery**: Handles invalid syntax gracefully
4. **Memory Management**: Stores and recalls variable values
5. **User Experience**: Provides clear feedback and help

This calculator goes beyond basic arithmetic by implementing a robust expression parser that understands mathematical notation rules and maintains computational state through variables.
