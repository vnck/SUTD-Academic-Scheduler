import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;

  button {
    padding: 1rem;
    border: none;
    text-align: center;
    text-decoration: none;
    background-color: ${props => props.theme.accent};
    color: ${props => props.theme.white};
    font-weight: 600;
    border-radius: 6px;
    outline: none;
    cursor: pointer;
  }

  button:hover {
    background-color: ${props => props.theme.accentdark};
  }

  button:active {
    background-color: ${props => props.theme.accentdark};
  }

  button:focus {
    box-shadow: 0 0 0 2px ${props => props.theme.accentdark};
  }
`;

class GeneratorButton extends Component {
  constructor(props) {
    super(props);
    this.confirmRequest = this.confirmRequest.bind(this);
  }

  confirmRequest() {
    var r = window.confirm("Are you sure?\nThis action cannot be undone.");
    if (r == true) {
      alert("Generated New Schedule");
    }
  }

  render() {
    return (
      <React.Fragment>
        <Container>
          <button type="button" onClick={this.confirmRequest}>
            Generate New Schedule
          </button>
        </Container>
      </React.Fragment>
    );
  }
}

export default GeneratorButton;
