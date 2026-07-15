import { create } from "zustand";
import { api } from "../services/api";
import type { Project } from "../types/Project";

interface ProjectStore{
    projects:Project[];
    addProject:()=>Promise<void>;
}

export const useProjectStore=create<ProjectStore>((set,get)=>({

    projects:[],

    addProject:async()=>{

        const response=await api.post("/projects",{

            name:`Project ${get().projects.length+1}`,
            client:"Demo Client",
            location:"Hyderabad",
            resolution:"1920x1080"

        });

        set(state=>({

            projects:[
                ...state.projects,
                response.data
            ]

        }));

    }

}));
