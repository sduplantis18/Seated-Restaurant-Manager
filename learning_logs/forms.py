from django import forms
from .models import Menu, Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text','image']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'image']
        labels = {'text':'Restaurant:', 'image':'Thumbnail'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title']
        labels = {'title':'title'}


