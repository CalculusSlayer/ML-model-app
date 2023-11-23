// import DataFetcher from './components/DataFetcher';
import FileUpload from './components/FileUpload';
import DataVisualization from './components/DataVisualization';

import { useState, useEffect } from 'react';

function App() {
  const [modelData, setModelData] = useState(null);

  // TODO: might need below
  // const handleFileChange = (event) => {
  //   setSelectedFile(event.target.files[0]);
  // };

  const handleFileUpload = async (selectedFile) => {
    if (!selectedFile) {
      alert('Please select a file first!');
      return;   
    }

    alert('Uploading csv file and running DNN model')

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:8000/upload-csv', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const result = await response.json();
      setModelData(result);
      console.log(result);
      console.log("Result: ", result);

      alert('Model analysis complete!');
    } catch (error) {
      console.error('Upload error:', error);
      alert('Upload failed or another error!');
    }
  };

  useEffect(() => {
    console.log("ModelData:", modelData);
  }, [modelData]);

  return (
    <>
      <h1 style={{textAlign: 'center'}}>ECS 171 Group 25 Project</h1>
      <h3 style={{textAlign: 'center'}}>By Nayeel, Dhilan, Roger, Kyle, Jassan</h3>
      {/* <div style={{paddingLeft: '20px', paddingBottom: '10px'}}>
        <DataFetcher url="http://localhost:8000/"/>
      </div> */}
      <div style={{paddingLeft: '20px', paddingBottom: '10px'}}>
        <FileUpload onFileUpload={handleFileUpload}/>
        {modelData && <DataVisualization data={modelData} />}
      </div>

    </>
  );
}

export default App;
