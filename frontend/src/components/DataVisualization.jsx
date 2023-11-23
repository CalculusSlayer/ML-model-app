import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

function DataVisualization(props) {
    console.log("props", props);

  if (!props.data) return <p>Loading...</p>;

  const commonOptions = {
    plugins: {
      tooltip: {
        callbacks: {
          title: function(tooltipItems) {
            // Return the label for the x-axis
            return `Day: ${tooltipItems[0].label}`;
          },
          label: function(tooltipItem) {
            // Return the label for the y-axis
            let label = tooltipItem.dataset.label || '';
            if (label) {
              label += ': ';
            }
            label += tooltipItem.parsed.y;
            return label;
          }
        }
      },
    }
  };
  
  // Rest of the component
  // Prepare data for the first chart
const yTestYpredData = {
    labels: Array.from({ length: props.data.Y_test.length }, (_, i) => i + 1),
    datasets: [
      {
        label: 'Actual close value',
        data: props.data.Y_test,
        borderColor: 'red',
        backgroundColor: 'rgba(255, 0, 0, 0.5)',
      },
      {
        label: 'Predicted close value',
        data: props.data.Y_pred,
        borderColor: 'blue',
        backgroundColor: 'rgba(0, 0, 255, 0.5)',
      }
    ],
  };

  const yTestYpredOptions = {
    ...commonOptions,
    scales: {
      x: {
        title: {
          display: true,
          text: 'Day'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Close Value (INR)'
        }
      }
    }
  };  
  
  // Prepare data for the second chart
  const lossData = {
    labels: Array.from({ length: props.data['train loss'].length }, (_, i) => i + 1),
    datasets: [
      {
        label: 'Training Loss',
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

  const lossOptions = {
    ...commonOptions,
    scales: {
      x: {
        title: {
          display: true,
          text: 'Epoch'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Loss'
        }
      }
    }
  };  

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <h2>Actual close value vs. Predicted close value</h2>
      <div style={{ width: '1200px', height: '600px' }}>
        <Line data={yTestYpredData} options={yTestYpredOptions}/>
      </div>
  
      <h2>Training Loss vs. Validation Loss</h2>
      <div style={{ width: '1000px', height: '500px' }}>
        <Line data={lossData} options={lossOptions}/>
      </div>
  
      <p><strong>MSE: </strong><em>{props.data.mse ? props.data.mse.toFixed(4) : 'N/A'}</em></p>

    </div>
  );  
}

export default DataVisualization;
