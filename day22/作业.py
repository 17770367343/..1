# class Circle:
#     '''创造一个圆对象，其包含一个半径属性radius，以及两个方法面积area、周长perimeter'''
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return round(3.14*self.radius**2,3)
#     def perimeter(self):
#         return round(2*3.14*self.radius,3)
#
# circle1 = Circle(5)
# circle2 = Circle(10)
# print(circle1.__dict__,circle2.__doc__)
# print(circle1.area(),circle1.perimeter(),circle2.area(),circle2.perimeter())
# import json
# class User:
#     def __init__(self,name,pwd):
#         with open('register','r',encoding='utf-8')as f:
#             self.user_dic = json.load(f,encoding='utf-8')
#         if self.user_dic[name] == pwd:
#             self.name= name
#             self.password = pwd
#         else:
#             return print('用户名或密码错误！')
#     def change(self,newpwd):
#         self.password = newpwd
#         with open('register','w',encoding='utf-8')as f:
#             self.user_dic[self.name] = self.password
#             json.dump(self.user_dic,f,ensure_ascii=False)
#         print('密码修改成功！')
# 小白 = User('小白','mm123')
# print(小白.name)
# print(小白.password)
# 小白.change('mm456')
# print(小白.password)