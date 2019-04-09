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
  padding: 0.2rem;
`;

const EmptyRequestsContainer = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 3rem;
`;

class RequestContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requests: []
    };
    this.remRequest = this.remRequest.bind(this);
    this.updateRequests = this.updateRequests.bind(this);

    this.RequestCardChild = React.createRef();
  }

  componentDidMount = () => {
    this.updateRequests();
  };

  updateRequests = () => {
    var that = this;
    fetch("http://localhost:5000/get-requests", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(result => result.json())
      .then(items => {
        var requests = [];
        for (var i = 0; i < items.length; i++) {
          var req = {
            id: items[i]["id"],
            day: items[i]["day"],
            requester: items[i]["requester"],
            startTime: items[i]["startTime"],
            endTime: items[i]["endTime"],
            reason: items[i]["reason"],
            status: items[i]["status"]
          };
          if (this.props.name != null) {
            if (req.requester === this.props.name) {
              requests.push(req);
            }
          } else {
            requests.push(req);
          }
        }
        that.setState({
          requests: requests
        });
      });
  };

  remRequest = async id => {
    try {
      let newReqls = this.state.requests.filter(r => r.id !== id);
      this.setState({
        requests: newReqls
      });
      this.RequestCardChild.current.setRequests();
    } catch (e) {
      alert(e);
    }
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          {this.state.requests.length === 0 && (
            <EmptyRequestsContainer>
              <p>No Requests!</p>
            </EmptyRequestsContainer>
          )}
          {this.state.requests.map((request, index) => (
            <FlexChild key={index}>
              <RequestCard
                ref={this.RequestCardChild}
                request={request}
                remRequest={this.remRequest}
                isCoordinator={this.props.isCoordinator}
              />
            </FlexChild>
          ))}
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default RequestContainer;
