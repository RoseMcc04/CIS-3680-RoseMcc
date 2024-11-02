# Dictionaries

## Table of Contents

0. [Table of Contents](#table-of-contents)
1. [Dictionaries](#dictionaries-1)
2. [Dictionary Literals](#dictionary-literals)
3. [Adding Keys and Replacing Values](#adding-keys-and-replacing-values)
4. [Accessing Values](#accessing-values)
5. [Removing Keys](#removing-keys)
6. [Traversing a Dictionary](#traversing-a-dictionary)
7. [Useful Dictionary Methods and Functions](#useful-dictionary-methods-and-functions)

## Dictionaries

- A dictionary organizes information by **association**, not position
    - *Example: When you use a dictionary to look up the definition of a word, you do not start on the first page, you turn to the words with the query you desire*
- Data structures organized by association are also called **tables**, **association lists**, or **mappings**
- In Python, a **dictionary** associates a **key** with a data value

## Dictionary Literals

- A Python dictionary is written as a sequence of key/value pairs separated by commas
    - Pairs are called **entries**
    - Enclosed in curly braces `{}`
    - A colon `:` separates a key and its value
    - A comma `,` separates entries
- Examples:
    - A phone book: `{'Savannah':'476-3321', 'Nathaniel':'351-7743'}`
    - Personal information: `{'Name':'Molly', 'Age':'18'}`
    - An empty dictionary: `{}`
- Keys in a dictionary can be data of any immutable types, including other data structures
    - They are normally strings or integers

## Adding Keys and Replacing Values

- Add a new key/value pair to a dictionary using `[]`:
```text
dict[key] = value
```
- Example:
```shell
>>> info = {}
>>> info["name"] = "Sandy"
>>> info["occupation"] = "hacker"
>>> info
{'name':'Sandy', 'occupation':'hacker'}
```
- Use `[]` also to replace a value at an existing key
```shell
>>> info["occupation"] = "manager"
>>> info
{'name':'Sandy', 'occupation':'manager'}
```

## Accessing Values

- Use `[]` to obtain the value associated with a key
- If the key is not present in the dictionary, an error is raised
```shell
>>> info["name"]
'Sandy'
>>> info["job"]
Traceback (most recent call last):
    File "<pyshell#1>", line 1, in <module>
        info['job']
KeyError: 'job'
```
- If the existence of a key is incertain, test for it using the dictionary method **has_key()**
    - Easier strategy is to use the method **get()**
```shell
if "job" in info:
    print(info.["job"])
```

## Removing Keys

## Traversing a Dictionary

## Useful Dictionary Methods and Functions
