import React, { Component } from "react";
import styled from "styled-components";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: 0.6em;
  padding: 1em;
  font-size: 0.6rem;
`;

const StyledHeader = styled.div`
  font-weight: 700;
  p {
    margin-bottom: 0.2rem;
  }
`;

const StyledDiv = styled.div`
  margin-bottom: 1.4em;
`;

const ButtonContainer = styled.div`
  display: flex;
  width: 100%;
`;

const ButtonChild = styled.div`
  flex-grow: 1;
  padding: 0.2rem;
`;

const ApproveButton = styled.button`
  padding: 0.4rem 1rem;
  border: none;
  background-color: ${props => props.theme.accent};
  color: ${props => props.theme.white};
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

const CancelButton = styled.button`
  padding: 0.4rem 1rem;
  border: none;
  background-color: ${props => props.theme.grey};
  border-radius: 6px;
  outline: none;
  cursor: pointer;

  :hover {
    background-color: ${props => props.theme.darkergrey};
  }

  :active {
    background-color: ${props => props.theme.darkestgrey};
  }

  :focus {
    box-shadow: 0 0 0 2px ${props => props.theme.darkergrey};
  }
`;

class RequestCard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: "",
      day: "",
      requester: "",
      startTime: "",
      endTime: "",
      reason: "",
      status: ""
    };
    this.approveRequest = this.approveRequest.bind(this);
    this.removeRequest = this.removeRequest.bind(this);
    this.setRequests = this.setRequests.bind(this);
  }

  componentDidMount = () => {
    this.setRequests();
  };

  setRequests = () => {
    if (this.props.request) {
      this.setState({
        id: this.props.request.id,
        day: this.props.request.day,
        requester: this.props.request.requester,
        startTime: this.props.request.startTime,
        endTime: this.props.request.endTime,
        reason: this.props.request.reason,
        status: this.props.request.status
      });
    }
  };

  approveRequest = async event => {
    this.setState({
      status: !this.state.status
    });

    event.preventDefault();
    try {
      // authentication API
      fetch("http://localhost:5000/approve-request", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          id: this.state.id,
          status: this.state.status
        })
      });
    } catch (e) {
      alert(e);
    }
  };

  removeRequest = async event => {
    try {
      // authentication API
      fetch("http://localhost:5000/del-request", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          id: this.state.id
        })
      });
      this.props.remRequest(this.state.id);
    } catch (e) {
      alert(e);
    }
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <StyledHeader>
            <p>Every {this.state.day}</p>
            <p>
              {this.state.startTime} - {this.state.endTime}
            </p>
          </StyledHeader>
          <StyledDiv>
            <p>Requested by {this.state.requester}</p>
          </StyledDiv>
          <StyledDiv>
            <p>
              <b>Reason:</b>
            </p>
            <p>{this.state.reason}</p>
          </StyledDiv>
          <ButtonContainer>
            {this.props.isCoordinator && (
              <ButtonChild>
                <ApproveButton onClick={this.approveRequest}>
                  {this.state.status ? "Unapprove" : "Approve"}
                </ApproveButton>
              </ButtonChild>
            )}
            <ButtonChild>
              <CancelButton onClick={this.removeRequest}>Delete</CancelButton>
            </ButtonChild>
          </ButtonContainer>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default RequestCard;
