import type { Project } from "../../types/Project";

interface Props {
    project: Project;
}

export default function ProjectCard({project}:Props){

    return(

        <div className="project-card">

            <div className="thumb"/>

            <h3>{project.name}</h3>

            <p>{project.client}</p>

            <small>{project.resolution}</small>

        </div>

    )

}