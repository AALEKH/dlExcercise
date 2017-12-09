// For processing CDiscount bson train example

import numpy as np 
import pandas as pd 
import io
import os
import bson
import matplotlib.pyplot as plt
from skimage.io import *
import multiprocessing as mp 
import uuid

data = bson.decode_file_iter(open('train_example.bson', 'rb'))

prod_to_category = dict()
pictures = []
inter_ = ''
i = 0
for c, d in enumerate(data):
    # product_id = d['_id']
    if not os.path.exists(str(d['category_id'])):
    	os.makedirs(str(d['category_id']))
    # prod_to_category[product_id] = category_id
    for e, pic in enumerate(d['imgs']):
    	inter_ = './' + str(d['category_id']) + '/' + str(uuid.uuid4()) + '.jpg'
    	print inter_
        imsave(inter_, imread(io.BytesIO(pic['picture'])))
        # i = i+1
        # print i
