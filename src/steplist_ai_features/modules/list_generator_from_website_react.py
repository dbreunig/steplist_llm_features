import dspy
from steplist_ai_features.signatures.list_generator_from_website import ListGeneratorFromWebsiteSignature
from steplist_ai_features.utils.web_search import read_webpage

class ListGeneratorFromWebsiteReAct(dspy.Module):

    def __init__(self, tools=None):
        super().__init__()
        self.predictor = dspy.ReAct(ListGeneratorFromWebsiteSignature, tools=tools or [read_webpage])

    def forward(self, url: str) -> dspy.Prediction:
        return self.predictor(url=url)
