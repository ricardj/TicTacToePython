class Updateable:
    def update(self):
        input("HEllo there")
        pass


class UpdateManager:
    def update_input(self, current_scene: Updateable):
        current_scene.update()
        pass
