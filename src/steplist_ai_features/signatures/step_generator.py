"""Signature definitions for step_generator."""

import dspy
from typing import Optional

class StepGeneratorSignature(dspy.Signature):
    """
    Given a list_title and description, write a checklist of steps to complete the task or routine. The steps written should be clear, brief, detailed, and actionable. The entire list should be something the user can complete in one sitting, maybe two or three. Try not to add steps that could be entire lists unto themselves.
    """

    list_title: str = dspy.InputField(desc="The task title for the checklist")
    description: Optional[str] = dspy.InputField(desc="A brief description of the checklist")
    steps: list[str] = dspy.OutputField(desc="The steps to be completed to finish the task.")
