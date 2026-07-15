export interface CameraPreset {
    id: string;
    name: string;
    icon: string;
    duration: number;
    description: string;
}

export const cameraPresets: CameraPreset[] = [
    {
        id:"push-in",
        name:"Push In",
        icon:"MoveRight",
        duration:5,
        description:"Smooth forward cinematic movement"
    },
    {
        id:"push-out",
        name:"Push Out",
        icon:"MoveLeft",
        duration:5,
        description:"Smooth backward cinematic movement"
    },
    {
        id:"orbit-left",
        name:"Orbit Left",
        icon:"RotateCcw",
        duration:6,
        description:"Orbit around the room to the left"
    },
    {
        id:"orbit-right",
        name:"Orbit Right",
        icon:"RotateCw",
        duration:6,
        description:"Orbit around the room to the right"
    },
    {
        id:"dolly-in",
        name:"Dolly In",
        icon:"ArrowRight",
        duration:5,
        description:"Professional dolly shot"
    },
    {
        id:"dolly-out",
        name:"Dolly Out",
        icon:"ArrowLeft",
        duration:5,
        description:"Reverse dolly movement"
    },
    {
        id:"tilt-up",
        name:"Tilt Up",
        icon:"ArrowUp",
        duration:4,
        description:"Tilt camera upward"
    },
    {
        id:"tilt-down",
        name:"Tilt Down",
        icon:"ArrowDown",
        duration:4,
        description:"Tilt camera downward"
    },
    {
        id:"crane-up",
        name:"Crane Up",
        icon:"MoveUp",
        duration:6,
        description:"Vertical crane movement"
    },
    {
        id:"crane-down",
        name:"Crane Down",
        icon:"MoveDown",
        duration:6,
        description:"Descending crane movement"
    },
    {
        id:"walkthrough",
        name:"Walkthrough",
        icon:"ScanEye",
        duration:8,
        description:"Natural interior walkthrough"
    },
    {
        id:"handheld",
        name:"Handheld",
        icon:"Camera",
        duration:5,
        description:"Realistic handheld motion"
    }
];
