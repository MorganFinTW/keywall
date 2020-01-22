keywall
=======

### Environment

You can use vagrant to lunch a server, or just run
`sh ./vagrant/bootstrap.sh` on Ubuntu 18.4 to initial environment.

### How to execute keywall

please run the following command on your vm

``` {.bash}
ln -s /vagrant keywall
cd keywall

mkvirtualenv env --python=/usr/bin/python3
workon env
pip install -r requirement.txt
pipenv sync
python ./keywall.py --enable-save
```

to see more options

``` {.bash}
python ./keywall.py -h
```

### open source packages

-   atoma ( RSS parser https://github.com/NicolasLM/atoma )
-   nltk ( tokenize https://www.nltk.org/ )
-   pyyaml ( yaml config parser )
-   requests ( HTTP request handler )

