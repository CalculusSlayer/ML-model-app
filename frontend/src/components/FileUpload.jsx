import { useState } from 'react';

function FileUpload({onFileUpload}) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} accept=".csv" />
      <button onClick={() => onFileUpload(selectedFile)}>Upload</button>
    </div>
  );
}

export default FileUpload;
