#!/usr/bin/bash

git_push(){
    echo 'push to git@gitee.com:larryw3i/fun.git'
    git push git@gitee.com:larryw3i/fun.git

    echo 'push to git@github.com:larryw3i/fun.git'
    git push git@github.com:larryw3i/fun.git
}

uwsgi_start(){
    if [[ ! -f "uwsgi.ini" ]]
    then
        cp uwsgi.ini.example uwsgi.ini
    fi
    uwsgi --ini uwsgi.ini
}

uwsgi_stop(){
    sudo kill -9 $(cat uwsgi/uwsgi.pid)
}

uwsgi_restart(){
    uwsgi_stop; uwsgi_start
}

nohup(){
    nohup uwsgi_start > nohup.out
}

init(){

    echo "cd "$(dirname "$0")". . ."
    cd "$(dirname "$0")"
    echo "set pdfjs_version"
    pdfjs_version="2.8.335"
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
    manage.py migrate
    echo "python3 manage.py compilemessages. . ."
    python3 manage.py compilemessages
    echo "mkdir funfile/files. . ."
    mkdir funfile/files
    echo "python3 manage.py createsuperuser. . ."
    python3 manage.py createsuperuser
    echo "cd ./funstatic. . ."
    cd ./funstatic
    download_unzip_pdfjs(){
        wget "https://github.com/mozilla/pdf.js/releases/download/\
    v${pdfjs_version}/pdfjs-${pdfjs_version}-dist.zip"
        unzip_path=$(which unzip)
        if [ -x "$unzip_path" ]; then
            echo "unzip pdfjs-${pdfjs_version}-dist.zip -d pdf.js"
            unzip pdfjs-${pdfjs_version}-dist.zip -d pdf.js
            rm pdfjs-${pdfjs_version}-dist.zip
        else
            echo "unzip doesn't exist, please install it"
            exit 
        fi
    }
    read -r -p "Download mozilla's pdf.js and unzip it? [y/N] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
    then
        download_unzip_pdfjs
    else
        echo "You can download mozilla's pdf.js on the \
https://mozilla.github.io/pdf.js/getting_started/ and unzip it to \
fun/funstatic/pdf.js/"
    fi
    yarn_path=$(which yarn)
    if [ -x "$yarn_path" ]; then
        echo "yarn install. . ."
        yarn install
    else
        echo "yarn doesn't exist, please install it"
        exit 
    fi
    echo "cd .."; cd ..
    echo "python3 manage.py runserver. . ."
    python3 manage.py runserver
    echo "mkdir uwsgi. . ."; mkdir uwsgi
    echo "Done."
}

update_gitignore(){
    git rm -r --cached .
    git add .
    read -p "commit now?(y/N)" commit_now
    if [ "$commit_now" = 'y' ] || [ "$commit_now" = 'Y' ]; then
        git commit -m 'update .gitignore'
    fi
    echo "gitignore updated!"
}

$1
