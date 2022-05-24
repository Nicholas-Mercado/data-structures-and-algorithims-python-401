# Blog Notes: Insertion Sort

## Description

## Pseudocode

```py
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace

Sample List = [20,30,10,40]

Index positions 0  1  2  3

### Pass 1

[20,30,10,40]

We evaluate whether the value of index 1(**temp = arr[ i ]**) is less than value of index 0(**j = i - 1**). The value of temp is set to index[1] value.
If temp is less than **j**, we replace the value of **i** with the value of j.
Since that is not the case, we do nothing and return to the top of the loop

### Pass 2

[20,30,30,40] ---> [20,20,30,40] --->[10,20,30,40]

Variable i is set to 2 since we are on the second iteration of the loop. Variable j is set to 1(**j = i - 1)**. Temp variable is set to the value of index[2], which is 10

We then check our while loop logic:

- We evaluate whether the value of temp is less than the value of index j: 10 < 30

- This is true. We then set 30 to the position of (j+1), or the second index of our array.

- [20, 30, 30,40]

We then set j to (j-1), which the index[0] of our array and enter our while loop again.

We check if the value of temp is less than the value of j, which it is: 10 < 20

We then set the value of index[1] to the value of current value of j:

- [20, 20, 30,40]

We then set j to (j-1) which is -1, check our while loop logic

Since j is less than 0, we break out of the loop.

Finally, we set the zero index (arr[j + 1]) to temp which is 10.

### Pass 3

[10,20,30,40]

Variable i is set to 3 since we are on the second iteration of the loop.

Variable j is set to 2(**j = i - 1)**

The temp variable is set to the value of index[3], which is 40

For our loop, **temp** is not less than the value of **j**, so we don’t enter the loop.
Finally, we set the value of index 3 (arr[j + 1]) to temp(40)

Final output [10,20,30,40]
