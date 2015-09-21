TODO
==================

Adicionar os dias a q isto se refere os dias a q foi feito o pedido
E faze-lo periodicamente

========
Mount a webserver where this runs

==
- Install:

as root
rm /usr/bin/python
ln -s /usr/bin/python3.4 /usr/bin/python

apt-get update
apt-get install python3.4-dev
apt-get install python-pip
apt-get install git



as www
git clone https://github.com/i1caro/hotel.git


monitor
celery -A periodic.tasks worker --loglevel=info --beat
monitor
python runner.py
