

class UI(object):

    def __init__(self, state):

        self.state = state

        self.elements = {}
        self.controllers = []

        self.new_element_adders = []
        self.to_be_removed = set()

        self.needs_update = True

    def run(self):

        if self.to_be_removed:
            self.clear_elements()

        if self.new_element_adders:
            for e in self.new_element_adders:
                e()
            del self.new_element_adders[:]

        for element in self.elements.itervalues():
            if element.parent is None:
                element.run()
        if self.needs_update:
            self.update_controllers()

    def draw(self, surface):

        for element in self.elements.itervalues():
            if element.parent is None:
                element.draw(surface)

    # membership methods
    def add_element(self, element):
        self.elements[element.element_id] = element

    def remove_element(self, element):
        element.strand_element()
        del self.elements[element.element_id]

    def queue_element(self, func):
        self.new_element_adders.append(func)

    def dequeue_element_by_key(self, key):
        if key in self.elements:
            el = self.elements[key]
            self.to_be_removed.add(el)

    def remove_element_by_key(self, el_id):
        element = self.get_element(el_id)
        element.strand_element()
        del self.elements[el_id]

    def get_element(self, key):
        return self.elements.get(key, None)

    def add_controller(self, controller):
        self.controllers.append(controller)

    def clear_elements(self):
        for e in self.to_be_removed:
            self.remove_element(e)
        self.to_be_removed.clear()

    # handle clicking ui elements
    def click(self, pos):

        self.click_ui_elements(pos)

    def click_ui_elements(self, pos):

        for element in self.elements.itervalues():
            if element.parent is None:
                element.click(pos)

    def right_click(self, pos):

        self.right_click_ui_elements(pos)

    def right_click_ui_elements(self, pos):

        for element in self.elements.itervalues():
            if element.parent is None:
                element.click(pos)

    def request_update(self):
        self.needs_update = True

    def update_controllers(self):

        for controller in self.controllers:
            controller.update()

        self.needs_update = False
