## Access Hint

Did you account for base cases like numRows = 0, numRows = 1 ?

Take a look at how we can approach this problem.

Notice that the first and last numbers in each row ( for row >= 2 ) are 1 and 1.

For all the other numbers:

num at position i = number at position i in prev row + number at position (i + 1) in previous row.

Also, notice that for a row, you only need the value in the previous rows.

The values in i-2 row do not matter.

As such, all you need is to maintain 2 vectors and alternate between them.
