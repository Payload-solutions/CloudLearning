import React from 'react';
import '../assets/styles/components/Footer.scss';
import githubIcon from '../assets/static/github.png';
import twitterIcon from '../assets/static/twitter.png'

const Footer = () => (
  <footer className="footer">
    <a href="https://github.com/Arturo0911"><img src={githubIcon} /></a>
    <a href="https://twitter.com/DevTuron"><img src={twitterIcon}  alt="" /></a>
  </footer>
);

export default Footer;