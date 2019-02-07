#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua= UserAgent()
header= {"user-agent": ua.chrome}
response= requests.get("https://www.google.com/gmail/", headers= header)
#print(response.content)
soup= BeautifulSoup(response.content, "lxml")
soup.prettify()
title= soup.title
print (title.get("style"))
title.string.replace_with("Hello")
print(title.string)


# In[18]:


print(title.descendents)
print(title.parent)
print(title.parents)
print(title.next_sibing)
print(title.previous_sibling)


# In[ ]:




