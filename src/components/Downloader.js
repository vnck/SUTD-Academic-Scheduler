import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  display: flex;
  justify-content: center;
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

class Downloader extends Component {
  render() {
    return (
      <React.Fragment>
        <Container>
          <button type="button">Download CSV</button>
        </Container>
      </React.Fragment>
    );
  }
}

export default Downloader;
