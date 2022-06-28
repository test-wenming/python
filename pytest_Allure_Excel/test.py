# test_fixture.py

# import pytest
#
# @pytest.fixture()
# def fixtureFunc():
#     return '返回fixtureFunc'
#
# def test_fixture(fixtureFunc):
#     print('我调用了{}'.format(fixtureFunc))
#
# class TestFixture(object):
#     def test_fixture_class(self, fixtureFunc):
#         print('在类中使用fixture "{}"'.format(fixtureFunc))
#
# if __name__=='__main__':
#     pytest.main(['-sv', 'test.py'])

# import pytest
#
#
# def read_yaml():
#     return ["1,1a,1b","2,2a,2b" ]
#
#
# @pytest.fixture(params=read_yaml())
# def get_param(request):
#     return request.param
#
#
# def test01(get_param):
#     print('测试用例：' + get_param)
#     print(type(get_param))
#
#
# if __name__ == '__main__':
#     pytest.main(['-sv', 'test.py'])

# test_fixture.py
# import pytest
# @pytest.fixture()
# def fixtureFunc():
#     print('\n ############fixture->fixtureFunc########')
#
# @pytest.mark.usefixtures('fixtureFunc')
# def test_fixture():
#     print('-----in test_fixture-----')
#
# class TestFixture(object):
#     def test_fixture_class(self):
#         print('+++++++++in class with text_fixture_class+++++++++')
#
# if __name__=='__main__':
#     pytest.main(['-s', 'test.py'])

# init = [123456789.0, 123456.0, 1234.0]
# print(init[0])


# a = 'login/test_login.py::Test_Login::test_UI_0001[cs-001]'
#
# b = a.split("[")[-1][:-1]
# print(b)
# from pprint import pprint
#
# import requests
# import re
#
# list_kong = []
# list_chongfu = []
#
# for i in range(5):
#     response = requests.get(f"http://h5.daluxmall.com/recommend-service/firstpagesuggest?dataType=local&deviceUniqueId=3EC1F3F3-29B5-4936-ABF3-D5AB9B9D04E4&key=daa25f5102a46b4ac621983930cc9b1e&lang_type=zh_cn&language=zh_cn&localLastpage=0&memberId=135321&pageNo={i}&pageSize=20&userGender=3")
#     obj = response.json()
#     # pprint(obj)
#     goods_name = re.compile(r'\'goods_name\': \'(.+?)\',')
#     common_id = re.compile(r"goods_collect.+?\'goods_commonid\': \'(.+?)\'", re.DOTALL)
#     list1 = []
#     list2 = []
#     for one in goods_name.findall(str(obj)):
#         list1.append(one)
#     for two in common_id.findall(str(obj)):
#         list2.append(two)
#
#     list_name_common = zip(list(list1), list(list2))
#
#     for x, y in list_name_common:
#         print(f"goods_commonid:{y}        goods_name:{x}")
#         if x not in list_kong:
#             list_kong.append(x)
#         else:
#             list_chongfu.append(x)
#
# print(list_chongfu)

        # with open(r"C:\Users\Administrator\Desktop\商品名和commonid.txt","a",encoding='utf8') as f:
        #     f.write(f"\n{y}                           {x} \n")
        #     f.close()


# import xlrd
#
# book = xlrd.open_workbook("信息.xlsx")
#
# # 得到所有sheet对象
# sheets = book.sheets()
#
# incomeOf3years = 0
# for sheet in sheets:
#     print(sheet)
i = 0
while i < 4:
    print(i)
    i +=1
