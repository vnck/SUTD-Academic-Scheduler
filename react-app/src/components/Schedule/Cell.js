import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  padding: 0.1em 0;
  border-radius: ${props => (props.color != null ? "10px" : "")};
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: hsl(${props => props.color || 0}, 50%, 75%);
  p {
    font-size: 0.5em;
    text-align: center;
  }

  p.t {
    font-size: 0.3em;
  }

  p.b {
    font-weight: 600;
  }
  grid-row-start: ${props => props.start || ""};
  grid-row-end: ${props => props.end || ""};
`;

class Cell extends Component {
  constructor(props) {
    super(props);
    this.state = {
      course: "",
      day: 0,
      endTime: 0,
      professors: "",
      room: "",
      startTime: 0,
      studentGroups: "",
      timing: ""
    };
  }

  componentDidMount() {
    if (this.props.data) {
      this.setState({
        course: this.props.data.course,
        day: this.props.data.day,
        endTime: (this.props.data.endTime - 8.5) * 2,
        professors: this.props.data.professors,
        room: this.props.data.room,
        startTime: (this.props.data.startTime - 8.5) * 2,
        studentGroups: this.props.data.studentGroups,
        timing:
          this.props.times[(this.props.data.startTime - 8.5) * 2] +
          "-" +
          this.props.times[(this.props.data.endTime - 8.5) * 2]
      });
    }
  }

  componentDidUpdate(prevProps) {
    if (prevProps.data !== this.props.data) {
      this.setState({
        course: this.props.data.course,
        day: this.props.data.day,
        endTime: (this.props.data.endTime - 8.5) * 2,
        professors: this.props.data.professors,
        room: this.props.data.room,
        startTime: (this.props.data.startTime - 8.5) * 2,
        studentGroups: this.props.data.studentGroups,
        timing:
          this.props.times[(this.props.data.startTime - 8.5) * 2] +
          "-" +
          this.props.times[(this.props.data.endTime - 8.5) * 2]
      });
    }
  }

  render() {
    return (
      <React.Fragment>
        <Container
          color={this.props.color}
          start={this.state.startTime + 1}
          end={this.state.endTime + 1}
        >
          <p className="b">{this.state.course}</p>
          <p className="b">{this.state.course}</p>
          <p>{this.state.studentGroups}</p>
          <p>{this.state.room}</p>
          <p className="t">{this.state.timing}</p>
          <p>{this.state.professors}</p>
        </Container>
      </React.Fragment>
    );
  }
}

export default Cell;
