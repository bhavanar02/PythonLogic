def dynamicArray(arr, element):
    arr.append(element)
    if len(arr) == len(arr):
        new_arr = arr + [None] * len(arr)
        arr[:] = new_arr

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Watermelon", "Peach", "Kiwi", "Strawberry"]
print("Initial fruits array:", fruits)

dynamicArray(fruits, "Lychee")
print("Fruits array after adding Lychee:", fruits)