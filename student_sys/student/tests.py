from django.test import TestCase,Client
from .models import Student

# Create your tests here.
# app初始化时，Django默认创建的
class StudentTestCase(TestCase):
    def setUp(self):
        """创建初始化的数据"""
        Student.objects.create(
            name='张三',
            sex = 1,
            email = 'nobody@123.com',
            profession = '程序员',
            qq = '123123123',
            phone = '123123123',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name = '李四',
            sex = 2,
            email = 'have_body@123.com',
            profession = 'Web',
            qq = '321321321',
            phone = '123321231',
        )
        self.assertEqual(student.sex_show, "女","性别字段内容跟显示不一致")

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='have_2_body@123.com',
            profession='全栈',
            qq='32132132',
            phone='12331231',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'student code must be 302!')

        response = client.get('/')
        # 这里的b'' ==>是为了声明他是bytes类型， 而不是字符串类型
        self.assertEqual(b'test_for_post' in response.content, 'response content must contain "test_for_post"')