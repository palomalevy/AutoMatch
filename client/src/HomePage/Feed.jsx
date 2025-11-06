import React, { useState, useEffect } from 'react'
import '../Design/Feed.css'
import getBrandLogo from '../Utils/GetBrandLogo.jsx';

const API_BASE = "http://127.0.0.1:8000";
const PAGE_SIZE = 12;

const Feed = () => {
    const [cars, setCars] = useState([]);
    const [page, setPage] = useState(1);
    const [loading, setLoading] = useState(false);
    const [hasMore, setHasMore] = useState(true);

    async function fetchPage(pageNum) {
        if (loading) return "Loading in progress";
        setLoading(true);

        try {
            const res = await fetch(`${API_BASE}/api/listings/?page=${pageNum}&pageSize=${PAGE_SIZE}`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();

            const newCars = Array.isArray(data.cars) ? data.cars : [];
            setCars(prev => (pageNum === 1 ? newCars : [...prev, ...newCars]));
            setHasMore(Boolean(data.hasMore));
            setPage(pageNum + 1);
        } catch (err) {}

        setLoading(false);
    }

    useEffect(() => {
        fetchPage(1);
    }, []);

  return (
    <section className="feedContainer">
        <h2>Recommended For You</h2>
        <section className="feedItems">
            {cars.map((car, index) => {
                const brand = car.manufacturer.toLowerCase();
                const year = Number(car.year);
                const price = `$${Number(car.price).toLocaleString()}`;

                return (
                    <div className="itemObject" key={car.id ?? `${brand}-${year}-${index}`}>
                    <img src={getBrandLogo(car.manufacturer)} alt="Image N/A" />
                    <div className="itemDetails">
                        <h3>{year} {brand[0].toUpperCase() + brand.slice(1)}</h3>
                        <p>Manufacturer: {brand}</p>
                        <p>Price: {price}</p>
                        <p>Year: {year}</p>
                        <button className="viewButton">View Details</button>
                    </div>
                    </div>
                );
            })}
        </section>

        <section className="paginationControls">
            <button className="loadMore" onClick={() => fetchPage(page)} disabled={loading || !hasMore}>
                {loading ? "Loading…" : hasMore ? "Load more" : "No more results"}
            </button>
        </section>
    </section>
  )
}

export default Feed;
