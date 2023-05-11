class Question:
    def __init__(self, position, title, text, image, possibleAnswers):
        self.text = text
        self.title = title
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers