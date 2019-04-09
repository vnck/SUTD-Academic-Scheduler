import React, { Component } from "react";
import { ThemeProvider } from "styled-components";
import { withRouter } from "react-router-dom";
import { GlobalStyle } from "./theme/globalStyle";
import { theme } from "./theme/theme";
import Routes from "./routes/Routes";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isAuthenticated: false,
      isAuthenticating: true,
      isCoordinator: false,
      name: ""
    };
  }

  userHasAuthenticated = authenticated => {
    this.setState({ isAuthenticated: authenticated });
  };

  userIsCoordinator = isCoordinator => {
    this.setState({ isCoordinator: isCoordinator });
  };

  setName = name => {
    this.setState({ name: name });
  };

  getName = () => {
    return this.state.name;
  };

  handleLogout = async event => {
    // await logout api
    this.userHasAuthenticated(false);
    this.userIsCoordinator(false);
    this.props.history.push("/login");
    this.setName("");
  };

  async componentDidMount() {
    try {
      // await authentication API
      this.userIsCoordinator(false);
      this.userHasAuthenticated(false);
    } catch (e) {
      alert(e);
    }
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
