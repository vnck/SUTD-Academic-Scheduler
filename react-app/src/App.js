import React, { Component } from "react";
import { ThemeProvider } from "styled-components";
import { withRouter } from "react-router-dom";
import { GlobalStyle } from "./theme/globalStyle";
import { theme } from "./theme/theme";
import Routes from "./routes/Routes";
import Cookies from "universal-cookie";

class App extends Component {
  constructor(props) {
    super(props);

    this.cookies = new Cookies();

    this.state = {
      isAuthenticated: false,
      isAuthenticating: true,
      isCoordinator: false,
      name: ""
    };
  }

  // componentDidMount = () => {
  //   if (this.cookies.get("authenticated") === "TRUE") {
  //     this.setState({ isAuthenticated: true });
  //     if (this.cookies.get("isCoordinator") === "TRUE") {
  //       this.setState({ isCoordinator: true });
  //     } else if (this.cookies.get("isCoordinator") === "FALSE") {
  //       this.setState({ isCoordinator: false });
  //     }
  //   }
  //   this.props.history.push("/login");
  // };

  userHasAuthenticated = authenticated => {
    this.setState({ isAuthenticated: authenticated });
    if (authenticated) {
      this.cookies.set("authenticated", "TRUE", { path: "/" });
    }
  };

  userIsCoordinator = isCoordinator => {
    this.setState({ isCoordinator: isCoordinator });
    if (isCoordinator) {
      this.cookies.set("isCoordinator", "TRUE", { path: "/" });
    } else if (!isCoordinator) {
      this.cookies.set("isCoordinator", "FALSE", { path: "/" });
    }
  };

  setName = name => {
    this.setState({ name: name });
    this.cookies.set("name", name, { path: "/" });
  };

  getName = () => {
    return this.state.name;
  };

  handleLogout = async event => {
    // await logout api
    this.cookies.set("authenticated", "FALSE", { path: "/" });
    this.cookies.set("isCoordinator", "", { path: "/" });
    this.cookies.set("name", "", { path: "/" });
    this.userHasAuthenticated(false);
    this.userIsCoordinator(false);
    this.props.history.push("/login");
    this.setName("");
  };

  async componentDidMount() {
    this.setState({ isAuthenticating: false });
  }

  render() {
    const childProps = {
      isAuthenticated: this.state.isAuthenticated,
      userHasAuthenticated: this.userHasAuthenticated,
      handleLogout: this.handleLogout,
      isCoordinator: this.state.isCoordinator,
      userIsCoordinator: this.userIsCoordinator,
      setName: this.setName,
      name: this.state.name
    };
    return (
      !this.state.isAuthenticating && (
        <ThemeProvider theme={theme}>
          <React.Fragment>
            <Routes childProps={childProps} />
            <GlobalStyle />
          </React.Fragment>
        </ThemeProvider>
      )
    );
  }
}

export default withRouter(App);
