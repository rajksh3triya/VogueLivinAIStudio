import type { CameraPreset } from "../../data/cameraPresets";

interface Props{
    preset:CameraPreset;
}

export default function CameraPresetCard({preset}:Props){

    return(

        <div className="camera-card">

            <div style={{fontSize:"40px"}}>
                {preset.icon}
            </div>

            <h3>{preset.name}</h3>

            <p>{preset.description}</p>

            <small>{preset.duration}s</small>

        </div>

    );

}
