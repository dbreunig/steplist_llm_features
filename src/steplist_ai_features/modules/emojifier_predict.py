import dspy
from steplist_ai_features.signatures.emojifier import EmojifierSignature


class EmojifierPredict(dspy.Module):

    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict(EmojifierSignature)

    def forward(self, title: str) -> dspy.Prediction:
        return self.predictor(title=title)
