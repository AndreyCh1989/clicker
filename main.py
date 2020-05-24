import time
import redis

from pynput.mouse import Button, Controller

SIMULATE_KEY = 'simulate_key'


def set_simulate(value):
    r = redis.Redis()
    r.set(SIMULATE_KEY, value)


def get_simulate():
    r = redis.Redis()
    return r.get(SIMULATE_KEY)


if __name__=='__main__':
    mouse = Controller()
    while True:
        if get_simulate() == b'1':
            mouse.click(Button.left, 1)
        time.sleep(0.1)

