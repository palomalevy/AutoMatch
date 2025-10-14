import React from 'react'
import '../Design/Feed.css'

const Feed = () => {
  return (
    <section className="feedContainer">
        <h2>Recommended For You</h2>
        <section className="feedItems">
            <div className="itemObject">
                <img src="https://toppng.com/uploads/preview/techno-disney-cars-movie-disney-pixar-disney-wiki-disney-cars-11562993425a7t2mebpym.png" width={200}/>
                <div className="itemDetails">
                    <h3>2018 Toyota Camry</h3>
                    <p>Mileage: 30,000 miles</p>
                    <p>Price: $18,000</p>
                    <p>Location: Los Angeles, CA</p>
                    <button className="viewButton">View Details</button>
                </div>
            </div>
            
            <div className="itemObject">
                <img src="https://www.vhv.rs/dpng/d/526-5262969_clipart-cars-plan-disney-cars-movie-characters-hd.png" width={200}/>
                <div className="itemDetails">
                    <h3>2017 Ford Mustang</h3>
                    <p>Mileage: 25,000 miles</p>
                    <p>Price: $25,000</p>
                    <p>Location: New York, NY</p>
                    <button className="viewButton">View Details</button>
                </div>
            </div>
            
            <div className="itemObject">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoBLBU3Z0T5lgkWnXAS2cqBrvjuRdaW7rsBQ&s" width={200}/>
                <div className="itemDetails">
                    <h3>2016 BMW 3 Series</h3>
                    <p>Mileage: 40,000 miles</p>
                    <p>Price: $22,000</p>
                    <p>Location: Chicago, IL</p>
                    <button className="viewButton">View Details</button>
                </div>
            </div>
            
        </section>
    </section>
  )
}

export default Feed
