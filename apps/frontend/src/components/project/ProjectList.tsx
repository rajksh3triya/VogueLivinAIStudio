import ProjectCard from "./ProjectCard";
import { useProjectStore } from "../../stores/projectStore";

export default function ProjectList() {

    const { projects } = useProjectStore();

    return (
        <div className="project-grid">
            {projects.map(project => (
                <ProjectCard
                    key={project.id}
                    project={project}
                />
            ))}
        </div>
    );
}
