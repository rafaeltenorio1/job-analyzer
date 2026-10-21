from dataclasses import dataclass


@dataclass(frozen=True)
class JobPosting:
    source: str
    external_id: str
    title: str
    description: str

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Title cannot be empty")
        if not self.description.strip():
            raise ValueError("Description cannot be empty")

    @property
    def key(self) -> tuple[str, str]:
        return (self.source, self.external_id)
