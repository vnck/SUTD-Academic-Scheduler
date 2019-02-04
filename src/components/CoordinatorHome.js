import React, { Component } from "react";
import styled, { ThemeProvider } from "styled-components";
import Header from "./Header";
import TableDisplay from "./TableDisplay";
import Downloader from "./Downloader";

const ContentBody = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;

  padding: 0.6rem;
  padding-top: 3rem;

  .subheader {
    margin-bottom: 1rem;
  }
`;

const FlexContainer = styled.div`
  display: flex;
  justify-content: center;
  width: 80%;
`;

class CoordinatorHome extends Component {
  render() {
    return (
      <React.Fragment>
        <Header handleLogout={this.props.handleLogout} />
        <ContentBody>
          <h2 className="subheader">Term Schedule</h2>
          <FlexContainer>
            <TableDisplay />
          </FlexContainer>
          <Downloader />
        </ContentBody>
      </React.Fragment>
    );
  }
}

export default CoordinatorHome;
