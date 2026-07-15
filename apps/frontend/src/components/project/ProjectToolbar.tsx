import { useProjectStore } from "../../stores/projectStore";

export default function ProjectToolbar() {

    const addProject = useProjectStore(state => state.addProject);

    return (
        <div className="project-toolbar">

            <button
                className="primary-button"
                onClick={addProject}
            >
                + New Project
            </button>

        </div>
    );
}
