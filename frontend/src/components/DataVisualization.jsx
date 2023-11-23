import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

function DataVisualization(props) {
    console.log("props", props);

  if (!props.data) return <p>Loading...</p>;

  // Rest of the component
  // Prepare data for the first chart
const yTestYpredData = {
    labels: Array.from({ length: props.data.Y_test.length }, (_, i) => i + 1),
    datasets: [
      {
        label: 'Y_test',
        data: props.data.Y_test,
        borderColor: 'red',
        backgroundColor: 'rgba(255, 0, 0, 0.5)',
      },
      {
        label: 'Y_pred',
        data: props.data.Y_pred,
        borderColor: 'blue',
        backgroundColor: 'rgba(0, 0, 255, 0.5)',
      }
    ],
  };
  
  // Prepare data for the second chart
  const lossData = {
    labels: Array.from({ length: props.data['train loss'].length }, (_, i) => i + 1),
    datasets: [
      {
        label: 'Train Loss',
        data: props.data['train loss'],
        borderColor: 'green',
        backgroundColor: 'rgba(0, 255, 0, 0.5)',
      },
      {
        label: 'Validation Loss',
        data: props.data['validation loss'],
        borderColor: 'orange',
        backgroundColor: 'rgba(255, 165, 0, 0.5)',
      }
    ],
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <h2>Y_test vs Y_pred</h2>
      <div style={{ width: '1200px', height: '600px' }}>
        <Line data={yTestYpredData} />
      </div>
  
      <h2>Training and Validation Loss</h2>
      <div style={{ width: '1000px', height: '500px' }}>
        <Line data={lossData} />
      </div>
  
      <p>MSE: {props.data.mse}</p>
    </div>
  );
  
  
  
  
}

export default DataVisualization;
