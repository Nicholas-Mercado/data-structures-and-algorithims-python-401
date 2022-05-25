# Blog Notes: Merge Sort

## Pseudocode

```py
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

## Trace

Sample List = [50,70,20,30]

Index positions 0  1  2  3  4  5

Merge sort sorts a list of integers in two parts. A divide function called merge sort that breaks down a list into its smallest possible list containing one integer each using recursion and a combine function called merge which sorts the each pair of lists setting the lower value integer to the left position. This continues till each list has been sorted into one list.

### Mergesort

This braking down of the input list is done recursively and there for will happen in different times depending on when each Mergesort is called. For simplicity we will be doing the dividing of the list all at once.

Input list = [50,70,20,30]

```py
DECLARE mid <-- n/2

DECLARE left <-- arr[0...mid]

DECLARE right <-- arr[mid...n]
```

These three lines of code divide up the input list. After each pass the right and left variable are called like so Mergesort(left), Mergesort(right). This recursion divides the list like the following picture.

[50,70,20,30]

[50,70],[20,30]

[50],[70],[20],[30]

### Merge

```py
 while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
        k <-- k + 1
```

This is the code that takes in the divided lists and sorts them lowest to highest, left to right.

First we declare three variable (i,j,k) and set them to zero and while i is less then the length of left and j is less then length of right we do the following.

```py
if left[i] <= right[j]
  arr[k] <-- left[i]
  i <-- i + 1
else
  arr[k] <-- right[j]
  j <-- j + 1
k <-- k + 1
```

Once again because of recursion these step happens at different times but for the sake of human readability we will be breaking them down together. First we the if the left[i] is less then or equal the right[j]. It is. So we set left[i](50) to the arr[k] which is index 0. This process is repeated with the right side lists. see below

**Left side**

Input - [50],[70]

Sort left to right

Output - [50,70]

**Right side**

Input - [20],[30]

Sort left to right

Output -  [20,30]

Finally the process is repeated with the new left and right

Input - [50,70],[20,30]

Output - [20,30,50,70]

