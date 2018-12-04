#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os
import re


# In[35]:

def remove_extension(ext = '\.txt$'):

    """ this script will remove the specific extension of all the files in the current folder
    and list the content of the folder if success, this is a nice and short one, the old one
    under this is still working"""
    
    regex = re.compile(ext)
    
    file_list = os.listdir()
    file_list_new = [regex.sub('', file) for file in file_list]
    zipped = zip(file_list, file_list_new)
    
    for o, n in zipped:
        try:
            os.rename(o, n)
        except:
            print(f'{o}: access denied')
    
    os.listdir()

def remove_extension_old(ext = 'txt'):

    """ this script will remove the specific extension of all the files in the current folder
    and list the content of the folder if success"""
    
    file_list = os.listdir()
    
    file_list_splitted = []
    for file in file_list:
        file_list_splitted.append(file.split('.'))    # split the file name.
    
    for i, s in enumerate(file_list_splitted):
        if s[-1] == ext:
            s.pop()
        file_list_splitted[i] = '.'.join(s)           # remove the extension and join the file name back
    
    zipped = zip(file_list, file_list_splitted)
    
    for o, n in zipped:
        os.rename(o, n)


# In[41]:

def zero_one():
    
    """ changing the leading 1, 2, 3... in the file name to 01, 02, 03... for the sorting purpose."""
    
    file_list = os.listdir()
    
    for file in file_list:
        file_new = re.sub('^(\d) ', r'0\1 ', file)
        os.rename(file, file_new)

    os.listdir()


def remove_files_regex(regex):
    
    """ remove files that match a regex pattern"""
    
    for file in os.listdir():
        if regex.match(file):
            try:
                os.remove(file)
            except:
                print(f'{file}: file not exists')

    



