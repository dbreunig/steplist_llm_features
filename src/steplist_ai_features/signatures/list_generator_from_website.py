"""Signature definitions for list_generator_from_website."""

import dspy

class ListGeneratorFromWebsiteSignature(dspy.Signature):
    """
    Given a website URL, generate a checklist of steps to complete the task or routine described on the webpage. The steps written should be clear, brief, detailed, and actionable. The entire list should be something the user can complete in one sitting, maybe two or three. Try not to add steps that could be entire lists unto themselves.
    """

    url: str = dspy.InputField(desc="The website URL")
    list_title: str = dspy.OutputField(desc="A recognizeable title for the checklist")
    description: str = dspy.OutputField(desc="A brief description of the checklist, including the source.")
    steps: list[str] = dspy.OutputField(desc="The steps to be completed to finish the task.")
