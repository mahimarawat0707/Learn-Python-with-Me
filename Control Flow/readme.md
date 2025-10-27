# 🔁 Control Flow in Python

## 🔹 What is Control Flow?
- **Control flow** refers to the order in which individual statements, instructions, or function calls are executed in a program.  
- Python uses **conditional statements** and **loops** to control execution based on conditions or repetitions.

---

## ⚙️ If / Else Statements
- The `if` statement allows code to run **only if** a certain condition is **True**.  
- The `else` block runs if the condition is **False**.  
- Statements **outside** the `if` block run **regardless** of the condition.

### Key Concepts:
- **`if`** checks for a condition.  
- **`else`** executes when the `if` condition fails.  
- Indentation defines **code blocks** in Python.  
- Any code **not indented** runs outside the conditional structure.

### Example Concept:
- If a variable `a` is `True`, the output will show:
  - “It is true!”
  - Followed by “It will get printed cause it is outside the if else block.”

---

## 🔁 For Loops
- A `for` loop is used to **iterate** (loop) through a sequence such as a list, tuple, or string.  
- It runs once for **each item** in the sequence.

### Key Concepts:
- Each item in the sequence is processed one at a time.  
- The loop continues until all items have been visited.  
- Useful for **iterating over collections** like lists or dictionaries.

### Example Concept:
- For a list `[1, 12, 23, 34, 45, 56]`, the loop will print each number:
  - 1  
  - 12  
  - 23  
  - 34  
  - 45  
  - 56  

---

## 🔂 While Loops
- A `while` loop repeats as long as a specified condition is **True**.  
- It checks the condition **before** each iteration.  
- If the condition becomes **False**, the loop stops.

### Key Concepts:
- Always ensure the condition will **eventually become False**, or it will create an **infinite loop**.  
- Commonly used for **repeated actions** where the number of iterations isn’t known in advance.

### Example Concept:
- If `a = 0` and the condition is `while a < 5`, the loop runs as long as `a` is less than 5.  
- After each iteration, `a` increases by 1, so the loop prints:
  - 0  
  - 1  
  - 2  
  - 3  
  - 4  

---

## 🧠 Summary Table

| Control Structure | Description | Executes When |
|--------------------|--------------|----------------|
| **if** | Executes a block if condition is True | Condition is True |
| **else** | Executes a block if condition is False | Condition is False |
| **for loop** | Iterates through a sequence | Until all elements are visited |
| **while loop** | Repeats while condition is True | Until condition becomes False |

---

## 💡 Key Takeaways
- **Indentation** is crucial in Python control flow.  
- `if/else` handles **decision-making**.  
- `for` loops are for **iteration**.  
- `while` loops are for **repetition until a condition changes**.  
- Always ensure loops have a way to **end safely**.

---
