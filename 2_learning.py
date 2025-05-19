# %%
import pandas as pd
import os
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
new_df = df[['单词', '解释']].copy()

# %%
l = len(new_df)
for i in range(l):
    print('-'*80)
    print(f"{i+1}. {new_df.loc[i,'单词']}")
    ans = int(input('1-OK 2-a_bit 3-NO!: '))
    # ans = 2
    if ans != 1:
        new_df.loc[i,'Mark'] = 1
    print(new_df.loc[i,'解释'])

print('*'*80)
print("下面这些单词还需要加强记忆：")
for i in range(l):
    if new_df.loc[i,'Mark'] == 1:
        print(f"{i+1}. {new_df.loc[i,'单词']}    {new_df.loc[i,'解释']}")
