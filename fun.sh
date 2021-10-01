#!/usr/bin/bash

_args=("$@") # all parameters from terminal.

init(){
    if [[ -x "$(which virtualenv)" ]]; then
        [[ -f "./venv/bin/activate" ]] || virtualenv venv
        source venv/bin/activate
    else
        echo "virtualenv doesn't exist, please install it" && exit 
    fi
    pip3 install -r requirements.txt.example
    [[ -f "$(which yarn)" ]] && cd fun/funstatic && yarn install
    cd ..
    cp ./.env.example.yaml ./.env.yaml
    python3 manage.py migrate
    python3 manage.py compilemessages
    [[ -d "./funfile/files" ]] || mkdir ./funfile/files
    python3 manage.py createsuperuser
    python3 manage.py runserver
    echo "Done."
}

update_gitignore(){
    git rm -r --cached . && git add .
    read -p "commit now?(y/N)" commit_now
    [[ *"$commit_now"* = 'Yy' ]] && git commit -m 'update .gitignore'
    echo "gitignore updated!"
}

_start(){
    python3 manage.py runserver
}

ug(){   update_gitignore;   }
_s(){   _start;             }

$1