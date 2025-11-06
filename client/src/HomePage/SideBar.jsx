import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';
import '../Design/SideBar.css'

const SideBar = () => {
  const { id } =  useParams();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/users/${id}/`)
      .then(res => res.json())
      .then(data => setUser(data))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <section className="sidebar">Loading…</section>;

  const activePrefs = Object.entries(user.preferences)
    .filter(([_, value]) => value === 1)
    .map(([k]) => (<li key={k}>{k}</li>))

  return (
    <section className="sidebar">
      <h2>User Profile</h2>
      <p>Name: {user.name}</p>
      <p>User ID: {user.id}</p>
      <h3>User Prefs</h3>
      <ul>
        {activePrefs.map(pref => (
          <li key={pref}>{pref}</li>
        ))}
      </ul>
      <button className="cosSim">Cosine Similarity</button>
      car brand, condition
      <button className="pearson">Pearson Correlation</button>
      Precio/budget, distancia, mileage
    </section>
  )
}

export default SideBar
