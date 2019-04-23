import React, { Component } from "react";
import styled from "styled-components";
import Downloader from "../Buttons/Downloader";
import GeneratorButton from "../Buttons/GeneratorButton";
import PopUp from "../Containers/PopUp";
import EventForm from "../EventForm";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding-left: 3rem;
`;

class CoordFunctionContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      popup: false
    };
    this.cancelPopup = this.cancelPopup.bind(this);
    this.callPopup = this.callPopup.bind(this);
  }

  cancelPopup = () => {
    this.setState({ popup: false });
  };

  callPopup = () => {
    this.setState({ popup: true });
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          {/* <h3>Coordinator Menu</h3> */}
          {/* <AddEvent handler={this.callPopup} reqHandler={this.updateRequests} /> */}
          {/* <Uploader /> */}
          <Downloader name={this.props.name} isCoordinator={true} />
          <GeneratorButton />
        </FlexContainer>
        {this.state.popup && (
          <PopUp handler={this.cancelPopup}>
            <EventForm handler={this.cancelPopup} />
          </PopUp>
        )}
      </React.Fragment>
    );
  }
}

export default CoordFunctionContainer;
