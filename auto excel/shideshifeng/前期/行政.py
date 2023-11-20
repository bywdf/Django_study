import xlrd 

data = xlrd.open_workbook('行政后勤模板.xlsx') 
sheet = data.sheet_by_index(0)             

with open('行政后勤.txt', 'w') as f:
    for i in range(1,sheet.nrows):
        f.write('%s(%s)\n很满意\n满意\n基本满意\n不满意\n\n' 
                % (sheet.row(i)[0].value, sheet.row(i)[2].value))
        f.write('您对该人员不满意原因有[多选题]\n')
        f.write('A歧视、侮辱教师、学生、家长等\n')
        f.write('B组织、参与有偿补课，或推荐学生参加有偿补课\n')
        f.write('C举办或参与校外培训机构经营，到校外培训机构兼职任教\n')
        f.write('D索要财物，擅自推荐教辅材料、社会保险等\n')
        f.write('E敷衍管理，个人能力差，不作为\n')
        f.write('F大局意识淡薄，学校管理混乱，作风差，造成恶劣影响\n')
        f.write('G不尊重老师、家长和学生，对待他人态度恶劣\n')
        f.write('H接受他人礼品彩金等财物\n')
        f.write('H对该人员职业道德状况不满意的其他原因（手动填写）\n\n')
