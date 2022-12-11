class Observable(object):
    def __init__(self):
        self.callbacks = []

    def add_listener(self, callback):
        self.callbacks.append(callback)

    def raise_event(self):
        e = Event()
        e.source = self
        # for k, v in attrs.iteritems():
        #     setattr(e, k, v)
        for fn in self.callbacks:
            fn()


class Event(Observable):


    pass


class Button:
    on_button_fired = Event()

    def button_pressed(self):
        self.on_button_fired.raise_event()


if __name__ == '__main__':
    start_button = Button()
    start_button.on_button_fired.add_listener(lambda: print("Button pressed"))
    start_button.on_button_fired.add_listener(lambda: print("Button pressed again i guess"))
    start_button.button_pressed()
