from openpyxl import Workbook # 引入excel包

# 实例化创建一个excel文件
wb = Workbook()
# 获取当前active的sheet
sheet = wb.active
sheet.title = "excel"
print(wb.active) # 打印sheet名

# 写入数据
sheet["A1"] = "杨幂"
sheet["A2"] = "迪丽热巴"
sheet["A3"] = "赵丽颖"

sheet.append(["周慧敏"])

wb.save("star.xlsx")
