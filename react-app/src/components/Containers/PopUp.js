import React, { Component } from "react";
import styled from "styled-components";

const OuterPopup = styled.div`
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
`;

const InnerPopup = styled.div`
  background: white;
  display: flex;
  flex-direction: column;
  border-radius: 0.4rem;
  align-items: center;
`;

const Container = styled.div`
  width: 100%;
  padding: 1em;
`;

const HeaderContainer = styled.div`
  margin-left: auto;
  margin-right: 0;
  padding-top: 0.6em;
  padding-right: 0.6em;
`;

const CancelButton = styled.button`
  padding: 1rem;
  border: none;
  background-color: ${props => props.theme.accent};
  border-radius: 6px;
  outline: none;
  cursor: pointer;

  :hover {
    background-color: ${props => props.theme.accentdark};
  }

  :active {
    background-color: ${props => props.theme.accentdark};
  }

  :focus {
    box-shadow: 0 0 0 2px ${props => props.theme.accentdark};
  }
`;

class PopUp extends Component {
  render() {
    return (
      <OuterPopup>
        <InnerPopup>
          <HeaderContainer>
            <CancelButton onClick={this.props.handler} />
          </HeaderContainer>
          <Container>{this.props.children}</Container>
        </InnerPopup>
      </OuterPopup>
    );
  }
}

export default PopUp;
