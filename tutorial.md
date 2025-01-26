# Instalacja i przygotowanie środowiska
1. Instalacja pyenv (do zarzadzania wersjami pythona):
    ```brew update && brew install pyenv```
2. Instalacja Pythona:
    ```pyenv versions``` by sprawdzic wersje juz zainstalowane.
    ```pyenv install -l``` by sprawdzic dostepne wersje
    ```pyenv install 3.13.1``` instalacja wybranej wersji
    ```pyenv global 3.13.1``` ustawienie wersji globalnej
    polecenie ```pyenv exec``` wykonuje komendy pythona
3. Instalacja pipx (sluzy do instalacji bibliotek w wirtualnym srodowisku)
    ```brew install pipx```
    ```brew ensurepath```
    Restart terminala
4. Instalacja Poetry (dependency manager):
    Przejdz do folderu z projektem i uruchom:
    ```pipx install poetry```
    ```poetry new nazwa_folderu```
5. Otwórz folder nazwa_folderu w Visual Studio Code i uruchom w terminalu (cmd + j):
    ```poetry shell```
    cmd + shift + p - by otworzyc paletę i wybrac interpreter pythona uwtorzony dla projektu.
6. Do pliku pyproject.toml, ponziej python = "^3.13" dodaj:
    ```django = "^5.0.1"```
7. W terminalu:
    ```poetry install```
# Uruchomienie i stworzenie projektu Django
1. Usun folder z nazwa projektu, a nastepnie uruchom:
    ```poetry run django-admin startproject nazwa_projektu .```
    ```poetry run python manage.py migrate``` migruje baze danych
    ```poetry run python manage.py createsuperuser``` tworzy superusera
    ```poetry run python manage.py runserver``` uruchamia serwer
    Strona jest dostepna pod adresem  'localhost:8000/admin'
2. Stworz aplikacje django (o nazwie np app):
    ```poetry run python manage.py startapp app```
3. W pliku app/views stworz metode 'home' z widokiem.
4. W pliku app/urls.py wpisujesz sciezki (urlpatterns).
5. W pliku djangocourse/urls.py dopisz:
    ```from django.urls import path, include
        urlpatterns = [
            path('', include('app.urls')),
            path('admin/', admin.site.urls),
        ]
    ```
    Sciezki z obu plikow urls.y sa sklejane.
6. W pliku djangocourse/settings.py do sekcji INSTALLED_APPS dopisz 'app.apps.AppConfig'.
# Tworzenie modeli
1. W pliku app/models.py stwórz modele do bazy danych
2. W pliku app/admin.py zarejestruj modele
3. W pliku djangocourse/settings.py zaznacz, ze aplikacja ma uzywac UserProfile a nie AbstractUser.
    `AUTH_USER_MODEL = 'app.UserProfile'`
4. Przeprowadź migracje bazy danych w terminalu:
    `poetry run python manage.py makemigrations`
    `poetry run python manage.py migrate`
W przypadku bledu nalezy usunac plik db.sqlite3 i jeszcze raz przeprowadzic migracje.
Aby w VSC przegladac pliki db zainstaluj rozszerzenie `sqlite viewer`.
5. Stworz na nowo superusera:
    `poetry run python manage.py createsuperuser`
Po uruchomieniu serwera i zalogowaniu sie do panelu admina (localhost:8000/admin)
mozna dodawac artykuly.
# Wyswietlanie artykulow
1. W pliku app/views.py uzupelnij metode `home`.
2. Obok app i djangocourse stworz folder templates, a w nim app, gdzie utworz plik home.html (skrót: !+TAB).
3. W pliku djangocourse/settings.py uzupelnij wpis o lokalizacji plikow z szablonami.
    `'DIRS': [BASE_DIR / 'templates'],`
4. W szablonie uzywa sie {%%} i {{}}.

# Forms - Function Base
1. W katalogu app utworz plik forms.py.
2. W katalogu templates/app stworz plik html dla formularza (article_create.html).
3. W pliku app/views.py stworz widok dla formularza (create_article(request))
4. W pliku app/urls.py dodaj sciezke dla create_article. 

# Forms - Class Base
1. Nie potrzebny jest plik forms.py
2. W pliku app/views.py stworz klase o nazwie np CreateArticleView.
3. Stworz widok ArticleListView, ArticleUpdateView, ArticleDeleteView
4. Popraw urls.py

# Docker
1. Zainstaluj Docker desktop
2. Stworz plik Dockerfile i .dockerignore
3. Uruchom aplikacje Docker desktop
4. W terminalu VSC:
    `docker build -t djangocourse .`
    by zbudowac obraz.
5. Uruchomienie kontenera:
    `docker run -p 8005:8000 --name djangocourse  djangocourse`
    -p czyli port, 8005 to port na maszynie lokalnej, 8000 z kontenera.
    
6. W nowym oknie terminala uruchom:
    `docker exec djangocourse poetry run python manage.py migrate`
