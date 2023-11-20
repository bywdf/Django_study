import xlrd 

data = xlrd.open_workbook('2022级教师信息.xlsx') 
sheet = data.sheet_by_index(0)             

with open('2022级教师信息.txt', 'w', encoding='utf-8') as f:
    for i in range(1,sheet.nrows):
        f.write('高二 %s(%s)\n很满意\n满意\n基本满意\n不满意\n\n' 
                % (sheet.row(i)[0].value, sheet.row(i)[2].value))
        f.write('师德不满意原因[多选题]\n')
        f.write('A歧视、侮辱、体罚或变相体罚学生\n')
        f.write('B组织、参与有偿补课，或推荐学生参加有偿补课\n')
        f.write('C举办或参与校外培训机构经营，到校外培训机构兼职任教\n')
        f.write('D索要学生及家长财物，擅自推荐教辅材料、社会保险等\n')
        f.write('E敷衍教学，教学能力差，让家长代为评改作业\n')
        f.write('F德育意识淡薄，班级管理或课堂管理混乱，造成恶劣影响\n')
        f.write('G不尊重家长，对待家长态度恶劣\n')
        f.write('H接受家长礼品彩金等财物\n')
        f.write('I对该教师职业道德状况不满意的其他原因\n\n')

