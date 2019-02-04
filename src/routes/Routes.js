import React from "react";
import { Switch, Route } from "react-router-dom";
import AppliedRoute from "../components/AppliedRoute";
import PrivateRoute from "../components/PrivateRoute";
import Error from "../components/Error";
import Login from "../components/Login";
import CoordinatorHome from "../components/CoordinatorHome";

const Routes = ({ childProps }) => (
  <main>
    <Switch>
      <AppliedRoute exact path="/login" component={Login} props={childProps} />
      <PrivateRoute
        exact
        path="/"
        component={CoordinatorHome}
        props={childProps}
        auth={childProps.isAuthenticated}
      />
      <Route component={Error} />
    </Switch>
  </main>
);

export default Routes;
