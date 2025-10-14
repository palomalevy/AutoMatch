import React from 'react'
import SideBar from './SideBar'
import '../Design/Home.css'
import FeaturedItem from './FeaturedItem'
import Feed from './Feed'

const Home = () => {
  return (
    <section className="homeContainer">
      <h1>AutoMatch</h1>
      <section className="homePage">
        <SideBar />
        <div className="divider">
            <FeaturedItem />
            <Feed />
        </div>
      </section>
    </section>
  )
}

export default Home
