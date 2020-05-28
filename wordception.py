#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[1]:


import pandas as pd
import mysql.connector as sql


# ### Import all words

# In[2]:


db_connection = sql.connect(host='localhost', database='wn_pro_mysql', user='root', password='anuj123456', auth_plugin='mysql_native_password')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM wn_synset')
table_rows = db_cursor.fetchall()
words_df = pd.DataFrame(table_rows)


# In[3]:


words_df.head(10)


# In[4]:


len(words_df)


# ### Keep required columns

# In[5]:


words_df = words_df.drop(columns=[0,1,3,4,5])


# In[6]:


words_df = words_df.rename(columns={2 : "word"})


# In[7]:


words_df.head()


# ### Strip any leading or trailing spaces

# In[8]:


words_df['word'] = words_df['word'].str.strip()


# In[9]:


words_df.head()


# In[10]:


len(words_df)


# ### Remove any word with underscore '_' as it signifies the word contains a space and its not a single word

# In[11]:


words_df = words_df[~words_df.word.str.contains('_')]


# In[12]:


len(words_df)


# ### Replace non alpha character with empty character

# In[13]:


words_df = words_df[words_df.word.str.isalpha()]


# ### Create a column for word length

# In[14]:


words_df['word_len'] = words_df['word'].str.len()


# In[15]:


words_df.head()


# In[16]:


len(words_df)


# In[17]:


words_df = words_df.sort_values(by=['word'])


# In[18]:


words_df.head()


# ### Drop Duplicates

# In[19]:


words_df.drop_duplicates(subset="word", keep = 'first', inplace = True)


# In[20]:


len(words_df)


# In[21]:


words_df.head(10)


# ### Export the final dataset to csv

# In[31]:


words_df.to_csv('data/words_dataset_edit.csv')


# ### Create a global list 'globvar' to keep a track of valid words found

# In[23]:


#Declare the global var
globvar = []

#Function to reset global list before a new word is started
def reset_word_list():
    global globvar
    globvar = []
    
#Function to update global list and add a new word (val)
def set_word_list(val):
    global globvar
    globvar.append(val)

#Function to return global list
def return_globvar():
    return globvar

#Function to print global list
def print_globvar():
    print(globvar)

#Analyse the list global list for current word if a continuous chunk of valid words is found with 
#length of word decreasing by 1
def analyse_list(word, word_len):
    length = word_len
    flag = 0      #Flag will remain zero if len(globvar[i] != len(globvar[i-1]))
    word_str = []
    #Iterate through entire global list
    for i in range(0, len(globvar)):
        
        #If length becomes 1 then a valid chain of words is found whose length is in decreasing order
        if flag == 1 and length == 1:
            
            word_str.append(word +  " -> ")
            for j in range(i - word_len + 1 , i):
                word_str.append(globvar[j] + " -> ")
            return word_str
            
        elif len(globvar[i]) == length - 1:
            flag = 1
            length = length - 1
        else:
            flag = 0
            length = word_len
    
    return 0


# ### Function which keeps o chopping a word recursively and looks if the wor dis valid

# In[24]:


def chop(word):
    word_len = len(word)
    
    #If valid word is found, push it in globvar
    if len(words_df[words_df['word'] == word]) > 0:
        set_word_list(word)
        
        #For each valid word found, repeat the process of chopping one letter one by one recursively
        for i in range(0, word_len):
            new_word = word[0:i] + word[i+1:]
            chop(new_word)


# ### Number of 9 letter words in our dictionary

# In[26]:


len(words_df[words_df['word_len'] == 9])


# ### Create a dataframe with 9 letter words

# In[27]:


words_df_9 = words_df[words_df['word_len'] == 9]
words_df_9.head()


# ### Call to function to find 9-letter 'magic word'

# #### This piece of code will take time to run, you can uncomment the print statement to check the progress

# In[28]:


magic_word = []
for index, row in words_df_9.iterrows():
    
    word = row['word']
    word_len = row['word_len']
    
    #print("Current word: ", word)
    reset_word_list()
    chop(word)
    current_result = analyse_list(word, word_len)
    if current_result != 0:
        print(current_result)
        magic_word.append(current_result)


# ### Print Final list of all such magic words

# In[29]:


for word in magic_word:
    print(word)

