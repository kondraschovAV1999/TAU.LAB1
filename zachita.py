# tuple1 = list()
# for i in range(1, 11):
#     tuple1.append(i)
# tuple1 = tuple(tuple1)
# print(tuple1)
# list1 = list()
# for i in tuple1:
#     if i % 2 == 0:
#         list1.append(i * 5)
#     else:
#         list1.append(i + 3)
# list1.extend(list(tuple1))
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# set1 = set()
# for i in list1:
#     set1.add(i)
# print(set1)
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


class ComputerTable(DeskTable):
    def square(self, e):
        return self.width * self.length - e