import React, { Component } from "react";
import styled from "styled-components";
import Cell from "./Cell";

const Col = styled.div`
  display: grid;
  grid-template-rows: repeat(19, 30px);
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
    this.state = {
      data: []
    };
    this.condRender = this.condRender.bind(this);
    this.getColorValue = this.getColorValue.bind(this);
    this.filterConditions = this.filterConditions.bind(this);
  }

  componentDidMount = () => {
    this.setState({
      data: this.props.data
    });
  };

  componentDidUpdate = prevProps => {
    if (prevProps.filter !== this.props.filter) {
      this.setState({
        data: this.props.data.filter(this.filterConditions)
      });
    }
  };

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
          color={this.getColorValue(item.course)}
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

  filterConditions = item => {
    var filterList = this.props.filter;
    if (item.day == null || filterList.every(item => item === "")) {
      return true;
    }
    if (item.professors.includes(filterList[0]) && filterList[0] !== "") {
      return true;
    } else if (item.course === filterList[1] && filterList[1] !== "") {
      return true;
    } else if (item.studentGroups === filterList[2] && filterList[2] !== "") {
      return true;
    }
    return false;
  };

  render() {
    return (
      <React.Fragment>
        <Col>
          {this.state.data
            .filter(item => item != null)
            .map((item, index) => this.condRender(item, index))}
        </Col>
      </React.Fragment>
    );
  }
}

export default DayCol;
