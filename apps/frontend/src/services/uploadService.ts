import { api } from "./api";

export async function uploadScene(projectId: string, file: File) {

    const formData = new FormData();

    formData.append("project_id", projectId);
    formData.append("file", file);

    const response = await api.post(
        "/scenes/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}
