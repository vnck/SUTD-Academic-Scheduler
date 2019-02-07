import React from "react";
import { Switch, Route } from "react-router-dom";
import AppliedRoute from "../components/AppliedRoute";
import PrivateRoute from "../components/PrivateRoute";
import Error from "../components/Error";
import Login from "../components/Login";
import CoordinatorHome from "../components/CoordinatorHome";
import InstructorHome from "../components/InstructorHome";
import HomeRedirect from "../components/HomeRedirect";

const Routes = ({ childProps }) => (
  <main>
    <Switch>
      <AppliedRoute
        exact
        path="/"
        component={HomeRedirect}
        props={childProps}
      />
      <AppliedRoute exact path="/login" component={Login} props={childProps} />
      <PrivateRoute
        exact
        path="/coordinator-home"
        component={CoordinatorHome}
        props={childProps}
        auth={childProps.isAuthenticated && childProps.isCoordinator}
      />
      <PrivateRoute
        exact
        path="/instructor-home"
        component={InstructorHome}
        props={childProps}
        auth={childProps.isAuthenticated && !childProps.isCoordinator}
      />
      <Route component={Error} />
    </Switch>
  </main>
);

export default Routes;
