import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;

  button {
    width: 100%;
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

  button:hover:enabled {
    background-color: ${props => props.theme.accentdark};
  }

  button:active:enabled {
    background-color: ${props => props.theme.accentdark};
  }

  button:focus:enabled {
    box-shadow: 0 0 0 2px ${props => props.theme.accentdark};
  }

  button:disabled {
    background-color: ${props => props.theme.accentdark};
    cursor: default;
  }
`;

class GeneratorButton extends Component {
  constructor(props) {
    super(props);

    this.state = {
      generate_status: "Generate New Schedule",
      generate_button_disabled: false
    };

    this.confirmRequest = this.confirmRequest.bind(this);
    this.generateSchedule = this.generateSchedule.bind(this);
  }

  componentDidMount = () => {
    fetch("http://localhost:5000/get-schedule-status", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then(result => result.json())
      .then(response => {
        if (response.message) {
          this.setState({
            generate_status: "Generating Schedule...",
            generate_button_disabled: true
          });
        }
      });
  };

  generateSchedule = () => {
    this.setState({
      generate_status: "Generating Schedule...",
      generate_button_disabled: true
    });
    fetch("http://localhost:5000/generate-schedule", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    }).then(response => {
      console.log(response);
      if (response.status === 200) {
        this.setState({
          generate_status: "Generate New Schedule",
          generate_button_disabled: false
        });
      }
    });
  };

  confirmRequest = () => {
    var r = window.confirm("Are you sure?\nThis action cannot be undone.");
    if (r === true) {
      this.generateSchedule();
    }
  };

  render() {
    return (
      <React.Fragment>
        <Container>
          <button
            type="button"
            disabled={this.state.generate_button_disabled}
            onClick={this.confirmRequest}
          >
            {this.state.generate_status}
          </button>
        </Container>
      </React.Fragment>
    );
  }
}

export default GeneratorButton;
