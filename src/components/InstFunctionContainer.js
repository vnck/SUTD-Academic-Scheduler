import React, { Component } from "react";
import styled from "styled-components";
import Downloader from "./Downloader";
import CustomisePreferences from "./CustomisePreferences";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding-left: 3rem;
`;

class InstFunctionContainer extends Component {
  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <Downloader />
          <CustomisePreferences />
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default InstFunctionContainer;
