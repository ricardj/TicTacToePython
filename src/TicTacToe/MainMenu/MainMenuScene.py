from ApplicationEngine.SceneManager import Scene


class MainMenuScene(Scene):
    def render(self) -> str:
        result ='''
 _______ _        _               _             
|__   __(_)      | |             | |            
   | |   _  ___  | |_ __ _  ___  | |_ ___   ___ 
   | |  | |/ __| | __/ _` |/ __| | __/ _ \ / _ \\
   | |  | | (__  | || (_| | (__  | || (_) |  __/
   |_|  |_|\___|  \__\__,_|\___|  \__\___/ \___|'''
        return result

    def update(self):
        input("Press enter")
        self.change_scene()