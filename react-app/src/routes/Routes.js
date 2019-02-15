import React from "react";
import { Switch, Route } from "react-router-dom";
import AppliedRoute from "./AppliedRoute";
import PrivateRoute from "./PrivateRoute";
import Error from "../components/Pages/Error";
import Login from "../components/Pages/Login";
import CoordinatorHome from "../components/Pages/CoordinatorHome";
import InstructorHome from "../components/Pages/InstructorHome";
import HomeRedirect from "./HomeRedirect";

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
