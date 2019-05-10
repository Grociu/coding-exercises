
Strip URL Query Parameters

Create a function that takes a URL (string), removes duplicate query parameters and parameters specified within the 2nd argument (which will be an optional list).
Examples

strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"

strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"

strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"

Notes

    The 2nd argument params_to_strip is optional.
    params_to_strip can contain multiple params.
    If there are duplicate query parameters with different values, use the value of the last occuring parameter (see examples #1 and #2 above).

