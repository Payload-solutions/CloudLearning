import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../containers/Home';
import Values from '../containers/Values';
import About from '../components/About';
import Layout from '../components/Layout';
import Tables from '../containers/Tables';
import Upload from '../containers/Upload';

const App = () => (
    <BrowserRouter>
        <Layout>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/values" component={Values} />
                <Route exact path="/about" component={About} />
                <Route exact path="/tables" component={Tables}/>
                <Route exact path="/upload" component={Upload} />
            </Switch>
        </Layout>
    </BrowserRouter>
);

export default App;