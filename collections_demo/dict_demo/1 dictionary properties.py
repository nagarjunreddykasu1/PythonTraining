'''
Dictionary: it is a collection data type which holds group of values in the form of key-value pairs
{key:value,key2:value2,.....}
ex: {"name":"Prateek", "age":30, "name":"Nagarjun"}

Properties:
1. Dictionary is represented by curly braces {}
2. Key and values can be either homogeneous or heterogeneous
3. Keys can not be duplicated but values can be duplicated
4. Insertion order is preserved (python 3.7+)
5. Indexing/slicing is not supported
6. Dictionary is a mutable object.
within the dictionary, we can have both mutable and immutable objects
7. Dictionary can be created by using dict() function
8. To access a element of a dictionary, if we pass the key, we will get the value.
person={"name":"prateek", age:25, "city":"Texas"}
person["name"]
person.get("name")

'''

"""

| Feature               | `Dictionary`           | `List`             | `Tuple`              | `Set`                  |
| --------------------- | ---------------------- | ------------------ | -------------------- | ---------------------- |
| Syntax                | `{key: value}`         | `[item1, item2]`   | `(item1, item2)`     | `{item1, item2}`       |
| Ordered (Python 3.7+) | ✅ Yes                 | ✅ Yes             | ✅ Yes               | ❌ No                   |
| Mutable               | ✅ Yes                 | ✅ Yes             | ❌ No                | ✅ Yes                  |
| Duplicate Values      | Keys ❌, Values ✅     | ✅ Yes             | ✅ Yes               | ❌ No                   |
| Index-based access    | ❌ No (key-based)      | ✅ Yes             | ✅ Yes               | ❌ No                   |
| Use case              | Fast lookup using keys | Ordered collection | Immutable collection | Unique item collection |


"""


