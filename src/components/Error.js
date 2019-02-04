import React, { Component } from "react";
import styled from "styled-components";

const FlexContainer = styled.div`
width: 100vw;
height: 100vh;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
background-color: ${props => props.theme.accent}
color: ${props => props.theme.white}
`;

class Error extends Component {
  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <h1>Page Not Found</h1>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default Error;
