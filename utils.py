import urllib.parse


def redirected_url(url: str):
    decoded_url: str = urllib.parse.unquote(url)
    if "=" not in url:
        return url
    first_indx = decoded_url.rfind("=") + 1
    last_indx = len(decoded_url)
    return  decoded_url[first_indx:last_indx]
