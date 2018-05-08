

class Listener(object):

    def __init__(self, key_code, on_press=None, on_release=None):

        self.key_code = key_code

        def default():
            pass

        if on_press is None:
            self.on_press = default
        else:
            self.on_press = on_press

        if on_release is None:
            self.on_release = default
        else:
            self.on_release = on_release

    def check_key_down(self, key_code):

        if key_code == self.key_code:
            self.on_press()

    def check_key_up(self, key_code):

        if key_code == self.key_code:
            self.on_release()
