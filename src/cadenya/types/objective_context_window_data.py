# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ObjectiveContextWindowData"]


class ObjectiveContextWindowData(BaseModel):
    completion_tokens: Optional[int] = FieldInfo(alias="completionTokens", default=None)
    """
    A calculated value for how many completion tokens (output tokens) have been used
    in this context window
    """

    objective_id: Optional[str] = FieldInfo(alias="objectiveId", default=None)
    """The objective's ID that this window belongs to"""

    previous_window_continue_instructions: Optional[str] = FieldInfo(
        alias="previousWindowContinueInstructions", default=None
    )
    """
    The instructions for this window to continue from a previous window's chat
    history.
    """

    prompt_tokens: Optional[int] = FieldInfo(alias="promptTokens", default=None)
    """
    A calculated value for how many prompt tokens (input tokens) have been used in
    this context window
    """

    sequence: Optional[int] = None
    """sequence is a numeric representation of which context window this is.

    Sequences are useful to perform a max(sequence) on in order to calculate how
    many context windows an objective has.
    """
