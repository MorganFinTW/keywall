# keywall

### setup environment
You can use vagrant to lunch a server, or just run
 `sh ./vagrant/bootstrap.sh` on Ubuntu 18.4 to initial environment.
 
### how to execute this program
please run the following command on your vm 
```bash
ln -s /vagrant keywall
cd keywall

mkvirtualenv env --python=/usr/bin/python3
workon env
pip install -r requirement.txt
```