# from django import forms

# from .models import Comments

# class AddCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['id', 'title', 'content']

#     def __init__(self, *args, **kwargs):
#         self._user = kwargs.pop('user')
#         super(AddCommentForm, self).__init__(*args, **kwargs)

#     def save(self, commit=True):
#         inst = super(AddCommentForm, self).save(commit=False)
#         inst.author = self._user
#         if commit:
#             inst.save()
#             self.save_m2m()
#         return inst
