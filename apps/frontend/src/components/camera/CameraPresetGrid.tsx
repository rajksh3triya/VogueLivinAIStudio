import { cameraPresets } from "../../data/cameraPresets";
import CameraPresetCard from "./CameraPresetCard";

export default function CameraPresetGrid(){

    return(

        <div
            style={{
                display:"grid",
                gridTemplateColumns:"repeat(auto-fill,minmax(250px,1fr))",
                gap:"20px",
                marginTop:"25px"
            }}
        >

            {cameraPresets.map(preset=>(

                <CameraPresetCard
                    key={preset.id}
                    preset={preset}
                />

            ))}

        </div>

    );

}
