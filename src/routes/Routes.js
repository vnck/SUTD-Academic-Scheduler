import React from "react";
import { Switch, Route } from "react-router-dom";
import App from "../App";
import Error from "../components/Error";

const Routes = () => (
  <main>
    <Switch>
      <Route exact path="/" component={App} />
      <Route exact path="/error" component={Error} />
    </Switch>
  </main>
);

export default Routes;
