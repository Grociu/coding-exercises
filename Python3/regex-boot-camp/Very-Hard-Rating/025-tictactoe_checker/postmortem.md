While this excersise hardly used regex, I still enjoyed the challenge.

The tricky part for me was figuring out that one letter in the string had to be
called by a[row][0][letter]

Type check for an item is probably best done with:

isinstance(i, list)
isinstance(i[0], str)

as other users did. Also in my example I used type(row) != type([]) but these:

(type(row[0]) != str)
(type(row) != list)

are better.