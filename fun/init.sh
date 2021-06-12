
#  check virtualenv

virtualenv_path=$(which virtualenv)
if [ -x "$virtualenv_path" ]; then
    virtualenv venv 
else
    echo "virtualenv doesn't exist, please install it"
    exit 
fi

source venv/bin/activate

pip3 install -r requirements.txt.example

python3 manage.py makemigrations
python3 manage.py makemigrations funhome
python3 manage.py makemigrations eduhub
python3 manage.py makemigrations funuser
python3 manage.py makemigrations funfile

python3 manage.py migrate

python3 manage.py collectstatic

python3 manage.py compilemessages

echo "create superuser. . ."
python3 manage.py createsuperuser

echo "copy .env.yaml.example to .env.yaml. . ."

echo "try runserver. . ."
python3 manage.py runserver

echo "Done."