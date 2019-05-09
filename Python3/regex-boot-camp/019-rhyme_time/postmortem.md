I'm quite happy with this code.

One of the other solutions has a "".join of raw findalls and then make them lower 
at the final comparisant, which is probably faster, as my .lower() changes the 
whole string first.