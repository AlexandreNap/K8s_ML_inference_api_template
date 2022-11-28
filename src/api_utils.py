

class Model:
    def __init__(self, model):
        self.model = model

    def preprocess(self, input):
        # preprocessing
        return input

    def predict(self, input):
        input = self.preprocessing(input)
        y = self.model(input)  # or y = self.model.predict(input)
        return y


def log_data(input, prediction):
    # log input and prediction in a database, s3 storage etc...
    pass
