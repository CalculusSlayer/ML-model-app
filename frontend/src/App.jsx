import './App.css';
import DataFetcher from './components/DataFetcher';
import UserForm from './components/UserForm';

function App() {
  return (
    <>
      <h1>HI</h1>
      <DataFetcher url="http://localhost:8000/" />
      <UserForm>Fill this out</UserForm>
    </>
  );
}

export default App;
