import dspy
from steplist_ai_features.signatures.step_generator import StepGeneratorSignature


class StepGeneratorPredict(dspy.Module):

    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict(StepGeneratorSignature)

    def forward(self, list_title: str, description: str) -> dspy.Prediction:
        return self.predictor(list_title=list_title, description=description)
