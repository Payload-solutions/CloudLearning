import React from 'react';
import Header from '../components/Header';
import Search from '../components/Search';
import Footer from '../components/Footer'
// import Catgories from '../components/Categories';
// import Carousel from '../components/Carousel';
// import CarouselItem from '../components/CarouselItem';
// import Categories from '../components/Categories';
import '../assets/styles/App.scss';


const App = () => (
    <div className="App">
        <Header/>
        <Search/>
        {/* <Categories>
            <Carousel>
                <CarouselItem/>
                <CarouselItem/>
                <CarouselItem/>
                <CarouselItem/>
            </Carousel>
        </Categories> */}
        <Footer/>
    </div>
);

export default App;