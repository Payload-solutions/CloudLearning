import React from 'react';
import '../assets/styles/components/Header.scss'

// Presentational components, not logic
// only presentation in html

const Header = () => (
    <header className="header">
        <img className="header__img" src="../assets/images/deeplearning_icon.png" alt="neuron network icon" />
        <div className="header__menu">
            <div className="header__menu--profile">
                <img src="" alt="" />
                <p>Profile</p>
            </div>
            <ul>
                <li><a href="">Account</a></li>
                <li><a href="">Logout</a></li>
            </ul>
        </div>
    </header>
);

export default Header;