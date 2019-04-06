import React, { Component } from "react";
import styled from "styled-components";
import Cell from "./Cell";

const Col = styled.div`
  display: grid;
  grid-template-rows: repeat(19, 50px);
  grid-column-start: ${props => props.idx || ""};
  grid-column-end: ${props => props.idx + 1 || ""};
  border: 1px solid ${props => props.theme.darkestgrey};
`;

const TimeCol = styled.div`
  background-color: ${props => props.theme.white};
  border: 1px solid ${props => props.theme.darkestgrey};
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 0.6em;
  font-weight: 600;
  padding: 0 1rem;
`;

class DayCol extends Component {
  constructor(props) {
    super(props);
    this.condRender = this.condRender.bind(this);
    this.getColorValue = this.getColorValue.bind(this);
  }

  getColorValue = cond => {
    let color = 0;
    this.props.cc.forEach(colorCode => {
      if (colorCode[0] === cond) {
        color = colorCode[1];
      }
    });
    return color;
  };

  condRender = (item, index) => {
    if (item.day != null) {
      return (
        <Cell
          key={index}
          data={item}
          times={this.props.times}
          color={this.getColorValue(item.professors)}
        />
      );
    } else {
      return (
        <TimeCol key={index}>
          <p>{item}</p>
        </TimeCol>
      );
    }
  };

  render() {
    return (
      <React.Fragment>
        <Col>
          {this.props.data
            .filter(item => item != null)
            .map((item, index) => this.condRender(item, index))}
        </Col>
      </React.Fragment>
    );
  }
}

export default DayCol;
