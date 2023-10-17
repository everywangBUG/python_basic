from openpyxl.styles import Font, colors, Alignment, Border, Side
from openpyxl import load_workbook

# 设置单元格样式
myfont = Font(name="宋体", size=20, italic=True, color=colors.BLACK)

wb = load_workbook("住户模板.xlsx")
sheet = wb.get_sheet_by_name("住户模板")
sheet["A3"].font = myfont

# 水平居中和垂直居中
sheet["A3"].alignment = Alignment(horizontal="center", vertical="center")
sheet.row_dimensions[1].height = 80
sheet.column_dimensions["A"].width= 50

# 设置边框


wb.save("住户模板.xlsx")
