import { useState } from 'react';

function FileUpload({onFileUpload}) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [selectedModel, setSelectedModel] = useState('dnn'); // default model

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleModelChange = (event) => {
    setSelectedModel(event.target.value);
  };

  return (
    <>
      <div>
        <input type="file" onChange={handleFileChange} accept=".csv" />
        <button onClick={() => onFileUpload(selectedFile, selectedModel)}>Upload and Run</button>
      </div>
      <div style={{paddingTop: '8px'}}>
        <select onChange={handleModelChange}>
          <option value="dnn">Dnn</option>
          <option value="ann">Ann</option>
          <option value="perceptron">Perceptron</option>
        </select>
      </div>
    </>
  );
}

export default FileUpload;

