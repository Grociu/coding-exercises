What an ugly piece of code, for this seemingly quite easy problem.

For Edabit, without f-strings I used

subtitles = subtitles.replace(timer_str[i],
            '{:02d}:{:02d}:{:02d},{:d}'.format(
                (timer_t[i].seconds) // 3600,
                (timer_t[i].seconds // 60) % 60,
                timer_t[i].seconds % 60,
                timer_t[i].microseconds
                )[:-3])

Other solutions have these interesting tidbits:
    
    i = TimeIncrement
    i = timedelta(hours=int(i[:2]), minutes=int(i[3:5]), 
                  seconds=int(i[6:8]), milliseconds=int(i[9:]))
    
This is probably much more eficient that another regex call. For a fixed lenghts
of strings this approach is definately easier.

 def convert(s):
        s = datetime.strptime(s, '%H:%M:%S,%f')
        return str((s + i).time())[:-3].replace('.', ',')

The strptime method of datetime is unknown to me but  seems to format a string of a given format into a 
time object. Author then adds the increment to this s, turns it into string cuts 3 digits off ms and replaces . with ,
I was wondering how to do it, this is probably a smart way.