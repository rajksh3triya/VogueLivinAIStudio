import type { Project } from "../types/Project";

const projects: Project[] = [];

export function getProjects(): Project[] {
    return projects;
}

export function createProject(project: Project) {
    projects.push(project);
}

export function deleteProject(id: string) {
    const index = projects.findIndex(p => p.id === id);

    if (index !== -1) {
        projects.splice(index,1);
    }
}