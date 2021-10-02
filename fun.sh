#!/usr/bin/bash

_args=("$@") # all parameters from terminal.

p8(){
    isort ./fun/
    autopep8 -i -a -a -r -v ./fun/
}

activate_source(){
    if [[ -x "$(which virtualenv)" ]]; then
        [[ -f "./venv/bin/activate" ]] || virtualenv venv
        source ./venv/bin/activate
    else
        echo "virtualenv doesn't exist, please install it" && exit 
        exit
    fi
}

init(){
    activate_source
    pip3 install -r requirements.txt
    [[ -x "$(which yarn)" ]] && cd ./fun/funstatic && yarn install && cd ../..

    [[ -d "./fun/funlog" ]] || mkdir ./fun/funlog
    [[ -f "./fun/funlog/django_fun.log" ]] || touch ./fun/funlog/django_fun.log

    [[ -d "./funfile/files" ]] || mkdir -p ./fun/funfile/files
    
    [[ -f "./fun/fun/settings.py" ]] || \
    cp ./fun/fun/settings_.py ./fun/fun/settings.py
    
    python3 ./fun/manage.py makemigrations
    python3 ./fun/manage.py migrate
    
    python3 ./fun/manage.py compilemessages

    read -p "Create superuser?(y/N)" _createsuperuser
    [[ *"${_createsuperuser}"* == 'Yy' ]] && \
    python3 ./fun/manage.py createsuperuser

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
    activate_source
    python3 ./fun/manage.py runserver
}

ug(){   update_gitignore;   }
_s(){   _start;             }
gita(){ p8; git add . ;     }

${_args[0]}