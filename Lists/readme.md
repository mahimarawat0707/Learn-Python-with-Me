# Python Lists & List Slicing (Notes)

## Lists
- A **list** is a collection of ordered and changeable items.
- Lists can store multiple values of different data types (numbers, strings, etc.).
- Lists are written inside **square brackets**.

---

## List Slicing (Extracting Portions of a List)

### Syntax:
list[start : stop : step]

### Parameters:
- **start** → Index where slicing begins (included)
- **stop** → Index where slicing ends (excluded)
- **step** → Skips items based on the step value (optional)

### Concepts:
- `list[start:]` → From a specific index to the end
- `list[:stop]` → From the beginning to a specific index
- `list[::step]` → Select every nth element using step
- Negative indexes allow slicing from the end of the list

---

## Using `range()`
- `range(n)` generates a sequence from **0 to n−1**.
- Often used in loops (`for`) to repeat actions multiple times.
- Can be combined with lists to generate sequential data.

---

## 🧠 Lists created using `range()`
- A list can be created from a range to automatically generate sequences.
- Adding a step to range allows skipping multiple values in the sequence.

---

## ✏️ Modifying Lists

### Adding elements:
- New items can be appended at the **end** of the list.
- New items can be inserted at a **specific position**.

### Removing elements:
- Items can be removed by **value**.
- Items can be removed by **position** (last value removed automatically).
- A list can be emptied by repeatedly removing items.

---

## 🧬 Copying Lists

### Incorrect way:
- Assigning one list to another makes both variables point to the **same memory location**.
- Any change to one list affects the other.

### Correct way:
- Use `.copy()` to make a **new independent list**.
- Changes to one list do **not affect** the original list.

---

## ⭐ Key Takeaways
- Lists are ordered and changeable.
- Slicing helps extract selected elements.
- `range()` helps generate sequences quickly.
- Use `.copy()` when you need a separate, independent list.
