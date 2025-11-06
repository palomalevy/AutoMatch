import { useState } from 'react'
import { Routes, Route, Link } from "react-router-dom";
import './App.css'
import Home from './HomePage/Home.jsx'

function App() {

  return (
    <Routes>
      <Route path="/home/:id" element={<Home />} />
    </Routes>
  )
}

export default App
