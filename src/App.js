import React, { Component } from "react";
import styled, { ThemeProvider } from "styled-components";
import { GlobalStyle } from "./theme/globalStyle";
import { theme } from "./theme/theme";
import CoordinatorHome from "./components/CoordinatorHome";
import Login from "./components/Login";

class App extends Component {
  render() {
    return (
      <ThemeProvider theme={theme}>
        <React.Fragment>
          <Login/>
          <GlobalStyle />
        </React.Fragment>
      </ThemeProvider>
    );
  }
}

export default App;
