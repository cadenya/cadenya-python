# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubjectAssertionParam"]


class SubjectAssertionParam(TypedDict, total=False):
    """
    SubjectAssertion identifies a person within a tenant in the customer's own
     namespace — typically their user id. Asserting a subject upserts the
     subject record under the asserted tenant and associates the created
     resource with it. A subject assertion is only valid alongside a tenant
     assertion: subject identifiers are scoped to their tenant.
    """

    id: Required[str]
    """The subject identifier in the customer's namespace (e.g.

    their user id). Stored as the subject record's external_id; unique within the
    tenant.
    """

    name: str
    """Optional human-readable name for the subject.

    Updates the subject record's name on every assertion that provides it.
    """
