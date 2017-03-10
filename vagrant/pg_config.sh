apt-get -qqy update
apt-get -qqy install postgresql
apt-get purge -y python-pip
wget https://bootstrap.pypa.io/get-pip.py
python ./get-pip.py
pip install flask
pip install sqlalchemy
pip install psycopg2
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
pip install redis
pip install passlib
pip install itsdangerous
pip install flask-httpauth
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb forum'
su vagrant -c 'psql forum -f /vagrant/forum/forum.sql'

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd
