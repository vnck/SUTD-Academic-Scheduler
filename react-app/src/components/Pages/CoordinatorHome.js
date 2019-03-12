import React, { Component } from "react";
import styled, { ThemeProvider } from "styled-components";
import Header from "../Containers/Header";
import TableDisplay from "../Schedule/TableDisplay";
import CoordFunctionContainer from "../Containers/CoordFunctionContainer";
import RequestContainer from "../Containers/RequestContainer";

const ContentBody = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;

  padding: 0.6rem;
  padding-top: 4rem;

  .subheader {
    margin-bottom: 1rem;
  }
`;

const FlexContainer = styled.div`
  display: flex;
  justify-content: center;
  width: 80%;
`;

const FlexChild = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const FlexChildW = styled.div`
  width: 30%;
  padding-top: 2.5rem;
`;

const Container = styled.div`
  width: 72%;
  margin-top: 3rem;
  margin-bottom: 3rem;

  p.header {
    font-weight: 700;
    padding-bottom: 0.5em;
  }
`;

class CoordinatorHome extends Component {
  render() {
    return (
      <React.Fragment>
        <Header handleLogout={this.props.handleLogout} />
        <ContentBody>
          <FlexContainer>
            <FlexChild>
              <h2 className="subheader">Term Schedule</h2>
              <TableDisplay />
            </FlexChild>
            <FlexChildW>
              <CoordFunctionContainer />
            </FlexChildW>
          </FlexContainer>
          <Container>
            <p className="header">Requests</p>
            <RequestContainer />
          </Container>
        </ContentBody>
      </React.Fragment>
    );
  }
}

export default CoordinatorHome;
