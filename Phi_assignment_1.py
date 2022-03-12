#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Check working directory
pwd

#Change Working Directory
get_ipython().run_line_magic('cd', 'C:\\Users\\malak\\Desktop\\bioinfomratics')


# In[17]:


#import Pandas
import pandas as pd
#import numpy
import numpy as np
#Open CSV file, hapc=Haplotype Comparison
hapc= pd.read_csv("phi_Assigment.csv")


# In[13]:


#View data
print(hapc)


# In[48]:


#Create a list that contains the following elements: Type, Filter, TRUTH.TP, TRUTH.FN, QUERY.FP, METRIC.Precision.

hapc_list=["Type", "Filter", "TRUTH.TP","TRUTH.FN", "QUERY.FP", "METRIC.Precision"]

# Use the list to subset the data frame and keep the desired columns.
hapc_sub=hapc[hapc_list]
#View hapc_sub
hapc_sub


# In[52]:


#Create two numpy arrays, one with the TRUTH.TP numbers and another with the QUERY.FP numbers
Truth_TP= np.array(hapc_a["TRUTH.TP"])
QUERY_FP= np.array(hapc_a["QUERY.FP"])


# In[53]:


#Calculate precision using your numpy arrays. Hint: Precision = True Positives /(True Positives + False Positives)
precision= Truth_TP/(Truth_TP+QUERY_FP)


# In[69]:


# Compare your values to the values in “METRIC.Precision”
METRIC=np.array(hapc_a["METRIC.Precision"])
np.round(METRIC,2)==np.round(precision,2)

#view rounded values
print(np.round(precision,2))


# In[65]:





# In[ ]:




