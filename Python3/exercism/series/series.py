def slices(series, length):
    if length < 1:
        raise ValueError("length minimum is 1")
    if len(series) < length:
        raise ValueError("length > series")
    return [series[i:i+length] for i in range(0,len(series)-length+1)]