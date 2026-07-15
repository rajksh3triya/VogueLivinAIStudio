from copy import deepcopy

class WorkflowInjector:

    @staticmethod
    def inject(workflow: dict, values: dict):

        wf = deepcopy(workflow)

        # Placeholder:
        # Next step will locate nodes dynamically and
        # inject prompts, image paths and output names.

        return wf
