import pdfplumber
import pandas as pd

# PDF file name是从Eudic导出PDF文件名中第二个_后面的数字，例如20250502_1553
pdf = input("Enter the PDF file name: ")
# pdf_file 由两部分组成，其中前面部分是导出生词本的名称，例如Daily Vocabulary
pdf_file = f'我的生词本_{pdf}.pdf'
# 设置导出Excel名字的格式（日期）
excel_file = pdf_file.split('_')[1]
# 提取PDF中的所有表格
tables = []
# 注意修改成你自己的文件夹路径
with pdfplumber.open("/Users/songzhao/Desktop/Eudic背单词/"+pdf_file) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        tables.extend(table)
# 导出的表格中可能存在前后各有两个None或者''，需要删除掉
for i in tables:
    if len(i) > 4:
        i.pop(0)
        i.pop(0)
        i.pop()
        i.pop()
# 存为DataFrame格式，导出成Excel
df = pd.DataFrame(tables[1:], columns=tables[0])
df.to_excel(f'/Users/songzhao/Desktop/Eudic背单词/Eudic_{excel_file}.xlsx',index=False)
