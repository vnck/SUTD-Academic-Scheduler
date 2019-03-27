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

  h1.header {
    margin-bottom: 3rem;
  }

  form {
    display: flex;
    flex-direction: column;
    font-size: 1.2em;
  }

  input {
    background-color: ${props => props.theme.white};
    border: none;
    padding: 0.3em;
    font-size: 1.2em;
    margin: 0.2em 0;
    outline: none;
  }

  input::placeholder {
    color: ${props => props.theme.greydark};
  }

  label.psw {
    margin-top: 0.5em;
  }

  button {
    margin-top: 2em;
    padding: 0.3em;
    font-size: 1.2em;
    font-weight: 600;
    border: none;
    background-color: ${props => props.theme.white};
    color: ${props => props.theme.accentdark};
    border-radius: 4px;
    outline: none;
    cursor: pointer;
  }

  button:hover:enabled {
    background-color: ${props => props.theme.silver};
  }

  button:disabled {
    color: ${props => props.theme.grey};
  }

  button:active:enabled {
    background-color: ${props => props.theme.grey};
  }

  button:focus {
    box-shadow: 0 0 0 4px ${props => props.theme.accentdark};
  }
`;

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: "",
      password: ""
    };
    this.validateForm = this.validateForm.bind(this);
    this.updateUser = this.updateUser.bind(this);
    this.updatePassword = this.updatePassword.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    this.props.userHasAuthenticated(true);
    this.props.userIsCoordinator(true);
    this.props.history.push("/coordinator-home");
  }

  validateForm = () => {
    return this.state.user.length > 0 && this.state.password.length > 0;
  };

  updateUser = value => {
    this.setState({
      user: value
    });
  };

  updatePassword = value => {
    this.setState({
      password: value
    });
  };

  handleSubmit = async event => {
    event.preventDefault();
    var that = this;
    try {
      // authentication API
      fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user: this.state.user,
          password: this.state.password
        })
      })
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          if (data.isAuthenticated) {
            that.props.userHasAuthenticated(data.isAuthenticated);
            that.props.userIsCoordinator(data.isCoordinator);

            if (data.isCoordinator) {
              that.props.history.push("/coordinator-home");
            } else {
              that.props.history.push("/instructor-home");
            }
          } else {
            alert("Failed to Log In.");
            that.props.history.push("/login");
          }
        });
    } catch (e) {
      alert(e);
    }
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <h1 className="header">SUTD Academic Scheduler</h1>
          <form>
            <label htmlFor="user">Staff ID</label>
            <input
              type="text"
              name="user"
              placeholder="Enter ID"
              onChange={event => {
                this.updateUser(event.target.value);
              }}
              value={this.state.user}
            />
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              placeholder="Enter Password"
              checked={this.state.acceptedTerms}
              onChange={event => {
                this.updatePassword(event.target.value);
              }}
              value={this.state.password}
            />
            <button disabled={!this.validateForm()} onClick={this.handleSubmit}>
              Submit
            </button>
          </form>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default Login;
