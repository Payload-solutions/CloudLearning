import React from 'react';
import '../assets/styles/components/Header.scss'
import logo from '../assets/static/otherlogo.png'
import menu from '../assets/static/menu.png'
// Presentational components, not logic
// only presentation in html

const Header = () => (

    <nav className="navbar navbar-expand-lg navbar bg">
        <div className="container-fluid">
            <img className="header__img" src={logo} alt="neuron network icon" />
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                <img src={menu} alt="" />
            </button>
            <div className="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/values">Estadísticas</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/tables">Tabla de contenido</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/about">Nosotros</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

);

export default Header;