# 1. 要求⽤户输⼊姓名、年龄、⼿机号、身份证号、所选课程，然后为学员完成注册
# 2. ⼿机号、身份证号唯⼀
# 3. 可选的课程只能从Python、Linux、⽹络安全、前端、数据分析 这⼏⻔⾥选
# 4. 学员信息存⼊⽂件

course_list = ["Python", "Linux", "⽹络安全", "前端", "数据分析"]
db__stu_file = "stu_info.txt"

def base_info():
    """ 学生信息输入
    :return: stu_data
    """
    stu_data = {}
    name = input("输入姓名：").strip()
    age = input("输入年龄：").strip()
    mobile = input("输入电话：").strip()
    identify = input("输入身份证号：").strip()
    
    selected_duplicate(mobile, identify)
    
    for i, c in enumerate(course_list):
        print(f"{i}. {c}")
    selected_course = input("选择以上课程输入：")
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if selected_course >= 0 and selected_course <= len(course_list):
            print("选择课程成功")
        else:
            print("请选择以上列表中的课程\n")
    else:
        exit("非法输入...")

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["mobile"] = mobile
    stu_data["identify"] = identify
    stu_data["course"] = course_list[selected_course]
    
    return stu_data


def selected_duplicate(mobile, identify):
    """ 手机号和身份证号唯一性
    :param: 手机号
    :param: 身份证号
    """
    f1  = open("stu_info.txt", mode="r", encoding="utf-8")
    for line in f1:
        line = line.split()
        has_mobile = line[2]
        has_identify = line[3]
        if mobile == has_mobile:
            print("该手机号已注册\n")
            base_info()
        if identify == has_identify:
            print("该身份证已注册")
            base_info()
            

def write_base_txt(filename: str, student_data: list):
    """ 学员数据存到文件中
    :param: filename文件名称
    :param: student_data学生数据
    """
    f = open("stu_info.txt", mode="a", encoding="utf-8")
    f.write(student_data["name"]+ " ")
    f.write(student_data["age"] + " ")
    f.write(student_data["mobile"] + " ")
    f.write(student_data["identify"] + " ")
    f.write(student_data["course"] + "\n")
    f.close()

stu_data = base_info()
write_base_txt(db__stu_file, stu_data)
print("完成注册")
