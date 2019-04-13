# Sorting Algorithm

### Bubble Sort

* bubble up the highest number
* one of the simplest but least efficient
* first step of learning sorting algorithm
* O(n^2): time complexity
* O(1): space complexity
* mostly never gonna use this sort (only used for an education purpose for the lack of efficiency)

### Selection Sort

* scan through array to locate the smallest element
* after one full scan, move the smallest element to the first
* repeat until all sorted out
* O(n^2): time complexity
* O(1): space complexity
* not very fast
* mostly won't be using this (but just for an education purpose)

### Insertion Sort

* not best efficient but efficient in some scenarios like almost sorted
* also works well with the small data set
* scan through elements and insert each element where it should belong
* O(n^2): time complexity
* O(1): space complexity
* useful with a small size of arry or almost sorted
* space complexity is good and easy to implement

### Merge Sort

* divide & conquer
* time: O(n log n)
* space: O(n) : to hold the divided list in memory
* divide array in half, divide again and again, until we have one item
* take 1st and 2nd item, determine which one to place first (reversed tree)
* combine (Merge) together by determine which element to place first
* efficient, typically perform better
* stable when some elements are same as it keeps the original layout
* if you are worried about a worst case with quick sort, use this
* one cost is with a higher space complexity
* note: (log n) is kind of like the height of the tree

### Quick Sort

* one of the most popular algorithm
* divide & conquer algorithm
* time: O(n log n)
* usually fastest on average but one downside is a worst case: O(n^2) if you choose a wrong pivot element
* space: O(log(n))
* choose a pivot (element) and compare and place left if it's 
* smaller and right if it's larger
* then use divide & conquer logic + recursion of quick sort in 
* each divided list from there in the right place of the pivot 
* elementary and combine them in the end

### Shell Sort

* time complexity: average or wost case O((n log n)^2), best case (O(n log n))
* space complexity: O(1)

### Heap Sort

* similar to merge or quick sort
* time complexity: O(n log n)
* space complexity: O(1)
* usually slower than quick sort