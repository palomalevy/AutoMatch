import React from 'react'
import '../Design/FeaturedItem.css'

const FeaturedItem = () => {
  return (
    <section className="featuredContainer">
        <h2>Featured Listing</h2>
        <section className="featuredItem">
            <img src="https://static.vecteezy.com/system/resources/thumbnails/053/733/179/small_2x/every-detail-of-a-sleek-modern-car-captured-in-close-up-photo.jpg" width={500}/>
            <div className="itemDetails">
                <h3>2015 Honda Accord</h3>
                <p>Mileage: 45,000 miles</p>
                <p>Price: $15,000</p>
                <p>Location: San Francisco, CA</p>
                <button className="viewButton">View Details</button>
            </div>
        </section>
    </section>
  )
}

export default FeaturedItem
