from ApplicationEngine.UpdateManager import UpdateManager
from ApplicationEngine.SceneManager import SceneManager
from TicTacToe.Gameplay.GameplayScene import GameplayScene
from TicTacToe.MainMenu.MainMenuScene import MainMenuScene


class ApplicationManager:
    scene_manager = SceneManager()
    input_manager = UpdateManager()

    main_menu_scene = MainMenuScene()
    gameplay_scene = GameplayScene()

    def __init__(self):

        pass

    def run(self):
        self.main_menu_scene.on_change_scene.add_listener(
            lambda: self.scene_manager.set_current_scene(self.gameplay_scene))
        self.gameplay_scene.on_change_scene.add_listener(
            lambda: self.scene_manager.set_current_scene(self.main_menu_scene))

        self.scene_manager.set_current_scene(self.main_menu_scene)

        while True:
            self.scene_manager.update()
        pass
