from dataclasses import dataclass


@dataclass
class TeamMember:
    """Team member's information."""

    name: str
    role: str
    avatar: str
    bio: str
