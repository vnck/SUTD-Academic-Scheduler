import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;

  a {
    display: inline-block;
    width: 100%;
    padding: 1rem;
    border: none;
    text-align: center;
    text-decoration: none;
    background-color: ${props => props.theme.grey};
    color: ${props => props.theme.black};
    font-weight: 600;
    border-radius: 6px;
    font-size: 11px;
    white-space: nowrap;
    outline: none;
    cursor: pointer;
  }

  a:hover {
    background-color: ${props => props.theme.darkergrey};
  }

  a:active {
    background-color: ${props => props.theme.darkestgrey};
  }

  a:focus {
    box-shadow: 0 0 0 2px ${props => props.theme.darkestgrey};
  }
`;

class Downloader extends Component {
  constructor(props) {
    super(props);
    this.downloadCSV = this.downloadCSV.bind(this);
  }

  downloadCSV = () => {
    fetch("http://localhost:5000/download-csv", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    }).then(response => {
      console.log(response);
    });
  };

  render() {
    return (
      <React.Fragment>
        <Container>
          {!this.props.isCoordinator ? (
            <a
              href={"http://localhost:5000/schedule/" + this.props.name}
              download={"schedule-" + this.props.name + ".csv"}
            >
              Download CSV
            </a>
          ) : (
            <a
              href={"http://localhost:5000/schedule/all"}
              download="schedule.csv"
            >
              Download CSV
            </a>
          )}

          {/* <button onClick={this.downloadCSV}>Download CSV</button> */}
        </Container>
      </React.Fragment>
    );
  }
}

export default Downloader;
