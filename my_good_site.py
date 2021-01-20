#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from core.mainWebPage import webpage
from core.mainWebPage import app as webapp
if __name__=='__main__':
	webapp.run(debug=True,host="0.0.0.0",port=9600)