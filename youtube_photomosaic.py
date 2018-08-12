#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request
from pandas import DataFrame
from PIL import Image

import numpy as np


def download_img(url, _name="tmp", _type="png"):
    data = request.urlopen(url).read()
    filename = _name + "." + _type
    with open(filename, mode="wb") as f:
        f.write(data)
    return filename


def create_img_df(img_path_list):
    data = {"filepath": [], "buffer": [], "ary_rgb": []}
    for path in img_path_list:
        # filepath
        data["filepath"].append(path)
        im = Image.open(path)
        # buffers of PIL Image
        data["buffer"].append(im)
        im = np.array(im)
        # the rgb average of the image
        data["ary_rgb"].append((im[:, :, 0].mean(dtype=np.int32),
                                im[:, :, 1].mean(dtype=np.int32),
                                im[:, :, 2].mean(dtype=np.int32)))
    return DataFrame(data)


def update_buffer(df):
    df["filepath"].apply(Image.open)


if __name__ == '__main__':
    im = Image.open('/Users/yameholo/Dropbox/PythonProject/YouTube-PhotoMosaic/tmp.png')
    print(im)
    im = np.array(im)
    print(im)
    print(im[:, :, 0].mean(dtype=np.int32), im[:, :, 1].mean(dtype=np.int32), im[:, :, 2].mean(dtype=np.int32))

    url = "https://yt3.ggpht.com/a-/ACSszfFbUaNMgfUp02dIH8cXWRz6U08PElsgrZuHng=s800-mo-c-c0xffffffff-rj-k-no"
    # download_img(url)
