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
        <ul>
            <li><a href="/about">About us</a></li>
            <li><a href="/tables">Datos generales</a></li>
            <li><a href="/values">Valores</a></li>
            <li><a href="/about">About us</a></li>
        </ul>
    </header>
);

export default Header;