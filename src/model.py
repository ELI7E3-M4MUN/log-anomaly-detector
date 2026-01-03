import pickle

class ModelLoader:
    def load(self, path):
        with open(path, "rb") as f:
            return pickle.load(f)
