import React, { Component } from "react";
import styled, { ThemeProvider } from "styled-components";
import Header from "./Header";
import TableDisplay from "./TableDisplay";
import InstFunctionContainer from "./InstFunctionContainer";

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

class InstructorHome extends Component {
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
              <InstFunctionContainer />
            </FlexChildW>
          </FlexContainer>
        </ContentBody>
      </React.Fragment>
    );
  }
}

export default InstructorHome;
