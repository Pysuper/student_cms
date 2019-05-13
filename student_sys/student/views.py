from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .forms import StudentForm
from .models import Student


def index(request):
    # students = Student.objects.all()
    students = Student.get_all()  # Student的model层中,封装了数据获取的逻辑
    # 对于用户提交的数据先做校验
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # # cleaned_data 是Form根据字段类型对用户提交的数据做完转换之后的结果

            # cleaned_data = form.cleaned_data
            # student = Student()

            # student.name = cleaned_data["name"]
            # student.sex  = cleaned_data["sex"]
            # student.email = cleaned_data["email"]
            # student.profession = cleaned_data["profession"]
            # student.qq = cleaned_data["qq"]
            # student.phone = cleaned_data["phone"]

            # student.save()

            # 在ModelFrom中有了Model的定义,这里手动构建Student对象的步骤可以省掉
            form.save()

            # 在urls.py中定义了name='index' ==> 这里使用reverse拿到对应的URL
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        "students": students,
        "form": form
    }

    # return render(request, 'index.html', context={"students":students})
    return render(request, 'index.html', context=context)


class IndexView(View):
    template_name = 'index.html'  # 直接从当前文件夹里面查找这个名字的模板文件

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context

    def get(self, request):
        # 只处理get请求
        context = self.get_context()
        form = StudentForm()
        # 使用get_content()获取了student数据 ==> 接着使用content.update()更新字典中的内容
        context.update({
            'form': form
        })
        # >>     context = {
        #         "students": students,
        #         "form": form
        #     }
        return render(request, self.template_name, context=context)

    def post(self, request):
        # 只处理post请求
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
