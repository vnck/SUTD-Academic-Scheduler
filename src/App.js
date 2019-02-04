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
      isAuthenticating: true
    };
  }

  userHasAuthenticated = authenticated => {
    this.setState({ isAuthenticated: authenticated });
  };

  handleLogout = async event => {
    // await logout api
    this.userHasAuthenticated(false);
    this.props.history.push("/login");
  };

  async componentDidMount() {
    try {
      // await authentication API
      // this.userHasAuthenticated(true);
    } catch (e) {
      alert(e);
    }
    this.setState({ isAuthenticating: false });
  }

  render() {
    const childProps = {
      isAuthenticated: this.state.isAuthenticated,
      userHasAuthenticated: this.userHasAuthenticated,
      handleLogout: this.handleLogout
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
