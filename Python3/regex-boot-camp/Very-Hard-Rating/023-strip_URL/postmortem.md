This code is ugly and complex, but I think it's readable.

It does not beat the Edabit built in test function, because of a dictionary being unindexed (order matters for output). Edabit does not run Python 3.7, no f'strings of saving of insertion order for dictionaries.

Irewrote the function for Edabit using 2 lists instead.

It's far from optimized though :(