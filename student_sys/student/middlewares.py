# 统计首页每次访问程序所消耗的时间 ==> Django接收请求到最终返回的时间
import time
from django.urls import reverse

from django.utils.deprecation import MiddlewareMixin


class TimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 请求来到middleware中进入的第一个方法
        # 一般可以在这里做一些校验 ==> '用户登录'或者'HTTP中是否有认证头'这类的认证
        # 可以有两种返回值 ==>
        # 如果返回HttpResponse : 接下来的处理方法只会执行process_response, 其他方法将不会执行
            ### 注意: 如果你的middleware是setting配置的MIDDLEWARE的第一个, 那么剩下的middleware也不会被执行
        # 如果返回None :那么django会执行其他方法
        return

    def process_view(self, request, func, *args, **kwargs):
        # 统计调用View所消耗的时间
        # 在执行process_request之后执行,
        # func :就是我们要执行的view
        #
        if request.path != reverse('index'):
            return None

        start_time = time.time()
        response = func(request)
        costed = time.time() - start_time
        print('process view: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response
