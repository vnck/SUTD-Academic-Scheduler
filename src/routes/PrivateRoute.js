import React from "react";
import { Redirect, Route } from "react-router-dom";

const PrivateRoute = ({
  component: C,
  props: cProps,
  auth: login,
  ...rest
}) => {
  return (
    <Route
      {...rest}
      render={props =>
        login ? (
          <C {...props} {...cProps} />
        ) : (
          <Redirect
            to={{ pathname: "/login", state: { from: props.location } }}
          />
        )
      }
    />
  );
};

export default PrivateRoute;
