import SceneToolbar from "../components/scene/SceneToolbar";
import SceneUploader from "../components/scene/SceneUploader";
import ScenePreview from "../components/scene/ScenePreview";

export default function Scenes() {

    return (

        <div>

            <h1>Scene Manager</h1>

            <SceneToolbar />

            <SceneUploader />

            <ScenePreview />

        </div>

    );

}
