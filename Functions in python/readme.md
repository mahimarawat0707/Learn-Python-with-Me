# 🧩 Functions in Python

## 🔹 What is a Function?
- A **function** is a reusable block of code that performs a specific task.  
- It helps make programs **modular**, **organized**, and **efficient**.  
- Functions can take **inputs (parameters)** and return **outputs (results)**.

---

## 🧠 Key Characteristics
- Defined using the `def` keyword.  
- Can accept **arguments** (inputs).  
- Can **return** values using the `return` statement.  
- Functions must be **called** to execute.

---

## 🔹 Built-in Function Example
- The `print()` function is a **built-in function** that outputs text or values to the screen.  
- For example:  
  - Printing “Hello” will simply display **Hello** in the output.

---

## 🔹 User-Defined Functions
- You can create your own functions using `def`.  
- Example Concept:  
  - A function `multiplyByThree(val)` returns the given value multiplied by 3.  
  - When given 8, it returns 24.

---

## 🔹 Functions with Multiple Parameters
- Functions can take more than one argument.  
- Example Concept:  
  - A function `multiply(val1, val2)` returns the product of both numbers.  
  - If passed `3` and `4`, the result is `12`.

---

## 🔹 Functions That Modify Lists
- Lists are **mutable**, meaning they can be changed inside a function.  
- Example Concept:  
  - A list `a = [1, 2, 3]` is passed to a function `appendFour(myList)`.  
  - The function appends the number `4` to it.  
  - The updated list becomes `[1, 2, 3, 4]`.

---

## ⚙️ Function Behavior Notes
- Functions can **return** values using the `return` statement.  
- If no `return` is provided, the function returns `None` by default.  
- Arguments can be **positional** or **keyword-based**.  
- Lists and other mutable types passed into functions can be **modified** directly inside the function.

---

## 🧩 Summary Table

| Concept | Description | Example Output |
|----------|--------------|----------------|
| **Function Definition** | Created using `def` | `def myFunc():` |
| **Return Statement** | Sends back a result | `return value` |
| **Built-in Function** | Predefined (e.g., `print()`) | Prints text |
| **User-defined Function** | Created by programmer | Custom logic |
| **Mutable Argument** | Can be changed inside function | List modifications |

---

## 💡 Key Takeaways
- Functions make code **cleaner** and **reusable**.  
- Use `return` to send results back.  
- Parameters pass information into functions.  
- Be careful with mutable objects — they can be changed inside functions.  
- Always give functions **meaningful names** that describe their purpose.

---
