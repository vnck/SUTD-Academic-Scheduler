import React, { Component } from "react";
import styled from "styled-components";
import RequestCard from "../RequestCard";

const FlexContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  justify-content: flex-start;
  background-color: #ddd;
  border-radius: 0.6rem;
  width: 100%;
  padding: 0.4rem;
`;

const FlexChild = styled.div`
  padding: 0.2em;
`;

class RequestContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requests: [
        {
          day: "Monday",
          requester: "John. O",
          startTime: "8.00AM",
          endTime: "9.00AM",
          reason: "Commutation in the morning."
        },
        {
          day: "Wednesday",
          requester: "John. O",
          startTime: "4.00PM",
          endTime: "5.00PM",
          reason: "Family"
        }
      ]
    };
  }
  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          {this.state.requests.map((request, index) => (
            <FlexChild key={request.requester + index}>
              <RequestCard request={request} />
            </FlexChild>
          ))}
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default RequestContainer;
