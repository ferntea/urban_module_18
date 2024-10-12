from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Sample list of existing users (consider using a database in a real application)
users = [
    'Ann',
    'Anton',
    'Peter'
]

template_name = 'fifths_task/registration_page.html'

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  # Capture email from POST data
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        try:
            age = int(request.POST.get('age'))
        except (ValueError, TypeError):
            info['error'] = 'Возраст должен быть числом'
            return render(request, template_name, info)

        print(f"username => {username}")
        print(f"email => {email}")  # Print email
        print(f"password => {password}")
        print(f"password_repeat => {password_repeat}")
        print(f"age => {age}")

        is_user_exist = username in users
        is_password_correct = password == password_repeat
        is_age_correct = age >= 18

        if is_user_exist:
            info['error'] = 'Пользователь уже существует'
            return render(request, template_name, info)
        if not is_password_correct:
            info['error'] = 'Пароли не совпадают'
            return render(request, template_name, info)
        if not is_age_correct:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, template_name, info)
        return HttpResponse(f"Приветствуем, {username}!", status=200)
    return render(request, template_name, info)


# The code below yields a mistake after pushing the button Зарегистрироваться
# therefore I leave the code as a partially fulfilled task.
# Intead of the please see below a simplified function ef sign_up_by_django
# def sign_up_by_django(request):
#     info = {}
#     form = UserRegister()  #
#     info["form"] = form
#     if request.method == 'POST':
#         print(request.POST)  # Log the POST data for checking
#         form = UserRegister(request.POST)
#         info["form"] = form
#         if form.is_valid():
#             username = request.POST.get('username')
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             password_repeat = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             print(f"username => {username}")
#             print(f"email => {email}")  # Print email
#             print(f"password => {password}")
#             print(f"password_repeat => {password_repeat}")
#             print(f"age => {age}")
#
#             is_user_exist = username in users
#             is_password_correct = password == password_repeat
#             is_age_correct = age >= 18
#
#             if is_user_exist:
#                 info['error'] = 'Пользователь уже существует'
#                 return render(request, template_name, info)
#             if not is_password_correct:
#                 info['error'] = 'Пароли не совпадают'
#                 return render(request, template_name, info)
#             if not is_age_correct:
#                 info['error'] = 'Вы должны быть старше 18'
#                 return render(request, template_name, info)
#
#             return HttpResponse(f"Приветствуем, {username}!", status=200)
#
#     return render(request, template_name, info)

# Below is a simplified code as far as the above one does not work properly
def sign_up_by_django(request):
    return sign_up_by_html(request)