from dataclasses import dataclass


@dataclass
class SocialLinks:
    """Social media links."""

    github: str
    linkedin: str
    twitter: str


@dataclass
class TeamMember:
    """Team member's information."""

    name: str
    role: str
    avatar: str
    bio: str
    social_links: SocialLinks
