I'm adding a lot of comments, but the idea is to understant the
underlying principles. This was 3rd exercise from the Very Easy pool on Edabit,
so I'm moving up a category.

Originally, I used a construct like

pattern = re.compile('[aeiou]')
return pattern.sub(ch, txt)

Which was different than current solution that is more elegant. re.sub is more 
intuitive and simpler.

I'm also aware that I don't really have to define the pattern first, but I find
it useful in future proofing - I could define the pattern as simply vowels, 
that would make it more readable.