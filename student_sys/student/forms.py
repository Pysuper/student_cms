from django import forms
from .models import Student

"""使用Form"""
# class StudentForm(forms.Form):
#     name = forms.CharField(label="姓名", max_length=128)
#     sex = forms.ChoiceField(label="性别", choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label="职业", max_length=128)
#     email = forms.EmailField(label="邮箱", max_length=128)
#     qq = forms.CharField(label="QQ", max_length=128)
#     phone = forms.CharField(label="手机", max_length=128)


"""使用ModelForm"""
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = (
#             "name", "sex", "profession", "email", "qq", "phone"
#         )


"""增加QQ号必须为纯数字的校验"""
class StudentForm(forms.ModelForm):
    def clean_qq(self):
        # 自动调出来处理每个字段的方法 ==> 可以使用clear_phone()来校验手机号码....
        cleaned_data = self.cleaned_data["qq"]

        # 校验QQ必须为纯数字
        if not cleaned_data.isdigit():
            # 异常会存储到Form中, 最后渲染到页面中
            raise forms.ValidationError("必须是数字.")

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            "name", "sex", "profession", "email", "qq", "phone"
        )
