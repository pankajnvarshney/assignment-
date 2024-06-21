#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


data=pd.read_csv("C:/Users/himan/Downloads/Active Users (4) (1) (1) (1).csv")


# In[4]:


data.head()


# In[5]:


data.info()


# In[11]:


data.columns


# In[10]:


# Reshape the data
long_data = data.melt(var_name='Week', value_name='Device_ID')

# Drop rows with missing values (if any)
long_data.dropna(inplace=True)



# In[12]:


# Sort data by Week
long_data.sort_values(by='Week', inplace=True)

# Display the reshaped data
long_data.head()


# In[16]:


data.describe()


# In[13]:


weekly_users = long_data.groupby('Week')['Device_ID'].apply(set).to_dict()

# Initialize lists to store metrics
weeks = sorted(weekly_users.keys())
new_users = []
retained_users = []
resurrected_users = []
churned_users = []

# Calculate metrics for each week
for i in range(1, len(weeks)):
    current_week = weeks[i]
    previous_week = weeks[i-1]
    
    current_users = weekly_users[current_week]
    previous_users = weekly_users[previous_week]
    
    new = current_users - previous_users
    retained = current_users & previous_users
    resurrected = current_users - new - retained
    churned = previous_users - current_users
    
    new_users.append(len(new))
    retained_users.append(len(retained))
    resurrected_users.append(len(resurrected))
    churned_users.append(len(churned))

# Create a DataFrame for easier analysis and visualization
metrics_df = pd.DataFrame({
    'Week': weeks[1:],
    'New Users': new_users,
    'Retained Users': retained_users,
    'Resurrected Users': resurrected_users,
    'Churned Users': churned_users
})

# Calculate Quick Ratio
metrics_df['Quick Ratio'] = (metrics_df['New Users'] + metrics_df['Resurrected Users']) / metrics_df['Churned Users']

# Display the metrics DataFrame
metrics_df.head()


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plot the metrics
plt.figure(figsize=(14, 8))
sns.lineplot(data=metrics_df, x='Week', y='New Users', label='New Users')
sns.lineplot(data=metrics_df, x='Week', y='Retained Users', label='Retained Users')
sns.lineplot(data=metrics_df, x='Week', y='Resurrected Users', label='Resurrected Users')
sns.lineplot(data=metrics_df, x='Week', y='Churned Users', label='Churned Users')
sns.lineplot(data=metrics_df, x='Week', y='Quick Ratio', label='Quick Ratio', linestyle='--')

plt.xlabel('Week')
plt.ylabel('Users')
plt.title('Weekly Growth Accounting Chart')
plt.legend()
plt.xticks(rotation=90)
plt.show()


# ### Considerations:
# Retained Users Can Be 0: Yes, if no users from the previous week remain active in the current week.
# 
# Churned Users Can Be 0: Yes, if all users from the previous week remain active in the current week.
# 
# Resurrected Users Can Be 0: Yes, if no previously inactive users return in the current week.

# In[18]:


plt.figure(figsize=(14, 8))

sns.lineplot(data=metrics_df, x='Week', y='New Users', label='New Users', marker='o')
sns.lineplot(data=metrics_df, x='Week', y='Retained Users', label='Retained Users', marker='o')
sns.lineplot(data=metrics_df, x='Week', y='Resurrected Users', label='Resurrected Users', marker='o')
sns.lineplot(data=metrics_df, x='Week', y='Churned Users', label='Churned Users', marker='o')
sns.lineplot(data=metrics_df, x='Week', y='Quick Ratio', label='Quick Ratio', marker='o', linestyle='--')

plt.xlabel('Week')
plt.ylabel('Users')
plt.title('Weekly Growth Accounting Chart')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[25]:


plt.figure(figsize=(14, 8))

sns.barplot(data=metrics_df, x='Week', y='New Users', label='New Users',color='r')
sns.barplot(data=metrics_df, x='Week', y='Retained Users', label='Retained Users',color='g')
sns.barplot(data=metrics_df, x='Week', y='Resurrected Users', label='Resurrected Users',color='b')
sns.barplot(data=metrics_df, x='Week', y='Churned Users', label='Churned Users',color='y')
sns.barplot(data=metrics_df, x='Week', y='Quick Ratio', label='Quick Ratio', linestyle='--',color='c')

plt.xlabel('Week')
plt.ylabel('Users')
plt.title('Weekly Growth Accounting Chart')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[ ]:




