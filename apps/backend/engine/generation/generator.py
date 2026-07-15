from engine.prompts.builder import generate
from engine.workflows.loader import load_workflow
from engine.queue.manager import enqueue
from engine.generation.job import GenerationJob
from engine.generation.state import GenerationState

class GenerationEngine:

    def submit(
        self,
        project_id: str,
        scene_id: str,
        provider: str,
        workflow: str,
        camera: dict,
        scene: dict,
    ) -> GenerationJob:

        job = GenerationJob(
            id=f"{project_id}-{scene_id}",
            project_id=project_id,
            scene_id=scene_id,
            provider=provider,
            workflow=workflow,
            camera=camera["id"],
        )

        job.state = GenerationState.VALIDATING

        prompt = generate(provider, scene, camera)

        job.state = GenerationState.LOADING_WORKFLOW

        workflow_json = load_workflow(workflow)

        job.state = GenerationState.QUEUED

        enqueue(job)

        return job
