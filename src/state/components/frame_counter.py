

class FrameCounter(object):

    def __init__(self, flip):

        self.frame = 0
        self.flip = flip

    def run(self):

        self.frame += 1
        if self.frame >= self.flip:
            self.frame = 0
