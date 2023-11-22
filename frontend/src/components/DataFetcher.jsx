// DataFetcher.jsx
// Example component that makes GET
// request to API server to retrive
// information

import { useEffect, useState } from 'react';

function DataFetcher({ url }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, [url]); // Dependency array with URL ensures effect runs when URL changes

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <p>Data fetched:</p>
      <pre>{JSON.stringify(data, null, 2)}</pre>
      {/* <p>data[message] = {data.message}</p> */}
    </div>
  );
}

export default DataFetcher;
