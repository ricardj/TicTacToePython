import os


class Renderable:
    def render(self) -> str:
        return "Hello world"


class RenderManager:
    def render_target(self, renderable: Renderable):
        self.clear()
        print(renderable.render())
        pass

    def clear(self):  # this function will clear the console
        command = 'cls'  # cls is for windows
        if os.name != 'nt':  # if it isnt windows it will use clear
            command = 'clear'
        os.system(command)
        return 0