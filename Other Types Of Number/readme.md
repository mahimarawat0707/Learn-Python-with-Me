# 🔢 Integers and Decimals in Python

## 🧮 Integers

### 🔹 What Are Integers?
- **Integers** are whole numbers — they can be positive, negative, or zero.  
- Represented using the **`int`** data type.  
- Integers do **not** have decimal points.  
- Python can also **convert strings and numbers from other bases** into integers using the `int()` function.

---

### 🔹 Converting Strings to Integers
- The `int()` function can convert a string containing digits into an integer.  
- Example Concept:  
  - `int("100")` → **100**  

---

### 🔹 Converting from Different Number Bases
- You can specify a **base** (from 2 to 36) as the second argument in the `int()` function.  
- Python then converts the string according to that base.

| Example | Description | Result |
|----------|--------------|--------|
| `int("100", 2)` | Converts binary "100" to decimal | 4 |
| `int("1ab", 16)` | Converts hexadecimal "1ab" to decimal | 427 |

🧠 **Note:**  
- Base `2` → Binary  
- Base `8` → Octal  
- Base `10` → Decimal (default)  
- Base `16` → Hexadecimal  

---

## 💰 Decimals

### 🔹 The `decimal` Module
- Python’s `decimal` module provides a **Decimal data type** for precise decimal arithmetic.  
- It helps avoid rounding errors common with floating-point numbers.  
- Import it using:  
  - `from decimal import Decimal, getcontext`

---

### 🔹 Context and Precision
- The `getcontext()` function allows you to view or modify the **precision** and **rounding rules** of Decimal operations.  
- Example Concept:
  - Default precision: 28 digits  
  - You can set custom precision like:  
    - `getcontext().prec = 4` → Precision set to 4 digits  

🧠 **Note:**  
- The context defines how arithmetic operations are handled, including precision and rounding mode.

---

### 🔹 Using Decimals
- `Decimal(1) / Decimal(3)` → **Decimal('0.3333')** (shows precision up to 4 digits)  
- `Decimal(3.14)` converts a **float**, which includes tiny binary rounding errors:  
  - **Decimal('3.140000000000000124344978758017532527446746826171875')**  
- `Decimal("3.14")` converts a **string**, preserving exact value:  
  - **Decimal('3.14')**

✅ **Best Practice:**  
Always create Decimals from **strings**, not floats, to avoid floating-point precision errors.

---

## 🧩 Summary Table

| Concept | Description | Example | Result |
|----------|--------------|----------|--------|
| **Integer Conversion** | Converts string to integer | `int("100")` | 100 |
| **Binary to Integer** | Converts from base 2 | `int("100", 2)` | 4 |
| **Hexadecimal to Integer** | Converts from base 16 | `int("1ab", 16)` | 427 |
| **Decimal Precision** | Defines precision of decimals | `getcontext().prec = 4` | 4 digits |
| **Decimal Division** | Uses high precision math | `Decimal(1) / Decimal(3)` | Decimal('0.3333') |
| **Safe Decimal Input** | Use string input for accuracy | `Decimal("3.14")` | Decimal('3.14') |

---

## 💡 Key Takeaways
- **Integers** are used for whole numbers without decimals.  
- The `int()` function can convert strings and different base representations.  
- **Decimals** offer higher precision than floats — ideal for financial and scientific calculations.  
- Always use `Decimal("string")` for **accurate results**.  
- You can **adjust precision** globally using `getcontext().prec`.

---
