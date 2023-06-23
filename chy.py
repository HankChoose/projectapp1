# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('entry/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    # ...
]


# views.py
from django.shortcuts import render, redirect
from .models import Entry

def edit_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)

    if request.method == 'POST':
        # 处理表单提交
        entry.content = request.POST['content']
        entry.save()
        return redirect('entry_detail', entry_id=entry.id)

    return render(request, 'edit_entry.html', {'entry': entry})


<!-- edit_entry.html -->
<form method="post" action="{% url 'edit_entry' entry.id %}">
    {% csrf_token %}
    <textarea name="content">{{ entry.content }}</textarea>
    <button type="submit">保存</button>
</form>


<!-- entry_detail.html -->
<a href="{% url 'edit_entry' entry.id %}">编辑</a>

