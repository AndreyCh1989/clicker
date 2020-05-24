from celery import Celery
import logging
import main
from pynput.keyboard import Listener as KeyListner, KeyCode

app = Celery('tasks', broker='redis://guest@localhost//')


@app.task
def clicker():
    logging.info('clicker started')
    main.set_simulate(0)

    def on_press(key):
        if key == KeyCode.from_char('d'):
            if main.get_simulate() == b'1':
                main.set_simulate(0)
                logging.info('simulation finished')
            else:
                main.set_simulate(1)
                logging.info('simulation started')
        if key == KeyCode.from_char('q'):
            return False

    with KeyListner(on_press=on_press) as key_listener:
        key_listener.join()

    logging.info('clicker finished')
