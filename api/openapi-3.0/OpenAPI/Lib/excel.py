import xlrd, xlwt, os, sys, openpyxl


# 读取excel
def read_excel(excel_name='', sheet_name='', col_name=''):
    # 打开excel
    workbook = xlrd.open_workbook(excel_name)
    # print(workbook.sheet_names())
    sheet = workbook.sheet_by_name(sheet_name)
    rows = sheet.nrows
    cols = sheet.ncols
    client_id_row_col = {}
    all_client_id = []
    # 取出col_name列
    for i in range(rows):
        for j in range(cols):
            if sheet.cell_value(i, j) == col_name:
                client_id_row_col.update({'row': i, 'col': j})
    # 格式化col_name列内容
    for i in range(client_id_row_col['row'], rows):
        if sheet.cell_value(i, client_id_row_col['col']) == col_name:
            continue
        # print(sheet.cell_value(i, client_id_row_col['col']), sheet.cell_type(i, client_id_row_col['col']))
        # 部分为float格式，强制转换为int，再转换为str，格式统一
        all_client_id.append(str(int(sheet.cell_value(i, client_id_row_col['col']))))
        # all_client_id.append(sheet.cell_value(i, client_id_row_col['col']))
    print(col_name, "总共", len(all_client_id))
    return all_client_id


# 写excel
# 指定文件名、表名、写入行、列、表头、内容（为列表）
def write_excel(excel_name='', sheet_name='', row=0, col=0, col_value='', content=[]):

    # 单元格格式
    style = xlwt.XFStyle()
    font = xlwt.Font()
    # 字体
    font.name = 'Times New Roman'
    # 加粗
    font.bold = True
    style.font = font

    pattern = xlwt.add_palette_colour()

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
    sheet.write(row, col, col_value)
    for i in range(len(content)):
        sheet.write(i+1, col, content[i], style)
    workbook.save(excel_name)
    return


# 修改excel row：行   col：列
def rewrite_excel(excel_name='', sheet_name='', row=0, col=0, content=''):
    # 获取excel表
    workbook = openpyxl.load_workbook(excel_name)
    worksheet = workbook[sheet_name]
    # 写入数据
    worksheet.cell(row, col, content)
    # 保存excel，会覆盖之前的excel（如果在office中已经打开，会报错）
    try:
        workbook.save(filename=excel_name)
    except:
        raise AssertionError(excel_name, '已经打开，请先关闭!')
    return


sheet = read_excel(r'C:\Users\lfchao\Desktop\1-9迁移-test.xlsx', '迁移商户-all-test', '商户id')
print(sheet)
rewrite_excel(r'C:\Users\lfchao\Desktop\1-9迁移-test.xlsx', '迁移商户-all-test', 2, 1, 'hello123你好')

# tmp_list = []
# tmp_list2 = []
# sheet_new = read_excel(r'C:\Users\lfchao\Desktop\3-6迁移名单（3-4确认）.xlsx', 'Sheet1', '商户id')
# print(sheet1)
# sheet_old = read_excel(r'C:\Users\lfchao\Desktop\3-6迁移.xlsx', '迁移商户-all', '商户id')


# only_in_sheet_old = []
# only_in_sheet_new = []
# for tmp_old in sheet_old:
#     if tmp_old in sheet_new:
#         continue
#     else:
#         only_in_sheet_old.append(tmp_old)
#         print(tmp_old, ' not in 3-6迁移名单（3-4确认）.xlsx')
# print("##############################################")
# for tmp_new in sheet_new:
#     if tmp_new in sheet_old:
#         continue
#     else:
#         only_in_sheet_new.append(tmp_new)
#         print(tmp_new, ' not in 3-6迁移.xlsx')
# print('only in sheet new: \n', len(only_in_sheet_new))
# print(only_in_sheet_new)
# print('only in sheet old: \n', len(only_in_sheet_old))
# print(only_in_sheet_old)

# write_excel(r'C:\Users\lfchao\Desktop\test.xlsx', 'test', 0, 0, 'test', [0, 2, 'test'])



