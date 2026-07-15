import { useDropzone } from "react-dropzone";

export default function SceneUploader() {

    const onDrop = (acceptedFiles: File[]) => {

        console.log("Dropped:", acceptedFiles);

    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        multiple: false,
        accept: {
            "image/*": [".png", ".jpg", ".jpeg", ".webp"]
        }
    });

    return (

        <div
            {...getRootProps()}
            style={{
                border: "2px dashed #4A7DFF",
                borderRadius: "12px",
                padding: "60px",
                textAlign: "center",
                cursor: "pointer",
                marginTop: "20px"
            }}
        >

            <input {...getInputProps()} />

            {isDragActive
                ? <h2>Drop image here...</h2>
                : <h2>Drag & Drop Render Here<br/>or Click to Browse</h2>
            }

        </div>

    );

}
