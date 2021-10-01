#!/usr/bin/bash

_args=("$@") # all parameters from terminal.
pdfjs_version="2.8.335"

uwsgi_start(){
    [[ ! -f "./fun/uwsgi.ini" ]] && cp ./fun/uwsgi.ini.example ./fun/uwsgi.ini
    uwsgi --ini ./fun/uwsgi.ini
}

uwsgi_stop(){
    sudo kill -9 $(cat ./fun/uwsgi/uwsgi.pid)
}

uwsgi_restart(){
    uwsgi_stop; uwsgi_start
}

nohup(){
    nohup . fun.sh uwsgi_start > nohup.out
}

get_pdfjs(){
    cd ./fun/funstatic
    read -r -p "Download mozilla's pdf.js and unzip it? [y/N] " _get_pdfjs_
    if [[ "Yy" == *"${_get_pdfjs_}"* ]]; then
        wget "https://github.com/mozilla/pdf.js/releases/download/"\
        "v${pdfjs_version}/pdfjs-${pdfjs_version}-dist.zip"
        if [[ -x "$(which unzip)" ]]; then
            unzip pdfjs-${pdfjs_version}-dist.zip -d pdf.js
            rm pdfjs-${pdfjs_version}-dist.zip
        else
            echo "unzip doesn't exist, please install it" && exit 
        fi
    else
        echo "You can download mozilla's pdf.js on the "\
        "https://mozilla.github.io/pdf.js/getting_started/ and unzip it to "\
        "fun/funstatic/pdf.js/"
    fi

    if [[ -f "$(which yarn)" ]]; then
        yarn install
    else
        echo "yarn doesn't exist, please install it" && exit 
    fi
    cd ..
}

init(){
    if [[ -x "$(which virtualenv)" ]]; then
        [[ -f "./venv/bin/activate" ]] || virtualenv venv
        source venv/bin/activate
    else
        echo "virtualenv doesn't exist, please install it" && exit 
    fi
    pip3 install -r requirements.txt.example
    cp .env.yaml.example .env.yaml
    manage.py migrate
    python3 manage.py compilemessages
    mkdir ./fun/funfile/files
    python3 manage.py createsuperuser
    get_pdfjs
    mkdir uwsgi
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