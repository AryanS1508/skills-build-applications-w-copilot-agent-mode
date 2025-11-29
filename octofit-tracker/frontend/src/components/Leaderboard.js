import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboards, setLeaderboards] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboards/`
    : '/api/leaderboards/';

  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Fetched leaderboards:', results);
      })
      .catch(err => console.error('Error fetching leaderboards:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboards.map((entry, idx) => (
          <li key={entry.id || idx}>{entry.team} - {entry.points} points</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
