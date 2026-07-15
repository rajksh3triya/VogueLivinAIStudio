import { create } from "zustand";

export interface Scene {
    id: string;
    image?: string;
    filename?: string;
}

interface SceneStore {
    scenes: Scene[];
    addScene: (scene: Scene) => void;
    removeScene: (id: string) => void;
}

export const useSceneStore = create<SceneStore>((set) => ({
    scenes: [],

    addScene: (scene) =>
        set((state) => ({
            scenes: [...state.scenes, scene],
        })),

    removeScene: (id) =>
        set((state) => ({
            scenes: state.scenes.filter((s) => s.id !== id),
        })),
}));
