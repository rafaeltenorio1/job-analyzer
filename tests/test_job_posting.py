import pytest

from job_analyzer.domain.job_posting import JobPosting


def test_key_combines_source_and_external_id() -> None:
    posting = JobPosting(
        source="lever",
        external_id="abc123",
        title="Software Enginner",
        description="Docker and Python",
    )

    assert posting.key == ("lever", "abc123")


def test_empty_title_is_rejected() -> None:
    with pytest.raises(ValueError):
        JobPosting(source="lever", external_id="abc123", title="", description="Docker and Python")


def test_empty_description_is_rejected() -> None:
    with pytest.raises(ValueError):
        JobPosting(source="lever", external_id="abc123", title="Data Enginner", description="")
