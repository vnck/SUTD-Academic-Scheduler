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

const EmptyContainer = styled(FlexChild)`
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
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
  }

  componentDidMount = () => {
    var that = this;
    fetch("http://localhost:5000/get-requests", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
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
          requests.push(req);
<<<<<<< HEAD
          //requests.push(req);
          console.log(requests);
=======
>>>>>>> c02a2e960a96babc4b092ab88dd100adac0be62d
        }
        that.updateRequests(requests);
      });
  };

  updateRequests = reqs => {
    this.setState({
      requests: reqs
    });
  };

  remRequest = async id => {
<<<<<<< HEAD
	console.log(id);
    try { 
      var newReqls = this.state.requests.filter(r => r.id === id-1);
      this.setState({
        requests: newReqls
      });
    } catch (e) {
      alert(e);
    }
    
=======
    //try {
    //// authentication API
    //fetch("http://localhost:5000/del-request", {
    //method: "POST",
    //headers: {
    //Accept: "application/json",
    //"Content-Type": "application/json"
    //},
    //body: JSON.stringify({
    //id: this.state.id
    //})
    //});
    //var newReqls = this.state.requests.filter(r => r.id === id);
    //this.setState({
    //requests: newReqls
    //});
    //} catch (e) {
    //alert(e);
    //}
>>>>>>> c02a2e960a96babc4b092ab88dd100adac0be62d
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          {this.state.requests.length === 0 && (
            <EmptyContainer>
              <p>No requests.</p>
            </EmptyContainer>
          )}
          {this.state.requests.map((request, index) => (
            <FlexChild key={request.requester + index}>
              <RequestCard request={request} remRequest={this.remRequest} />
            </FlexChild>
          ))}
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default RequestContainer;