7. `docker rm nazwa_kontenera` kasuje kontener jesli pojawia sie blad
8. Aby uruchomic kontener polaczony z komputerem lokalnym:
    `docker run -dp 8005:8000 --name djangocourse -v "$(pwd):/code" djangocourse`
    flaga 'd' oznacza uruchomienie w trybie daemon.

# Dodanie Django Debug Toolbar
1. W terminalu:
    `poetry add -G dev django-debug-toolbar`
    -G tworzy nowa grupe w pliku pyproject.toml. Pozniej (in production) `poetry install --only main` sprawi, ze zainstalowane beda tylko zaleznosci spoza grupy dev.
2. W pliku djangocourse/settings.py pod MIDDLEWARE dodaj informacje o powyzszej wtyczce.
3. Kod:
    ```
    import socket 
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]+ ["127.0.0.1"]
    ```
    odpowiada za uzyskanie docker_ip by skozystac z Debug Toolbar przez Dockera.
    Jeśli INTERNAL_IPS jest inny niz '127.0.0.1' dopisz jeszcze:
    ```
    DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: print(request.META),
    }
    ``` sprawdz jaki ma byc ip i usun ten fragment bo Debug Toolbar nie pojawi sie.
4. Do pliku djangocourse/urls.py dodaj sciezke dla toolbara

# Automatyczne tworzenie superusera
1. Stworz custom migration przez terminal:
    `poetry  run python manage.py makemigrations --empty app`
2. W katalogu app/migrations pojawi sie nowy plik z migracja. Zmien jego nazwe na create_superuser.

# Logowanie
1. Dodaj pole 'creator' modelu Article w app/models.py
2. Dodaj walidacje w CreateArticleView w app/views.py
3. Zrob migracje:
    `poetry run python manage.py makemigrations`
    pojawi sie pytanie jak uzupelnic pole creator dla istniejacych artykulow (wybierz 1)
    `poetry run python manage.py migrate`
4. Dodaj `path('accounts/', include('django.contrib.auth.urls')),` do djangocourse/urls.py
5. Stworz szablony dla rejestracji uzytkownikow (templates/registration)
6. W base.html zrob prosta nawigacje do strony logowania.
7. W pliku djangocourse/settings okresl LOGIN_REDIRECT_URL i LOGOUT_REDIRECT_URL

# Django allauth
1. W terminalu:
    `poetry add "django-allauth[socialaccount]"`
2. W pliku settings.py dodaj `AUTHENTICATION_BACKENDS` oraz allauth i allauth.account jako THIRD_PARTY_APPS. Do MIDDLEWARE dodaj `'allauth.account.middleware.AccountMiddleware'`. Zmien LOGOUT_REDIRECT_URL na account_login.
3. W pliku djangocourse/urls.py zamien sciezki logowania (django.contrib.auth.urls) na `allauth.urls` w path 'accounts'.
4. Zmien szablony. W base.html zamiast `url 'logout'` ma byc `url 'account_logout'` i `account_login` zamiast `login`.
5. Katalog Registration jest niepotrzebny. Mozna usunac.
6. Migrate:
    `poetry run python manage.py migrate`
7. Test z uzyciem dockera:
    `docker build -t djangocourse .`
    `docker run -dp 8000:8000 --name djangocourse -v "$(pwd):/code" djangocourse`

# Social Authentication
1. W settings.py dodaj allauth.socialaccount w THIRD_PARTY
2. W terminalu migruj (przyklad z aplikacja uruchomiona w dockerze):
    `docker exec djangocourse poetry run python manage.py migrate`
3. W Github stworz aplikacje OAuth 

# Email do logowania
1. W settings.py dodaj ustawienia allauth pod # allauth
2. Teraz do logowania trzeba bedzie podac email.

# Dostosowanie UserProfile admin panel.
1. W admin.py dodaj import UserAdmin i stworz nowa klase CustomUserAdmin.
# Lokalizacja
1. W pliku Dockerfile dopisz fragment pozwalajacy na instalacje gettext.
2. Dodaj katalog locale
3. W settings.py dodaj LANGUAGE_CODE dla kraju i sciezke do katalogu locale.
4. W pliku models.py dodaj import dla gettext_lazy oraz funkcje _() dla rzeczy ktore maja byc przetlumaczone. Dodaj class Meta (dla samej nazwy Article).
5. Zrob migracje (makemigrations i migrate).
6. `docker exec djangocourse poetry run python manage.py makemessages --locale=pl`
7. W katalogu locale powstanie plik, ktory trzeba uzupelnic tlumaczeniami.
8. `docker exec djangocourse poetry run python manage.py compilemessages`.

# Kastomizacja UserProfile aby username nie byl wymagany
1. Stworz plik app/managers.py
2. W models.py uzupelnij klase UserProfile.
3. Migruj (makemigrations, migrate), makemessages, dodaj tlumaczenia do local/django.po i compilemessages.

