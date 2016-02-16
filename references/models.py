from citations import models as cit_models


class TextEdition(cit_models.Reference):
    pass

    def __str__(self):
        name = ''
        if self.author:
            name = self.author
        elif self.editor:
            name = self.editor

        name += ', {0}'.format(self.title[:18])
        return name
