import DataFetcher from './components/DataFetcher';
import FileUpload from './components/FileUpload';

function App() {
  return (
    <>
      <h1 style={{textAlign: 'center'}}>ECS 171 Group 25 Project</h1>
      <h3 style={{textAlign: 'center'}}>By Nayeel, Dhilan, Roger, Kyle, Jaasan</h3>
      <div style={{paddingLeft: '20px', paddingBottom: '10px'}}>
        <DataFetcher url="http://localhost:8000/"/>
      </div>
      <div style={{paddingLeft: '20px', paddingBottom: '10px'}}>
        <FileUpload />
      </div>
    </>
  );
}

export default App;
