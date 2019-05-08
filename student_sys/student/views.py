from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .forms import StudentForm
from .models import Student


def index(request):
    students = Student.objects.all()
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
        "students":students,
        "form":form
    }

    return render(request, 'index.html', context={"students":students})
