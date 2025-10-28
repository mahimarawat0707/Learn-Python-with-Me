# ➕ OPERATORS in Python

## 🔹 What Are Operators?
- **Operators** are special symbols or keywords used to perform operations on variables and values.  
- Python supports different types of operators such as:
  - **Arithmetic Operators**
  - **Comparison Operators**
  - **Logical Operators**
  - **Membership Operators**

---

## ⚙️ Arithmetic Operators
- Used to perform **basic mathematical operations** like addition, subtraction, multiplication, and division.

| Operator | Description | Example | Result |
|-----------|--------------|----------|--------|
| `+` | Addition | `1 + 1` | 2 |
| `-` | Subtraction | `2 - 4` | -2 |
| `*` | Multiplication | `4 * 8` | 32 |
| `/` | Division | `20 / 5` | 4.0 |
| `%` | Modulus (remainder) | `78 % 12` | 6 |

### 🧮 Additional Concept:
- Division always returns a **float**, even when the result is a whole number.  
  Example: `67 / 9` → 7.444444444444445  

---

## 🔤 Arithmetic Operators with Strings
- The `+` operator can **concatenate strings** (join them together).  
- The `*` operator can **repeat a string** multiple times.

### Example Concepts:
- `'String 1' + ' ' + 'String 2'` → `'String 1 String 2'`  
- `'String 1 ' * 5` → `'String 1 String 1 String 1 String 1 String 1 '`

🧠 **Note:**  
Arithmetic operators with strings only work with `+` (concatenation) and `*` (repetition).  
You cannot subtract or divide strings.

---

## 🔍 Comparison Operators
- Used to **compare two values** and return either **True** or **False**.

| Operator | Description | Example | Result |
|-----------|--------------|----------|--------|
| `==` | Equal to | `True == True` | True |
| `<` | Less than | `4 < 5` | True |
| `<=` | Less than or equal to | `5 <= 5` | True |
| `>` | Greater than | `5 > 2` | True |
| `>=` | Greater than or equal to | `5 >= 5` | True |
| `!=` | Not equal to | `5 != 2` | True |

🧩 **Note:**  
Comparison operators are often used inside **conditions**, such as `if` statements or loops.

---

## 🧠 Logical Operators
- Used to combine multiple conditions into a single Boolean expression.  

| Operator | Description | Example | Result |
|-----------|--------------|----------|--------|
| `and` | True if **both** conditions are True | `True and True` | True |
| `or` | True if **at least one** condition is True | `True or False` | True |
| `not` | Reverses the result | `not True` | False |

### Example Concepts:
- `True and False` → **False**  
- `False or False` → **False**  
- `not False` → **True**

🧩 **Note:**  
Logical operators are essential for decision-making and control flow in Python.

---

## 🔎 Membership Operators
- Used to check if a value is **present in** or **absent from** a collection (like a list, tuple, or string).

| Operator | Description | Example | Result |
|-----------|--------------|----------|--------|
| `in` | Returns True if value exists | `1 in [1,2,3,4,5,6]` | True |
| `not in` | Returns True if value does **not** exist | `10 not in [1,2,3,4,5]` | True |

### Example Concepts:
- `12 not in [1,2,3,4,5]` → **True**  
- `'cat' in 'my pet cat'` → **True**  
- `'dog' not in 'my pet dog'` → **False**

---

## 🧩 Summary Table

| Type | Operator Examples | Used For |
|------|--------------------|-----------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `**` | Mathematical operations |
| **Comparison** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparing values |
| **Logical** | `and`, `or`, `not` | Combining Boolean conditions |
| **Membership** | `in`, `not in` | Checking presence in collections |

---

## 💡 Key Takeaways
- **Arithmetic operators** perform math operations on numbers and strings (in specific cases).  
- **Comparison operators** compare values and return Boolean results.  
- **Logical operators** combine or reverse conditions.  
- **Membership operators** test whether an item exists in a collection.  
- Operators are fundamental for building conditions, expressions, and decision-making logic in Python.

---
