class Jumper:
    """Makes our jumper guy!"""

    def __init__(self) -> None:
        self._lines_to_draw = [
            " ___ ",
            "/___\\",
            "\\   /",
            " \\ /",
            "  0 ",
            " /|\\",
            " / \\"]
        self.is_dead=False

    def __str__(self) -> str:
        results = ''
        for line in self._lines_to_draw:
            results += line + '\n'

        return results

    def break_chute(self):
        """Cuts away one line of the chute, until it hits the head which will set him to dead"""
        if len(self._lines_to_draw) >3:
            self._lines_to_draw.pop(0)
        else:
            self._lines_to_draw[-1].replace('0','X')
            self.is_dead=True