from .base import BaseProvider

class WANProvider(BaseProvider):

    def name(self):
        return "WAN"

    def workflow(self):
        return {
            "provider":"wan"
        }

    def build_prompt(self, scene, camera):

        return f"""
Generate a smooth cinematic walkthrough.

Movement:
{camera["name"]}

Keep every furniture object fixed.

Do not redesign the room.

Maintain lighting realism.

High quality motion.
"""
