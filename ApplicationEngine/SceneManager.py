from ApplicationEngine.UpdateManager import UpdateManager, Updateable
from ApplicationEngine.RenderManager import RenderManager, Renderable
from Observer.Observer import Observable, Event


class Scene(Renderable, Updateable, Observable):

    on_change_scene = Event()

    def initialize(self):
        pass

    def render(self) -> str:
        return "Hello world"
        pass

    def update(selfs):
        input("Waiting for key input...")

    def change_scene(self):
        self.on_change_scene.raise_event()



class SceneManager:
    render_manager = RenderManager()
    input_manager = UpdateManager()
    current_scene: Scene = None

    def __init__(self):
        pass

    pass

    def set_current_scene(self, main_menu_scene):
        self.current_scene = main_menu_scene
        self.current_scene.initialize()
        pass

    def update(self):
        if self.current_scene is not None:
            self.render_manager.render_target(self.current_scene)
            self.input_manager.update_input(self.current_scene)
        pass
