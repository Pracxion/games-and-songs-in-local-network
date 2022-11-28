import React from 'react';
import ReactDOM from 'react-dom/client';
import Router from './Router';
import './index.scss';

const rootElement = document.getElementById('root');
if (!rootElement) throw new Error('Failed to find the root element');
const root = ReactDOM.createRoot(rootElement);
root.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);

