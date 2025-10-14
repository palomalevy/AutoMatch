import React from 'react'
import '../Design/Login.css'
import { Link } from "react-router-dom";

const Login = () => {
  return (
        <section className="loginBox">
            <section className="loginPage">
                <h1>AutoMatch</h1>
                <section className="loginForm">
                    <form className="form">
                        <div className="loginContainer">
                            <div className="credentials">
                                <div className="usernameInput">
                                    <label className="identifier"><b>Email or username</b></label>
                                    <input type="text" placeholder="Email or username" name="identifier" required/>
                                </div>
                                <div className="passwordInput">
                                    <label className="password"><b>Password</b></label>
                                    <input type="password" placeholder="Password" name="password" required/>
                                </div>
                            </div>
                            {/* {error && <p style={{ color: 'red' }}>{error}</p>} */}
                            <button className="loginButton" type="submit"><Link to="/home">Login</Link></button>
                        </div>
                    </form> 
                </section>
                {/* <p>Don't have an account? <Link to="/signup" className="linkTo">Sign Up</Link></p> */}
            </section>
        </section>
    );
}

export default Login
