"""Signature definitions for emojifier."""

import dspy

class EmojifierSignature(dspy.Signature):
    """
    """

    title: str = dspy.InputField(desc="")
    emoji: str = dspy.OutputField(desc="")
