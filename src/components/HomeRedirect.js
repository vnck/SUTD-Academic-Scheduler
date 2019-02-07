import React, { Component } from "react";
import styled from "styled-components";

const FlexContainer = styled.div`
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: ${props => props.theme.accent};
  color: ${props => props.theme.white};
`;

class HomeRedirect extends Component {
  componentDidMount() {
    console.log(this.props);
    if (this.props.isAuthenticated) {
      if (this.props.isCoordinator) {
        this.props.history.push("/coordinator-home");
      } else if (!this.props.isCoordinator) {
        this.props.history.push("/instructor-home");
      }
    } else {
      this.props.history.push("/login");
    }
  }
  render() {
    return (
      <React.Fragment>
        <FlexContainer />
      </React.Fragment>
    );
  }
}

export default HomeRedirect;
