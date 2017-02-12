import React from 'react'
import ReactDOM from 'react-dom'
import Layout from './components/Layout'
import HelloWorld from './components/HelloWorld'
import Login from './components/Auth.js'
import store from './store'

import { Router, Route, IndexRoute, browserHistory } from 'react-router'
import { Provider } from 'react-redux'

const router = (
    <Provider store={store}>
        <Router history={browserHistory}>
            <Route path="/" component={Layout}>
                <IndexRoute component={HelloWorld} />
                <Route path="/login" component={Login} />
            </Route>
        </Router>
    </Provider>
);


const render = () => { ReactDOM.render(router, document.getElementById("app")); }

render();

store.subscribe(render);
