# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: teacher.py
#@datatime: 2023/4/12 下午1:15

from user import User
class Teacher(User):
    def __init__(self, name, pwd, sex, birth, education, teach_course):
        super(Teacher, self).__init__(name, pwd, sex, birth, education)
        self.teach_course = teach_course # 主讲课程
        self.identity = 2

if __name__ == '__main__':
    taibai = Teacher('太白', '123456', 'male', '1980-11-01', '研究生', 'python')
    print(taibai)
    print(taibai.identity)
