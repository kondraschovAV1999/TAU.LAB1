# # Лекция №2
# def hello_concat(arg1, arg2):
#     print(arg1, ', from', name)
#
#
# def hello_from_with5(arg1, name, times):
#     print('%s, from %s for %.2f times' %(arg1, name, times))
#
#
# def hello_from_format(arg1, name, times):
#     print('{0}, from {1} for {2} times '.format(arg1, name, times))
#
# print('{}'.format(['elem1', 'elem2', 'elem3']))
# print('{:.3f}'.format(7.0 / 3))
# the_string = 'Hello, world'
# print(the_string)
# name = input('Введите имя: ')
# print(name)
# times = 5
# hello_concat(the_string, name)
# hello_from_with5(the_string, name, times)
# hello_from_format(the_string, name, times)


# def list_creater(to, start=1, step=1):
#     new_list = list()
#     for i in range(start, to, step):
#         new_list.append(i)
#     return new_list
#
#
# list2 = list_creater(10, 2, 3)
# print(list2)

# def tuple_creator_om_list_base(base):
#     new_tuple = tuple(range(base))
#     return(new_tuple)
#
# tuple2= tuple_creator_om_list_base(10)
# print(tuple2)

# def set_creator(to, start=1, step=1):
#     new_set = set()
#     for i in range(start, to, step):
#         new_set.add(i)
#     return new_set
#
#
# set2 = set_creator(15)
# print(set2)

def dict_creator(base):
    new_dict = dict()
    for i in range(base):
        new_dict[i] = i*2
    return new_dict

