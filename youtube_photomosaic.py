#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request


def download_pic(url, _name="tmp", _type="png"):
    data = request.urlopen(url).read()
    filename = _name + "." + _type
    with open(filename, mode="wb") as f:
        f.write(data)
    return filename


if __name__ == '__main__':
    url = "https://yt3.ggpht.com/a-/ACSszfFbUaNMgfUp02dIH8cXWRz6U08PElsgrZuHng=s800-mo-c-c0xffffffff-rj-k-no"
    download_pic(url)
