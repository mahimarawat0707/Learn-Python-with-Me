# 🧵 Strings in Python

## 🔹 What Are Strings?
- **Strings** are sequences of characters enclosed in quotes (`' '` or `" "`).  
- Strings are **immutable**, meaning once created, they cannot be changed.  
- You can access and manipulate strings using **indexing**, **slicing**, and **formatting** techniques.

---

## ✂️ String Slicing

- **Slicing** allows you to extract a portion of a string (or list) using the syntax:  
  `string[start:end]`
- The `start` index is **inclusive**, and the `end` index is **exclusive**.  

### Example Concepts:
| Expression | Description | Result |
|-------------|--------------|--------|
| `name = 'My name is Mahima Rawat'` | A string variable | `'My name is Mahima Rawat'` |
| `name[0]` | Gets the first character | `'M'` |
| `name[0:7]` | Gets characters from index 0 to 6 | `'My name'` |
| `name[:7]` | Same as above (start is optional) | `'My name'` |
| `name[9:]` | Gets all characters from index 9 onward | `'s Mahima Rawat'` |

### 🧩 Slicing Lists
- The same slicing technique applies to **lists**.

| Expression | Description | Result |
|-------------|--------------|--------|
| `myList = [1, 2, 3, 4, 5]` | Creates a list | `[1, 2, 3, 4, 5]` |
| `myList[2:4]` | Gets elements from index 2 to 3 | `[3, 4]` |

---

## 📏 Length of Strings and Lists

- You can find the number of characters in a string or elements in a list using the `len()` function.

| Expression | Description | Result |
|-------------|--------------|--------|
| `len(name)` | Length of the string | `23` |
| `len(myList)` | Length of the list | `5` |

---

## 🧮 String Formatting

### 🔹 Using Concatenation
- You can combine strings using the `+` operator.
- Remember: non-string values must be **converted** to strings using `str()`.

Example Concept:  
`'My number is: ' + str(5)` → `'My number is: 5'`

---

### 🔹 Using f-Strings (Formatted Strings)
- Introduced in **Python 3.6**, f-strings allow you to embed variables and expressions directly in strings using `{}`.

| Example | Description | Output |
|----------|--------------|--------|
| `f'My number is: {5}'` | Inserts value directly | `'My number is: 5'` |
| `f'My number is: {5} and twice that is {2*5}'` | Evaluates expressions | `'My number is: 5 and twice that is 10'` |

🧠 **Tip:**  
f-strings are faster and cleaner than concatenation or the `.format()` method.

---

## 🧾 Multi-line Strings

- Use triple quotes (`'''` or `"""`) to create strings that span multiple lines.
- Great for paragraphs or long blocks of text.

### Example Concept:
```python
myString = '''here is a long block of text.
I can add more lines. 
The text doesn't stop here ''' 
