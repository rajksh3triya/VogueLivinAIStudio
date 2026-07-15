from .base import BaseProvider

class LTXProvider(BaseProvider):

    def name(self):
        return "LTX"

    def workflow(self):
        return {
            "provider":"ltx"
        }

    def build_prompt(self, scene, camera):

        return f"""
Create a cinematic interior walkthrough.

Camera Movement:
{camera["name"]}

Duration:
{camera["duration"]} seconds

Maintain room geometry.

No object deformation.

Natural camera movement.

Ultra realistic.
"""
