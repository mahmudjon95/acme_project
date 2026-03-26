# Добавьте новые строчки с импортами классов.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import include, path, reverse_lazy

urlpatterns = [
    # Подключаем urls.py приложения для работы с пользователями.
    path('', include('django.contrib.auth.urls')),
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
]
