import React, { useState, useEffect } from 'react';
import Dashboard from './pages/Dashboard';
import { io } from 'socket.io-client';

function App() {
  const [socket, setSocket] = useState(null);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const newSocket = io(process.env.REACT_APP_API_URL || 'http://localhost:5000');
    
    newSocket.on('connect', () => {
      console.log('Connected to AI Ecosystem');
      setConnected(true);
    });

    newSocket.on('disconnect', () => {
      console.log('Disconnected from AI Ecosystem');
      setConnected(false);
    });

    setSocket(newSocket);

    return () => newSocket.close();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      <Dashboard socket={socket} connected={connected} />
    </div>
  );
}

export default App;
