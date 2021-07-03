
echo "cd "$(dirname "$0")". . ."
cd "$(dirname "$0")"

echo "check virtualenv. . ."
virtualenv_path=$(which virtualenv)
if [ -x "$virtualenv_path" ]; then
    echo "virtualenv venv. . ."
    virtualenv venv 
else
    echo "virtualenv doesn't exist, please install it"
    exit 
fi

echo "source venv/bin/activate. . ."
source venv/bin/activate

echo "pip3 install -r requirements.txt.example. . ."
pip3 install -r requirements.txt.example

echo "cp .env.yaml.example to .env.yaml. . ."
cp .env.yaml.example .env.yaml

echo "python3 manage.py migrate. . ."
python3 manage.py migrate

# echo "python3 manage.py collectstatic. . ."
# python3 manage.py collectstatic

echo "python3 manage.py compilemessages. . ."
python3 manage.py compilemessages

echo "mkdir funfile/files. . ."
mkdir funfile/files

echo "python3 manage.py createsuperuser. . ."
python3 manage.py createsuperuser

echo "cd ./funstatic. . ."
cd ./funstatic

echo "git clone https://github.com/mozilla/pdf.js.git. . ."
git clone https://github.com/mozilla/pdf.js.git

yarn_path=$(which yarn)
if [ -x "$yarn_path" ]; then
    echo "yarn upgrade. . ."
    yarn upgrade
else
    echo "yarn doesn't exist, please install it"
    exit 
fi

echo "cd .."
cd ..

echo "python3 manage.py runserver. . ."
python3 manage.py runserver

echo "Done."
