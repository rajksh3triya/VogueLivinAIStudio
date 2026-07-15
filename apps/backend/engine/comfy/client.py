import requests

class ComfyClient:

    def __init__(self, host="127.0.0.1", port=8188):
        self.base_url = f"http://{host}:{port}"

    def health(self):
        try:
            r = requests.get(f"{self.base_url}/system_stats", timeout=5)
            return {
                "online": r.status_code == 200,
                "status": r.status_code,
                "data": r.json() if r.status_code == 200 else {}
            }
        except Exception as e:
            return {
                "online": False,
                "error": str(e)
            }

    def queue(self):
        return requests.get(f"{self.base_url}/queue").json()

    def history(self):
        return requests.get(f"{self.base_url}/history").json()

    def prompt(self, workflow):
        return requests.post(
            f"{self.base_url}/prompt",
            json={"prompt": workflow}
        ).json()
