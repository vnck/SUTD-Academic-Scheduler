import React, { Component } from "react";
import styled from "styled-components";
import Downloader from "../Buttons/Downloader";
import Uploader from "../Buttons/Uploader";
import GeneratorButton from "../Buttons/GeneratorButton";
import AddEvent from "../Buttons/AddEvent";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding-left: 3rem;
`;

class CoordFunctionContainer extends Component {
  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          {/* <h3>Coordinator Menu</h3> */}
          <AddEvent />
          <Uploader />
          <Downloader />
          <GeneratorButton />
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default CoordFunctionContainer;
