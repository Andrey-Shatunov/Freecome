import React from 'react'
import ReactDOM from 'react-dom'
import Layout from './components/Layout'
import HelloWorld from './components/HelloWorld'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'
import { Provider } from 'react-redux'
import store from './store'

const router = (
    <Provider store={ store }>
        <Router history={ browserHistory }>
            <Route path="/" component={ Layout }>
                <IndexRoute component={ HelloWorld } />
            </Route>
        </Router>
    </Provider>
);


var render = () => { ReactDOM.render(router, document.getElementById("app")); }

render();

store.subscribe(render);
