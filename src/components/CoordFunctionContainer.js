import React, { Component } from "react";
import styled from "styled-components";
import Downloader from "./Downloader";
import GeneratorButton from "./GeneratorButton";
import AddEvent from "./AddEvent";

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
          <Downloader />
          <GeneratorButton />
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default CoordFunctionContainer;
