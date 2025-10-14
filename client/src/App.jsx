import { useState } from 'react'
import { Routes, Route, Link } from "react-router-dom";
import './App.css'
import Home from './HomePage/Home.jsx'
import Login from './LoginPage/Login.jsx'

function App() {

  return (
    <Routes>
      <Route path="/home" element={<Home />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  )
}

export default App
