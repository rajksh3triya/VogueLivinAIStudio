import "../styles/projects.css";
import ProjectToolbar from "../components/project/ProjectToolbar";
import ProjectSearch from "../components/project/ProjectSearch";
import ProjectList from "../components/project/ProjectList";

export default function Projects() {
    return (
        <div className="projects-page">

            <h1>Projects</h1>

            <ProjectToolbar />

            <ProjectSearch />

            <ProjectList />

        </div>
    );
}
