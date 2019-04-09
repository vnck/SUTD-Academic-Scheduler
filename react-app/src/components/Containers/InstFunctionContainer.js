import React, { Component } from "react";
import styled from "styled-components";
import Downloader from "../Buttons/Downloader";
import CustomisePreferences from "../Buttons/CustomisePreferences";
import PopUp from "../Containers/PopUp";
import PreferenceForm from "../PreferenceForm";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding-left: 3rem;
`;

class InstFunctionContainer extends Component {
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
          <Downloader />
          <CustomisePreferences handler={this.callPopup} />
        </FlexContainer>
        {this.state.popup && (
          <PopUp handler={this.cancelPopup}>
            <PreferenceForm
              name={this.props.name}
              popUpHandler={this.cancelPopup}
              reqHandler={this.props.reqHandler}
            />
          </PopUp>
        )}
      </React.Fragment>
    );
  }
}

export default InstFunctionContainer;
