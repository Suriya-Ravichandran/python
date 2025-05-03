import random
from .color import Color
class DogFacePrinter:
    def __init__(self):
        self.dog_faces = [
            fr"""{Color.RED}
             /^ ^\
            / 0 0 \
            V\ Y /V
             / - \
            |    \
            || (__)
            {Color.RESET}
            """,
            fr"""{Color.GREEN}
             __
          o-''|\_____/)
           \_/|_)     )
              \  __  /
              (_/ (_/
            {Color.RESET}
            """,
            fr"""{Color.BLUE}
              / \__
             (    @\___
             /         O
            /   (_____/
           /_____/ U
            {Color.RESET}
            """,
            r"""
              __     _
        o'')}____//
         `_/      )
         (_(_/-(_/
            """
        ]

    def print_random_face(self):
        return(random.choice(self.dog_faces))

    # def print_all_faces(self):
    #     for face in self.dog_faces:
    #         print(face)
    #         print("=" * 40)  # Separator line
