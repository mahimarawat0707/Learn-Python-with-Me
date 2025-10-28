# 🔢 Integers and Floats in Python

## 🔹 What Are Integers and Floats?
- **Integers (int)** are whole numbers (e.g., `1`, `25`, `-7`).  
- **Floats (float)** are numbers with decimal points (e.g., `3.14`, `-2.5`, `0.0`).  
- Python automatically determines whether a number is an **integer** or a **float** based on how it’s written.

---

## 🧮 Arithmetic Operations
- When performing operations between integers and floats, Python automatically **promotes** the result to a **float** if needed.
  
### Example Concepts:
- Division of two integers using `/` always gives a **float** result.  
  - Example: `20 / 4` → **5.0**  
- Adding an integer and a float results in a **float**.  
  - Example: `4 + 4.0` → **8.0**  
- Multiplying an integer by a float gives a **float**.  
  - Example: `4 * 5.0` → **20.0**  
- Using the power operator (`**`) with a float also returns a **float**.  
  - Example: `4 ** 5.0` → **1024.0**

---

## 🔁 Type Casting
- **Casting** means converting one data type into another.  
- Python provides built-in functions like `int()`, `float()`, and `str()` to perform type conversion.

### Example Concepts:
- `int(4 ** 5.0)` → **1024** (converts float result to integer)  
- `int(6.55555555555)` → **6** (truncates the decimal part, doesn’t round)  

---

## 🎯 Rounding Numbers
- The `round()` function rounds a float to the nearest whole number.  
- Example Concept:  
  - `round(45.7777)` → **46**

---

## 🧠 Summary Table

| Operation | Description | Example | Result |
|------------|--------------|----------|--------|
| `/` | Division (returns float) | `20 / 4` | 5.0 |
| `+` | Addition | `4 + 4.0` | 8.0 |
| `*` | Multiplication | `4 * 5.0` | 20.0 |
| `**` | Exponentiation | `4 ** 5.0` | 1024.0 |
| `int()` | Converts to integer | `int(6.5555)` | 6 |
| `round()` | Rounds float | `round(45.7777)` | 46 |

---

## 💡 Key Takeaways
- Python automatically converts between **int** and **float** when needed.  
- Division always results in a **float**, even if the division is exact.  
- **Casting** is used to convert between data types.  
- Use `round()` for rounding and `int()` for truncation.  
- Floats are useful when working with **decimal or fractional values**, while **ints** are ideal for whole numbers.

---
