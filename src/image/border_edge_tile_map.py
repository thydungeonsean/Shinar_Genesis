from src.image.border_image import BorderImage


class BorderEdgeTileMap(object):

    def __init__(self, dominion):

        self.dominion = dominion
        self.generated = {}

    def load_border_image(self, img_code, color):

        if img_code not in self.generated:
            self.generated[img_code] = BorderImage(img_code)

        img = self.generated[img_code]
        img.recolor(color)

        return img
