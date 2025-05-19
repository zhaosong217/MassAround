# %%
import pandas as pd
import os
import time

print('*'*50)
current_time = time.strftime("%Y%m%d")
print(f"Welcome back Jack! Today is {current_time}\nWhich file do you want to check?")
# %%
folder_path = '/Users/songzhao/Desktop/Eudic背单词/'
file_list = os.listdir(folder_path)
xlsx_lst = []
for i in file_list:
    if i[:6] == 'Eudic_':
        xlsx_lst.append(i)
for i in range(len(xlsx_lst)):
    print(f"{i+1}: {xlsx_lst[i]}")
# %%
num = int(input('Plese Select a file to learn: '))
# num = 5
file = folder_path + xlsx_lst[num-1]
df = pd.read_excel(file)
print(f"{xlsx_lst[num-1][:-5]} has {len(df)} words.\nYou can do it!")
# %%
models = {1:'Order', 2:'Random', 3:'I want TEN!'}
for k,v in models.items():
    print(f"{k}: {v}")
model = int(input('Please select the model: '))
print('*'*50)



results = []
# order model
def order():
    for i in range(len(df['No.'])):
        print(f"{i+1}. {df.loc[i, '解释']}")
        text = input("Enter your response:\n")
        df.loc[i, current_time] = text
        if text != df.loc[i, '单词']:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
        print('-'*50)

# random model
import random
nums = []
def rd():
    length = len(df['No.'])
    for i in range(length):
        num = random.randint(0, length-1)
        while num in nums:
            num = random.randint(0, length-1)
        nums.append(num)
    cnt = 1
    for i in nums:
        print(f"{cnt}. {df.loc[i, '解释']}")
        text = input("Enter your response:\n")
        df.loc[i, current_time] = text
        if text != df.loc[i, '单词']:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
        cnt += 1
        print('-'*50)

# TEN model
def ten():
    nums = []
    length = len(df['No.'])
    for i in range(10):
        num = random.randint(0, length-1)
        while num in nums:
            num = random.randint(0, length-1)
        nums.append(num)
    cnt = 1
    for i in nums:
        print(f"{cnt}. {df.loc[i, '解释']}")
        text = input("Enter your response:\n")
        df.loc[i, current_time] = text
        if text != df.loc[i, '单词']:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
        cnt += 1
        print('-'*50)

if model == 1:
    order()
elif model == 2:
    rd()
else:
    ten()

# modify the original file
df.to_excel(file, index=False)

if len(results) == 0:
    print("Awesome! No wrong word!")
else:
    print("The following words are wrong:")
    for i in range(len(results)):
        print(f"{i+1}. {results[i][0]}, {results[i][1]}")
    # generate a file that contain wrong words
    res = pd.DataFrame(results, columns=['单词','解释'])
    res.to_excel(f"{folder_path}{current_time}.xlsx",index=False)
