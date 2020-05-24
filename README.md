# clicker
1. pip install virtualenv
2. python -m venv venv
3. .\venv\Scripts\Activate
4. pip install -r requirements.txt
5. celery -A tasks purge
6. celery -A tasks worker -l info -P gevent
7. import tasks
8. tasks.clicker.delay()
9. python main.py

d - off/on simulation<br>
q - quite