import React from 'react';
import '../assets/styles/components/Header.scss'
import logo from '../assets/static/otherlogo.png'
// Presentational components, not logic
// only presentation in html

const Header = () => (
    <header className="header">
        <img className="header__img" src={logo} alt="neuron network icon" />
        <div className="header__menu">
            <div className="header__menu--profile">
                <img src="" alt="" />
                <a href="/about">About us</a>
            </div>
        </div>
    </header>
);

export default Header;