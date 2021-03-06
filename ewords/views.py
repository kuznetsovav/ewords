from django.shortcuts import render
from .models import Quote
from .models import Video
from .models import UserProfile
from .models import Article
from .models import MapUserQuote
from .models import User
from .models import Audio
from django.forms import modelformset_factory
from django.utils import timezone
import datetime
from django.contrib.auth.forms import UserCreationForm
from ewords.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ewords.forms import QuoteForm
from django.shortcuts import redirect
from ewords.forms import AddtomeForm
from ewords.forms import VideoForm
from ewords.forms import ArticleForm
from ewords.forms import AudioForm
from django.shortcuts import render, get_object_or_404



def signup(request):

    # Логическое значение указывающее шаблону прошла ли регистрация успешно.
    # В начале ему присвоено значение False. Код изменяет значение на True, если регистрация прошла успешно.
    registered = False

    # Если это HTTP POST, мы заинтересованы в обработке данных формы.
    if request.method == 'POST':
        # Попытка извлечь необработанную информацию из формы.
        # Заметьте, что мы используем UserForm и UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Если в две формы введены правильные данные...
        if user_form.is_valid() and profile_form.is_valid():
            # Сохранение данных формы с информацией о пользователе в базу данных.
            user = user_form.save()

            # Теперь мы хэшируем пароль с помощью метода set_password.
            # После хэширования мы можем обновить объект "пользователь".
            user.set_password(user.password)
            user.save()

            # Теперь разберемся с экземпляром UserProfile.
            # Поскольку мы должны сами назначить атрибут пользователя, необходимо приравнять commit=False.
            # Это отложит сохранение модели, чтобы избежать проблем целостности.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Предоставил ли пользователь изображение для профиля?
            # Если да, необходимо извлечь его из формы и поместить в модель UserProfile.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Теперь мы сохраним экземпляр модели UserProfile.
            profile.save()

            # Обновляем нашу переменную, чтобы указать, что регистрация прошла успешно.
            registered = True

        # Неправильная формы или формы - ошибки или ещё какая-нибудь проблема?
        # Вывести проблемы в терминал.
        # Они будут также показаны пользователю.
        else:
            print (user_form.errors, profile_form.errors)

    # Не HTTP POST запрос, следователь мы выводим нашу форму, используя два экземпляра ModelForm.
    # Эти формы будут не заполненными и готовы к вводу данных от пользователя.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Выводим шаблон в зависимости от контекста.
    return render(request,
            'ewords/signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # Если запрос HTTP POST, пытаемся извлечь нужную информацию.
    if request.method == 'POST':
        # Получаем имя пользователя и пароль, вводимые пользователем.
        # Эта информация извлекается из формы входа в систему.
                # Мы используем request.POST.get('<имя переменной>') вместо request.POST['<имя переменной>'],
                # потому что request.POST.get('<имя переменной>') вернет None, если значения не существует,
                # тогда как request.POST['<variable>'] создаст исключение, связанное с отсутствем значения с таким ключом
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Используйте Django, чтобы проверить является ли правильным
        # сочетание имя пользователя/пароль - если да, то возвращается объект User.
        user = authenticate(username=username, password=password)

        # Если мы получили объект User, то данные верны.
        # Если получено None (так Python представляет отсутствие значения), то пользователь
        # с такими учетными данными не был найден.
        if user:
            # Аккаунт активен? Он может быть отключен.
            if user.is_active:
                # Если учетные данные верны и аккаунт активен, мы можем позволить пользователю войти в систему.
                # Мы возвращаем его обратно на главную страницу.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # Использовался не активный аккуант - запретить вход!
                return HttpResponse("Your Ewords account is disabled.")
        else:
            # Были введены неверные данные для входа. Из-за этого вход в систему не возможен.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # Запрос не HTTP POST, поэтому выводим форму для входа в систему.
    # В этом случае скорее всего использовался HTTP GET запрос.
    else:
        # Ни одна переменная контекста не передается в систему шаблонов, следовательно, используется
        # объект пустого словаря...
        return render(request, 'ewords/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Используйте декоратор login_required(), чтобы гарантировать, что только авторизированные пользователи смогут получить доступ к этому представлению.
@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)

    # Перенаправляем пользователя обратно на главную страницу.
    return HttpResponseRedirect('/')


def profile(request):
    return render(request, 'ewords/profile.html', {})

def profile(request):
    users = UserProfile.objects.all().filter(user=request.user)
    return render(request, 'ewords/profile.html', {'users': users})

def index(request):
    return render(request, 'ewords/index.html', {})

def index(request):
    quotes = Quote.objects.all().filter(incognito=False)
    return render(request, 'ewords/index.html', {'quotes': quotes})

def quotations(request):
    return render(request, 'ewords/quotations.html', {})

def quotations(request):
    quotes = Quote.objects.all().filter(author=request.user)
    return render(request, 'ewords/quotations.html', {'quotes': quotes})

def quotations_new(request):
        if request.method == "POST":
            form = QuoteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('ewords.views.quotations')
        else:
            form = QuoteForm()
        return render(request, 'ewords/quotations_new.html', {'form': form})

def quotations_addtome(request):
        if request.method == "POST":
            addtome_form = AddtomeForm(request.POST)
            if addtome_form.is_valid():
                post = addtome_form.save(commit=False)
                post.user = request.user
                post.quote = request.POST.get('quote_id')
                addtome_form.save
                return redirect('ewords.views.index')
        else:
            addtome_form = AddtomeForm()
        return render(request, 'ewords/index.html', {'addtome_form': addtome_form})


def video(request):
    return render(request, 'ewords/video.html', {})

def video(request):
    videos = Video.objects.all()
    return render(request, 'ewords/video.html', {'videos': videos})

def video_new(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ewords.views.video')
    else:
        form = VideoForm()
    return render(request, 'ewords/video_new.html', {'form': form})

def articles(request):
    return render(request, 'ewords/articles.html', {})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'ewords/articles.html', {'articles': articles})

def articles_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ewords.views.articles')
    else:
        form = ArticleForm()
    return render(request, 'ewords/articles_new.html', {'form': form})

def articles_detail(request, pk):
        article = get_object_or_404(Article, pk=pk)
        return render(request, 'ewords/articles_detail.html', {'article': article})

def audio(request):
    return render(request, 'ewords/audio.html', {})

def audio(request):
    audio = Audio.objects.all()
    return render(request, 'ewords/audio.html', {'audio': audio})

def audio_new(request):
    if request.method == "POST":
        form = AudioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ewords.views.audio')
    else:
        form = AudioForm()
    return render(request, 'ewords/audio_new.html', {'form': form})

def audio_detail(request, pk):
        audio = get_object_or_404(Audio, pk=pk)
        return render(request, 'ewords/audio_detail.html', {'audio': audio})




