import React, { Component } from "react";
import styled from "styled-components";
import Header from "../Containers/Header";
import TableDisplay from "../Schedule/TableDisplay";
import InstFunctionContainer from "../Containers/InstFunctionContainer";

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
        <Header name={this.props.name} handleLogout={this.props.handleLogout} />
        <ContentBody>
          <FlexContainer>
            <FlexChild>
              <h2 className="subheader">Term Schedule</h2>
              <TableDisplay
                name={this.props.name}
                isCoordinator={this.props.isCoordinator}
              />
            </FlexChild>
            <FlexChildW>
              <InstFunctionContainer name={this.props.name} />
            </FlexChildW>
          </FlexContainer>
        </ContentBody>
      </React.Fragment>
    );
  }
}

export default InstructorHome;
