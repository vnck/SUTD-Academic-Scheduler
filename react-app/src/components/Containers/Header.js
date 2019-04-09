import React, { Component } from "react";
import styled from "styled-components";

const StyledHeader = styled.div`
  background-color: ${props => props.theme.accent};
  color: ${props => props.theme.white};
  display: flex;
  justify-content: space-between;
  align-items: center;

  position: fixed;
  top: 0;
  width: 100%;
  z-index: 999;
`;

const Title = styled.a`
  font-size: 1.2rem;
  padding: 0.5rem 0.5rem 0.5rem 1rem;
  margin-left: 10rem;
  color: ${props => props.theme.white};
  text-decoration: none;
  @media screen and (max-width: 600px) {
    font-size: 1rem;
    text-align: left;
    width: 100%;
    margin-left: 0.5rem;
  }
`;

const LogoutButton = styled.button`
  padding: 1rem 2rem;
  border: none;
  text-align: center;
  text-decoration: none;
  color: ${props => props.theme.white};
  background-color: ${props => props.theme.accentdark};
  font-weight: 600;
  outline: none;
  cursor: pointer;
`;

class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isHide: false
    };
  }

  render() {
    return (
      <StyledHeader>
        <Title href="/">SUTD Scheduler</Title>
        <p>Welcome, {this.props.name}</p>
        <LogoutButton onClick={this.props.handleLogout}>LOG OUT</LogoutButton>
      </StyledHeader>
    );
  }
}

export default Header;
