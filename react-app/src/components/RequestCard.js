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
      day: "",
      requester: "",
      startTime: "",
      endTime: "",
      reason: ""
    };
  }

  componentDidMount() {
    if (this.props.request) {
      this.setState({
        day: this.props.request.day,
        requester: this.props.request.requester,
        startTime: this.props.request.startTime,
        endTime: this.props.request.endTime,
        reason: this.props.request.reason
      });
    }
  }

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
            <ButtonChild>
              <ApproveButton>Approve</ApproveButton>
            </ButtonChild>
            <ButtonChild>
              <CancelButton>Reject</CancelButton>
            </ButtonChild>
          </ButtonContainer>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default RequestCard;
