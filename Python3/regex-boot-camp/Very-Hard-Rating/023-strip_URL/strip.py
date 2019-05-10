import re

def strip_url_params(url, params_to_strip=[]):
    # establish domain and isolate parameters
    match_domain = re.match('^(.*)\?', url)
    if match_domain:
        domain = match_domain.group(1)
    else:
        return url
    # make a dictionary of all unique, non stripped parameters
    params_dict = {}
    for param in re.findall('\w*=\d*', url[len(domain)+1::]):
        key = re.match('(\w*)(=\d*)', param).group(1)
        if key not in params_to_strip:
            value = re.match('(\w*)(=\d*)', param).group(2)
            params_dict[key] = value
    # reeasemble url address
    domain += "?"
    for key, value in params_dict.items():
            domain += key + value + "&"
    return domain[:-1]
