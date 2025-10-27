# 🐍 Python Data Structures — Notes

## 📋 Lists
- Lists are **ordered collections** of elements.  
- **Order matters** — elements maintain their sequence.  
- Lists are **mutable**, meaning values can be added, removed, or changed.  
- Can contain **different data types** (numbers, strings, etc.).  
- You can **append** new elements to a list.  
- **Example Concept:** `[1, 2, 3]` is not equal to `[3, 2, 1]`.

---

## 🔢 Sets
- Sets are **unordered collections** of **unique items**.  
- **Order does not matter** — two sets with the same elements are equal, regardless of order.  
- Sets **automatically remove duplicates**.  
- Sets are **mutable**, so elements can be added or removed.  
- The **length** of a set shows how many unique elements it has.  
- **Example Concept:** `{1, 2, 3}` is equal to `{3, 2, 1}`.

---

## 🎯 Tuples
- Tuples are **ordered collections**, similar to lists.  
- **Order matters** — elements retain their position.  
- Tuples are **immutable**, meaning once created, they cannot be changed.  
- Useful for storing **fixed data** that shouldn’t be modified.  
- The **length** of a tuple indicates how many items it contains.  
- **Example Concept:** `(1, 2, 3)` is not equal to `(3, 2, 1)`.

---

## 📖 Dictionaries
- Dictionaries store data in **key-value pairs**.  
- Keys are **unique**, while values can be **repeated**.  
- Dictionaries are **mutable**, allowing addition, removal, or modification of items.  
- Keys are used to **access** corresponding values.  
- Used for **structured data**, such as describing properties or mappings.  
- **Example Concept:** `'apple': 'A red fruit'` means key = `'apple'` and value = `'A red fruit'`.

---

## 🧠 Summary Table

| Data Type     | Ordered | Mutable | Allows Duplicates | Main Use                              |
|----------------|----------|----------|-------------------|----------------------------------------|
| **List**       | ✅ Yes   | ✅ Yes   | ✅ Yes            | Store ordered, changeable data         |
| **Set**        | ❌ No    | ✅ Yes   | ❌ No             | Store unique, unordered data           |
| **Tuple**      | ✅ Yes   | ❌ No    | ✅ Yes            | Store fixed, ordered data              |
| **Dictionary** | ✅ (3.7+) | ✅ Yes  | ❌ (keys only)    |
