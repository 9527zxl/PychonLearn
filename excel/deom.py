import openpyxl

# 获取Excel文件
excel = openpyxl.load_workbook('./data/data.xlsx')
# sheet页的获取
sheet = excel['9527']
# 获取指定单元格的内容
data = sheet['A1'].value
# 获取所有sheet页
sheets = excel.sheetnames
# 获取整个sheet页内容
for values in sheet.values:
    print(values)
