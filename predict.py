import replicate

class Predictor:
    def _init_(self):
        pass

    def predict(self, prompt: str) -> str:
        model = replicate.models.get("piyushp123/pikav2")
        version = model.versions.get("db21e426798682f56062d9275f0c9f3f3132fdbdfc42fc6e7a468ca8f82f48fe")
        output = version.predict(prompt=prompt)
        return output