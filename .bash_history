cd /webapps/hello_django/
virtualenv .
ls
source bin/activate
pip install django
django-admin.py startproject hello
cd hello
python manage.py runserver pi47.student.utwente.nl:8005
sudo chown -R hello:users /webapps/hello_django
logout
source bin/activate
pip install gunicorn
gunicorn hello.wsgi:application --bind example.com:8001
gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8001
gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
ls
cd hello/
ls
gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
cd ..
hello/gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
/hello/gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
./hello/gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
~/hello/gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
cd bin/
nano
cd ..
ls
bin/gunicorn_start 
cd /hello/ gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
ls
cd /hello gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
cd hello/ gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
gunicorn hello.wsgi:application --bind pi47.student.utwente.nl:8007
logout
ls
bin/gunicorn_start
cd bin/
ls
gunicorn_start
nano gunicorn_start 
bin/gunicorn_start
logout
