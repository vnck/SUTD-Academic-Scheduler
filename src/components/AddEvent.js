import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;

  button {
    padding: 1rem;
    border: none;
    text-align: center;
    text-decoration: none;
    background-color: ${props => props.theme.grey};
    font-weight: 600;
    border-radius: 6px;
    outline: none;
    cursor: pointer;
  }

  button:hover {
    background-color: ${props => props.theme.darkergrey};
  }

  button:active {
    background-color: ${props => props.theme.darkestgrey};
  }

  button:focus {
    box-shadow: 0 0 0 2px ${props => props.theme.darkestgrey};
  }
`;

class AddEvent extends Component {
  constructor(props) {
    super(props);
    this.confirmRequest = this.confirmRequest.bind(this);
  }

  confirmRequest() {
    alert("Add an Event");
  }

  render() {
    return (
      <React.Fragment>
        <Container>
          <button type="button" onClick={this.confirmRequest}>
            Add an Event
          </button>
        </Container>
      </React.Fragment>
    );
  }
}

export default AddEvent;
