if self.startbutton.draw(self.screen):
                game = Game(self.button_list)
                self.highscore = game.run()
                # self.highscore_surf = self.textfont.render(
                #   f"High Score: {self.highscore}", False, "black"
                # )
                # self.highscore_rect = self.highscore_surf.get_rect(center=(640, 300))

            if self.profilebutton.draw(self.screen):
                print("profile")