# keywall

### Environment
You can use vagrant to lunch a server, or just run
 `sh ./vagrant/bootstrap.sh` on Ubuntu 18.4 to initial environment.
 
### How to run keywall
please run the following command on your vm to setup the environment.
```bash
ln -s /vagrant keywall
cd keywall

mkvirtualenv env --python=/usr/bin/python3
workon env
pip install -r requirement.txt
pipenv sync
python ./setup.py
```

after all above commands are been done, run the following command to execute keywall
```bash
python ./keywall.py --enable-save
```

alos, to see more options.
```bash
python ./keywall.py -h
```

### Open source packages
- atoma ( RSS parser https://github.com/NicolasLM/atoma )
- beautifulsoup4 ( html/xml parser )
- html5lib ( html5 library for html parsing )
- nltk ( tokenize https://www.nltk.org/ )
- pyyaml ( yaml config parser )
- requests ( HTTP request handler )