# Dynamiczne dane modelu w Dashbord.
1. W pliku models.py uzupelnij UserProfile o metody @property. Dekorator ten sprawia, ze `my_user.article_count` zwraca dynamicznie wyliczone dane.
2. models.Sum zwraca dictionary.
3. Dzieki @property nie trzeba robic migracji.
4. W pliku settings.py dodaj `'django.contrib.humanize',` do lisy aplikacji.
5. W pliku home.html dodaj paragraf z informacja o ilosci slow stworzonych przez usera. 'intcomma' z biblioteki 'humanize' dodaje przecinek w przypadku duzych liczb (1,000).
# Markdown
1. Do base.html dodaj script instalujace wtyczke easeMDE oraz block dla page_js.
2. Stworz katalog templates/app/layouts a w nim plik base_form.html.
3. W article_create.html i article_update.html zmien import na plik base_form.html.

# PostgreSQL
1. W terminalu:
    `poetry add psycopg`
    `poetry add dj-database-url` - aby django rozumialo postgresql url.
2. W settings.py zaimportuj dj-database-url i dodaj dodatkowe dane w DATABASES
3. stworz plik .env.docker.
### DockerCompose
1. Stworz plik docker-compose.yml
2. Dodaj plik start-django.sh aby uruchamiac migracje automatycznie.
    `chmod 755 /code/start-django.sh`
3. W terminalu:
    `docker compose up --build`
    W przypadku bledu usunac containery i images stare z Docker Desktop i sprobowac jeszcze raz.
4. Komendy uzyteczne docker-compose:
    `docker compose up --build` - uruchamia docker compose pobierajac na nowo image
    `docker compose up -d` - jak wyzej, ale w trybie daemon i korzystajac ze starego image
    `docker compose down -v` - usuniecie bazy danych i volumes
    `docker image ls` - wylistowanie nazw obrazow
    `docker compose up --build --force-recreate --no-deps -d nazwa_obrazu`
    `docker compose down` - zatrzymanie 

# Tailwind CSS
1. W terminalu:
    `nvm use 22`
    `npx tailwidncss init` - zostanie utworzony plik tailwind.config.js
2. Dodaj sciezke do pliku tailwind.config.js
3. Stworz plik static/input.css
4. W terminalu:
    `npx tailwindcss -i ./static/input.css -o ./static/output.css --watch`
5. W pliku base.html dodaj load static i link do pliku output.css.
6. W pliku settings.py dodaj STATICFILES_DIRS
7. Uruchom aplikacje:
    `docker compose up`
8. `npm install -D tailwindcss`, `npm install -D @tailwindcss/forms @tailwindcss/typography`

#  django-browser-reload
1. `poetry add -G dev  django-browser-reload`
2. W settings.py dodaj  django-browser-reload do thirdParty i Middleware.
3. Do djangocourse/urls.py dodaj __reload__ path.
4. `docker compose up --build`

# django-widgets_tweaks
1. Aby modyfikowac formularze django:
    `poetry add django-widget-tweaks`
2. Do settings dodaj widget_tweaks do ThirdParty.
3. Aby dodac rozszerzenie do tailwind css nalezy zmodyfikowac plik tailwind.config.js

# AlpineJS
1. Ze strony Alpine JS skopiuj link instalujacy i wklej w pliku templates/base.html.
2. W przypadku x-bind uzywa sie pojedynczego znaku : tylko jesli element html nie pochodzi z django-widgets_tweaks. W przypadku elementow django-widgets_tweaks nalezy uzyc ::

# Flash Messaging
1. AllAuth emituje wiadomosci dostepne w szablonach jako 'messages'. Aby je wyswietlic dodaj div w base.html.
2. Aby wyswietlac message z wlasnej aplikacji nalezy w pliku app/views.py dodaj SuccessMessageMixin i w klasie ustaw np. success_message = 'Article deleted successfully'.
3. Aby moc wystylizowac message nalezy zamiast SuccessMessageMixin, nadpisac metode post().

# Pagination
1. In app/views.py in ArticleListView dodaj paginate_by.
2. W templates/app/home.html dodaj paginacje.

# Text search
1. W djangocourse/settings.py dodaj django.contrib.postgres w DJANGO_APPS.
2. W app.views.py dodaj search w ArticleListView w nadpisanej metodzie get_queryset.
3. W home.html dodaj formularz z wyszukiwaniem

# HTMX
1. W pliku templates/base.html dodaj 
`<script src="https://unpkg.com/htmx.org@2.0.3"></script>`

# Deploying
1. W settings.py dokonaj 6 zmian
2. W .env.docker ustaw DEBUG na True i SECRET_KEY
3. W djangocourse/urls.py zrob 2 zmiany.
4. `poetry add gunicorn "whitenoise[brotli]"`
5. W start-django.sh dokonaj zmian pozwalajacych na uruchomienie gunicorn
6. Dodaj whitenoise middleware w settings.py i 'whitenoise.runserver_nostatic' w Third Party apps
7. W settings.py dodaj lokalizacje dla plikow statycznych
8. komenda `poetry run python manage.py collectstatic` utworzy folder staticfiles. Dodaj tę komende w start-django.sh
