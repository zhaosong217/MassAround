import random
import pandas as pd
import time
import os

def profile():
    global current_time
    current_time = time.strftime("%Y%m%d")
    name = 'Jack'
    print(f"Welcome back {name}! Today is {current_time}")

def file_choice():
    print("Which file do you want to check?")
    global folder_path
    folder_path = '/Users/songzhao/Desktop/Eudic背单词/'
    file_list = os.listdir(folder_path)
    xlsx_lst = []
    for i in file_list:
        if i[:6] == 'Eudic_':
            xlsx_lst.append(i)
    for i in range(len(xlsx_lst)):
        print(f"{i+1}: {xlsx_lst[i]}")
    num = int(input('Please Enter the Number: '))
    global file
    file = folder_path + xlsx_lst[num-1]
    df = pd.read_excel(file)
    print(f"{xlsx_lst[num-1][:-5]} has {len(df)} words.\nYou can do it!")
    return file

def order():
    for i in range(len(df['No.'])):
        print(f"{i+1}. {df.loc[i, '解释']}")
        fill_blanks(df.loc[i,'单词'])
        text = input('Your response: ')
        df.loc[i, current_time] = text
        if text == df.loc[i,'单词']:
            print('Correct!')
        else:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
            print(f"Incorrect!-->{df.loc[i,'单词']}")
        print('-'*50)

def rd():
    nums = []
    length = len(df['No.'])
    for i in range(length):
        num = random.randint(0, length-1)
        while num in nums:
            num = random.randint(0, length-1)
        nums.append(num)
    cnt = 1
    for i in nums:
        print(f"{cnt}. {df.loc[i, '解释']}")
        fill_blanks(df.loc[i,'单词'])
        text = input('Your response: ')
        df.loc[i, current_time] = text
        if text == df.loc[i,'单词']:
            print('Correct!')
        else:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
            print(f"Incorrect!-->{df.loc[i,'单词']}")
        cnt += 1
        print('-'*50)

def ten(n):
    nums = []
    length = len(df['No.'])
    for i in range(n):
        num = random.randint(0, length-1)
        while num in nums:
            num = random.randint(0, length-1)
        nums.append(num)
    cnt = 1
    for i in nums:
        print(f"{cnt}. {df.loc[i, '解释']}")
        fill_blanks(df.loc[i,'单词'])
        text = input('Your response: ')
        df.loc[i, current_time] = text
        if text == df.loc[i,'单词']:
            print('Correct!')
        else:
            results.append([df.loc[i,'单词'], df.loc[i,'解释']])
            print(f"Incorrect!-->{df.loc[i,'单词']}")
        cnt += 1
        print('-'*50)

def model_choice():
    models = {1:'Order', 2:'Random', 3:'I want X!'}
    for k,v in models.items():
        print(f"{k}: {v}")
    num = int(input('Which model do you want to play: '))
    if num == 1:
        print('-'*50)
        order()
    elif num == 2:
        print('-'*50)
        rd()
    elif num == 3:
        n = int(input('How many words do you want to learn: '))
        print('-'*50)
        ten(n)

def fill_blanks(word):
    test_word = ''
    for letter in word:
        test_word += random.choice(['_', letter])
    print(test_word)

def main():
    global results
    results = []
    profile()
    global df
    df = pd.read_excel(file_choice())
    model_choice()

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

if __name__ == "__main__":
    main()
