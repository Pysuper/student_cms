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
        ### 注意: 如果你的middleware是setting配置的MIDDLEWARE的第一个, 那么剩下的middleware也不会被执行 ###
        # 如果返回None :那么django会执行其他方法
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        # 统计调用View所消耗的时间
        # 在执行process_request之后执行,
        # func :就是我们要执行的view ==> 在这里统计一个view的执行时间
        # 逻辑也和上面一样， 如果返回值为None ==> Django会执行view函数 ==> 从而得到最终的response
        if request.path != reverse('index'):
            return None

        start_time = time.time()
        response = func(request)
        costed = time.time() - start_time
        print('process view: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        # 只有在发生异常时，才会执行这个方法
        # 在将要调用的View中出现异常(process_view的func函数中) / 或者返回的模板response在渲染是发生异常
        # 但是如果在process_view中手动调用了func ==> 就不会出发这个函数了
        # 方法收到异常后，返回一个带有异常信息的HttpResponse,或者直接返回None不处理 ==> 使用Django自带的异常模板
        pass

    def process_template_response(self, request, response):
        # 从process_view中获的response,使用模板的response(通过return render(request, 'index.html', content={})返回的response)
        # 在这里可以修改这种response的header ==> 增加、修改
        return response

    def process_response(self, request, response):
        # 在所有流程都处理完之后，就会来到这
        # 逻辑和上面一样， 只是这里针对带有模板的response的处理
        costed = time.time() - self.start_time
        print('request to response cose : {:.2f}s'.format(costed))
        return response
