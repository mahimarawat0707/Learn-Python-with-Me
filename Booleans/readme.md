# Booleans in Python

## 🔹 What Are Booleans?
- Booleans represent **True** or **False** values in Python.  
- They are mainly used for **conditions**, **comparisons**, and **logical operations**.

---

## 🔹 Casting to Booleans
- `bool(1)` → **True**  
- `bool(0)` → **False**  
- `bool(-1)` → **True**  
- `bool(0.0)` → **False**  
- `bool(0j)` → **False**  
- `bool("True")` → **True**  
- `bool("False")` → **True** (because any **non-empty string** is `True`)  
- `bool("")` → **False** (empty string is `False`)

**Note:**  
Anything that is **empty** (like `[]`, `""`, `{}`, `set()`, `None`, or `0`) evaluates to **False**.  
Anything **non-empty** evaluates to **True**.

---

## 🔹 Booleans in Lists
- A list with elements is considered **True**.  
- An empty list is considered **False**.  
- Example Concept:  
  - If a list has values, Python treats it as **True**.  
  - If it’s empty, Python treats it as **False**.  
- This allows conditional checks like:  
  - “If the list has data, do something.”

---

## 🔹 Boolean Comparisons
- When comparing values:  
  - If `a - b` equals `0`, then both are equal.  
  - Therefore, `a == b` is **True**.  
- Any **non-zero** difference is considered **True**, meaning **not equal**.

---

## 🔹 Boolean Logic
- **and** → True if **both** conditions are True.  
- **or** → True if **at least one** condition is True.  
- **not** → Reverses the Boolean value.

---

### Example Concept
If `weatherIsNice = False` and `haveUmbrella = True`:

- Using `if haveUmbrella or weatherIsNice:`  
  → The result is **True**, because you have an umbrella.  

- Using `if not (haveUmbrella or weatherIsNice):`  
  → The result becomes **False**, because `not` flips the value.

- Using `if haveUmbrella or weatherIsNice:`  
  → Again **True**, so you can **go for a walk**.

---

## Boolean Logic Summary

| Expression | Description | Result |
|-------------|--------------|---------|
| `True and True` | Both are true | ✅ True |
| `True and False` | One is false | ❌ False |
| `True or False` | At least one is true | ✅ True |
| `not True` | Reverses to false | False |
| `not False` | Reverses to true | True |

---

## Key Takeaways
- Booleans are used for **decision-making**.  
- Any **non-empty or non-zero** value is `True`.  
- **Empty**, **zero**, or **None** values are `False`.  
- Boolean logic controls **flow** and **conditions** in programs.
