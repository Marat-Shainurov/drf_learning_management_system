
python3 -m venv venv
source venv/bin/activata
pip3 install -r requirements.txt
python4 manage.py migrate
python3 manage.py collectstatic --input
deactivate