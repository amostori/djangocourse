1. Przejdz do folderu z projektem i uruchom:
    ```poetry new nazwa_folderu```
2. Otwórz folder nazwa_folderu w Visual Studio Code i uruchom w terminalu (cmd + j):
    ```poetry shell```
    cmd + shift + p - by otworzyc paletę i wybrac interpreter pythona uwtorzony dla projektu.
3. Do pliku pyproject.toml, ponziej python = "^3.13" dodaj:
    ```django = "^5.0.1"```
4. W terminalu:
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
3. W pliku djangocourse/settings.py do sekcji INSTALLED_APPS dopisz 'app.apps.AppConfig'.
4. W pliku app/models.py stworz klase Post - model artykulu.
5. `poetry run python manage.py makemigrations`
6. `poetry run python manage.py migrate`
7. W pliku app/admin.py zarejestruj klase Post aby mozna ja bylo przegladac po zalogowaniu do panelu admina.

# Tworzenie widokow
1. W pliku app/views.py stwórz def post_list dla widoku listy postów oraz post_detail dla pojedyńczego artykułu.
2. Stwórz plik app/urls.py i dodaj do niego urlpatterns.
3. Aby połączyć wzorce url z głównymi wzorcami zedytuj plik ratol/urls.py
4. W settings.py wskaż folder dla templates w TEMPLATES ('DIRS': [BASE_DIR / 'templates']), oraz ustaw STATICFILES_DIRS
5. Stwórz szablony widoków w templates: base.html, list.html i detail.html.