#!/usr/bin/bash

_args=("$@") # all parameters from terminal.

p8(){
    isort ./fun/
    autopep8 -i -a -a -r -v ./fun/
}

init(){
    if [[ -x "$(which virtualenv)" ]]; then
        [[ -f "./venv/bin/activate" ]] || virtualenv venv
        source venv/bin/activate
    else
        echo "virtualenv doesn't exist, please install it" && exit 
    fi
    pip3 install -r requirements.txt.example
    [[ -f "$(which yarn)" ]] && yarn installn --cwd ./fun/funstatic

    [[ -d "./fun" ]] && mkdir ./fun
    [[ -f "./fun/funlog" ]] && touch ./fun/funlog

    python3 ./fun/manage.py migrate
    python3 ./fun/manage.py compilemessages
    [[ -d "./funfile/files" ]] || mkdir ./fun/funfile/files
    
    read -p "Create superuser?(y/N)" _createsuperuser
    [[ *"${_createsuperuser}"* = 'Yy' ]] && \
    python3 ./fun/manage.py createsuperuser

    [[ -f "fun/fun/settings.py" ]] || \
    cp fun/fun/settings_.py fun/fun/settings.py
    
    python3 ./fun/manage.py runserver
    echo "Done."
}

update_gitignore(){
    git rm -r --cached . && git add .
    read -p "commit now?(y/N)" commit_now
    [[ *"$commit_now"* = 'Yy' ]] && git commit -m 'update .gitignore'
    echo "gitignore updated!"
}

_start(){
    python3 ./fun/manage.py runserver
}

ug(){   update_gitignore;   }
_s(){   _start;             }

${_args[0]}