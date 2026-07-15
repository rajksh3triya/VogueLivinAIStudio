class WorkflowValidator:

    REQUIRED_KEYS = [
        "nodes"
    ]

    @staticmethod
    def validate(workflow: dict):

        missing = []

        for key in WorkflowValidator.REQUIRED_KEYS:
            if key not in workflow:
                missing.append(key)

        return {
            "valid": len(missing) == 0,
            "missing": missing
        }
