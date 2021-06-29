def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


array = []

is_done = False

while not is_done:
    user_input = input()
    if user_input == "done":
        is_done = True
    else:
        array.append(int(user_input))

print("Original : " + " ".join(str(k) for k in array))
result = quicksort(array)

print("Sorted : " + " ".join(str(v) for v in result))
