import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  padding: 0.2em 0;
  border-radius: ${props => (props.color ? "10px" : "")};
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: ${props => props.color || "#fff"};
  p {
    font-size: 0.6em;
    text-align: center;
    padding-bottom: .2em;
  }

  p.t {
    font-size: 0.5em;
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
      name: "",
      timing: "",
      venue: "",
      instructor: "",
      code: ""
    };
  }

  componentDidMount() {
    if (this.props.data) {
      this.setState({
        name: this.props.data.name,
        timing: this.props.data.timing,
        venue: this.props.data.venue,
        instructor: this.props.data.instructor,
        code: this.props.data.code
      });
    }
  }
  render() {
    return (
      <React.Fragment>
        <Container
          color={this.props.data.color}
          start={this.props.data.start}
          end={this.props.data.end}
        >
          <p className="b">{this.state.code}</p>
          <p className="b">{this.state.name}</p>
          <p>{this.state.venue}</p>
          <p className="t">{this.state.timing}</p>
          <p>
            {this.state.instructor
              ? "Instructors : " + this.state.instructor
              : ""}
          </p>
        </Container>
      </React.Fragment>
    );
  }
}

export default Cell;
